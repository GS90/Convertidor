# window.py
#
# Copyright 2025 Golodnikov Sergey
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


import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk

from .convertidor import quantities


@Gtk.Template(resource_path='/tech/digiroad/Convertidor/gtk/window.ui')
class ConvertidorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'Convertidor'

    # structure
    quantities_list = Gtk.Template.Child('quantities-list')

    label_cero = Gtk.Template.Child('label-cero')
    label_uno = Gtk.Template.Child('label-uno')
    label_dos = Gtk.Template.Child('label-dos')
    label_tres = Gtk.Template.Child('label-tres')

    units_cero = Gtk.Template.Child('units-cero')
    units_uno = Gtk.Template.Child('units-uno')
    units_dos = Gtk.Template.Child('units-dos')
    units_tres = Gtk.Template.Child('units-tres')

    # preferences
    pref_dialog = Gtk.Template.Child('pref-dialog')
    pref_theme = Gtk.Template.Child('pref-theme')
    pref_precision = Gtk.Template.Child('pref-precision')
    pref_quantize = Gtk.Template.Child('pref-quantize')
    pref_scientific = Gtk.Template.Child('pref-scientific')

    # other
    overlay = Gtk.Template.Child('overlay')
    show_imperial = Gtk.Template.Child('show-imperial')
    show_legacy = Gtk.Template.Child('show-legacy')
    button_reset = Gtk.Template.Child('button-reset')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # quantities
        for q in quantities:
            ar = Adw.ActionRow(name=q, title=quantities[q]['title'])
            icon_name = 'q-' + q + '-symbolic'
            ar.add_prefix(Gtk.Image.new_from_icon_name(icon_name))
            self.quantities_list.append(ar)
