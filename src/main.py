# main.py
#
# Copyright 2025-2026 Golodnikov Sergey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from decimal import Decimal
import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gio, Adw, Gdk, GLib

from .convertidor import quantities, conversion
from .window import ConvertidorWindow


class ConvertidorApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='tech.digiroad.Convertidor',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/tech/digiroad/Convertidor')
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.about_action, None)
        self.create_action('preferences',
                           self.preferences_action,
                           ['<primary>p'])

    def do_activate(self):
        self.pref = Gio.Settings.new('tech.digiroad.Convertidor')

        self.w = self.props.active_window
        if not self.w:
            self.w = ConvertidorWindow(application=self)
        self.w.set_default_size(self.pref.get_int('width'),
                                self.pref.get_int('height'))
        self.w.present()

        if self.pref.get_boolean('maximized'):
            self.w.maximize()

        self.update_theme()

        self.clipboard = Gdk.Display().get_default().get_clipboard()

        self.structure = (
            (self.w.label_cero, self.w.units_cero, []),
            (self.w.label_uno, self.w.units_uno, []),
            (self.w.label_dos, self.w.units_dos, []),
            (self.w.label_tres, self.w.units_tres, []),
        )

        self.filling, self.entries, self.derived = [], [], []

        self.freeze = False
        self.recent_quantity = (-1, '', [])  # index, key, pattern

        self.w.button_reset.connect('clicked', self.entries_reset_wrapper)

        # displaying derived units of measurement
        self.show_derived = self.pref.get_boolean('derived')
        self.w.show_derived.set_active(self.show_derived)
        self.w.show_derived.connect('toggled', self.state_derived)
        # displaying imperial units of measurement
        self.show_imperial = self.pref.get_boolean('imperial')
        self.w.show_imperial.set_active(self.show_imperial)
        self.w.show_imperial.connect('toggled', self.state_imperial)
        # displaying legacy units of measurement
        self.show_legacy = self.pref.get_boolean('legacy')
        self.w.show_legacy.set_active(self.show_legacy)
        self.w.show_legacy.connect('toggled', self.state_legacy)

        # initialization
        recent_index = self.pref.get_int('quantity')
        recent_ar = self.w.quantities_list.get_row_at_index(recent_index)
        self.quantities_choice(None, recent_ar)
        self.w.quantities_list.select_row(recent_ar)
        self.w.quantities_list.connect('row-selected', self.quantities_choice)

    def quantities_choice(self, _, ar):
        index = ar.get_index()
        if index == self.recent_quantity[0]:
            return
        key = ar.get_name()
        self.recent_quantity = (index, key, quantities[key]['pattern'])
        self.pref.set_int('quantity', index)

        # clear, todo: check
        for element in self.structure:
            for unit in element[2]:
                unit[0].remove(unit[1])
                element[1].remove(unit[0])
            element[1].remove_all()
            element[2].clear()

        self.filling.clear()
        self.entries.clear()
        self.derived.clear()

        # fill
        for index, unit in enumerate(quantities[key]['units']):

            cell = Gtk.Box(hexpand=True, orientation='vertical')
            cell.append(Gtk.Label(halign='start', label=unit[0]))

            cell.set_margin_top(2)
            cell.set_margin_bottom(2)
            cell.set_margin_start(2)
            cell.set_margin_end(2)

            wrapper = Gtk.Box(margin_top=4)
            wrapper.add_css_class('linked')

            entry = Gtk.Entry(
                hexpand=True,
                input_purpose='digits',
                name=str(index),
                # text='0',
            )
            entry.set_size_request(190, -1)

            increment = Gtk.Button(icon_name='plus-symbolic')
            decrement = Gtk.Button(icon_name='minus-symbolic')
            copy = Gtk.Button(icon_name='copy-symbolic')

            entry.connect('changed', self.entry_changed, key)
            increment.connect('clicked', self.entry_increment, entry)
            decrement.connect('clicked', self.entry_decrement, entry)
            copy.connect('clicked', self.entry_copy, entry)

            wrapper.append(entry)
            wrapper.append(increment)
            wrapper.append(decrement)
            wrapper.append(copy)

            cell.append(wrapper)

            derived = False
            if len(unit) > 3:  # optional parameter
                derived = unit[3]

            self.filling.append((unit[2], cell, wrapper, derived))
            self.entries.append(entry)

        self.fill()
        self.visibility()

    def entries_reset(self, skip_name: str = ''):
        self.freeze = True
        for i in self.entries:
            if i.get_name() != skip_name:
                i.set_text('')
        self.freeze = False

    def entries_reset_wrapper(self, _):
        self.entries_reset()
        for element in self.structure:
            element[1].unselect_all()
        self.w.overlay.add_toast(Adw.Toast(title=self.w.ts_reset, timeout=2))

    def entry_get(self, entry) -> tuple[Decimal | str, int | None] | None:
        try:
            text = entry.get_text().replace(',', '.').strip()
            if text == '':
                text = '0'
            decimal = Decimal(text)
            exponent = decimal.as_tuple().exponent
            if type(exponent) is not int:
                return None  # todo: think about it
            return max(decimal, Decimal('0')), exponent
        except BaseException:
            try:
                return entry.get_text().strip(), None
            except BaseException:
                GLib.idle_add(self.entries_reset, entry.get_name())
                return None

    def entry_changed(self, entry, quantity):
        if self.freeze:
            return

        entry_index = entry.get_name()

        value = self.entry_get(entry)
        if value is None:
            return

        result = conversion(quantity,
                            int(entry_index),
                            value[0],
                            self.pref.get_int('precision'),
                            self.pref.get_int('quantize'),
                            self.pref.get_int('scientific'))

        sc = entry.get_style_context()

        if result is None:
            if not sc.has_class('css-error'):
                entry.add_css_class('css-error')
                if self.pref.get_int('theme') == 0:
                    css = '.css-error {color: #660000;}'
                else:
                    css = '.css-error {color: #ff8080;}'
                provider = Gtk.CssProvider()
                provider.load_from_data(css.encode())
                display = Gdk.Display.get_default()
                Gtk.StyleContext.add_provider_for_display(
                    display,
                    provider,
                    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
                )
            return

        if sc.has_class('css-error'):
            entry.remove_css_class('css-error')

        self.freeze = True
        for i in self.entries:
            index = int(i.get_name())
            if index != int(entry_index):
                try:
                    i.set_text(result[index])
                    sc = i.get_style_context()
                    if sc.has_class('css-error'):
                        i.remove_css_class('css-error')
                except BaseException as exception:
                    print('Error:', str(exception))
        self.freeze = False

    def entry_increment(self, _, entry):
        value = self.entry_get(entry)
        if value is not None:
            decimal, exponent = value
            if type(decimal) is Decimal and exponent is not None:
                if exponent < 1:
                    self.freeze = True
                    entry.set_text(str(decimal + Decimal('1')))
                    self.freeze = False
                    self.entry_changed(entry, self.recent_quantity[1])
                    # todo: else?

    def entry_decrement(self, _, entry):
        value = self.entry_get(entry)
        if value is not None:
            decimal, exponent = value
            if type(decimal) is Decimal and exponent is not None:
                if exponent < 1:
                    self.freeze = True
                    decimal = Decimal.max(decimal - Decimal('1'), Decimal('0'))
                    entry.set_text(str(decimal))
                    self.freeze = False
                    self.entry_changed(entry, self.recent_quantity[1])
                    # todo: else?

    def entry_copy(self, _, entry):
        self.clipboard.set(entry.get_text())
        self.w.overlay.add_toast(Adw.Toast(title=self.w.ts_copy, timeout=2))

    def fill(self):
        # clear
        for element in self.structure:
            element[1].remove_all()
            element[2].clear()
        # fill
        for i in self.filling:
            pattern, cell, wrapper, derived = i
            if derived and not self.show_derived:
                continue
            self.structure[pattern][1].insert(cell, -1)
            self.structure[pattern][2].append((cell, wrapper))

    def visibility(self):
        pattern = [None, None, None, None]  # cero, uno, dos, tres

        for i, j in enumerate(self.recent_quantity[2]):
            if j[1] == 'imperial' and not self.show_imperial:
                pattern[i] = None
            elif j[1] == 'legacy' and not self.show_legacy:
                pattern[i] = None
            else:
                pattern[i] = j[0]

        for i, j in enumerate(pattern):
            if j is not None:
                self.structure[i][0].set_text(j)
                self.structure[i][0].set_visible(True)
                self.structure[i][1].set_visible(True)
            else:
                self.structure[i][0].set_text('')
                self.structure[i][0].set_visible(False)
                self.structure[i][1].set_visible(False)

    def state_derived(self, toggle_button):
        state = toggle_button.get_active()
        self.show_derived = state
        self.pref.set_boolean('derived', state)
        self.fill()

    def state_imperial(self, toggle_button):
        state = toggle_button.get_active()
        self.show_imperial = state
        self.pref.set_boolean('imperial', state)
        self.visibility()

    def state_legacy(self, toggle_button):
        state = toggle_button.get_active()
        self.show_legacy = state
        self.pref.set_boolean('legacy', state)
        self.visibility()

    def about_action(self, *args):
        about = Adw.AboutDialog(
            application_name='Convertidor',
            application_icon='tech.digiroad.Convertidor',
            developer_name='Golodnikov Sergey',
            version='1.3.0',
            comments=self.w.ts_comment,
            website='https://digiroad.tech',
            developers=['Golodnikov Sergey <nn19051990@gmail.com>'],
            artists=[
                'Golodnikov Sergey <nn19051990@gmail.com>',
                'GNOME Design Team https://welcome.gnome.org/team/design',
            ],
            copyright='Copyright © 2025 Golodnikov Sergey',
            license_type=Gtk.License.GPL_3_0,
        )
        about.add_link((self.w.ts_src), 'https://github.com/GS90/Convertidor')
        about.present(self.props.active_window)

    def preferences_action(self, widget, _):
        self.w.pref_theme.set_selected(self.pref.get_int('theme'))
        self.w.pref_precision.set_value(self.pref.get_int('precision'))
        self.w.pref_quantize.set_value(self.pref.get_int('quantize'))
        self.w.pref_scientific.set_value(self.pref.get_int('scientific'))
        self.w.pref_dialog.connect('closed', self.preferences_save)
        self.w.pref_dialog.present(self.props.active_window)

    def preferences_save(self, dialog):
        self.pref.set_int('theme',
                          self.w.pref_theme.get_selected())
        self.pref.set_int('precision',
                          int(self.w.pref_precision.get_value()))
        self.pref.set_int('quantize',
                          int(self.w.pref_quantize.get_value()))
        self.pref.set_int('scientific',
                          int(self.w.pref_scientific.get_value()))
        self.update_theme()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)

    def update_theme(self):
        style_manager = Adw.StyleManager.get_default()
        if self.pref.get_int('theme') == 0:
            style_manager.set_color_scheme(Adw.ColorScheme.FORCE_LIGHT)
        else:
            style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

    def do_shutdown(self):
        if self.w.is_maximized():
            self.pref.set_boolean('maximized', True)
        else:
            self.pref.set_boolean('maximized', False)
            window_size = self.w.get_default_size()
            self.pref.set_int('width', window_size[0])
            self.pref.set_int('height', window_size[1])
        Gio.Application.do_shutdown(self)


def main(version):
    app = ConvertidorApplication()
    return app.run(sys.argv)
