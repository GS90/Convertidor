# convertidor.py
#
# Copyright 2025-2026 Golodnikov Sergey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from decimal import Decimal, getcontext
from gettext import gettext as _
import math


constants = {
    # energy
    'Wh': (
        '<b>Watt‑hour (SI)</b>\n'
        '1 Wh = 3600 J (exact)'
    ),
    'eV': (
        '<b>2022 CODATA Value (SI 2019)</b>\n'
        '1 eV = 1.602176634x10−19 J'
    ),
    'erg': (
        '<b>Erg</b>\n'
        '1 erg = 1E-7 J (exact, CGS unit)'
    ),
    'cal (th)': (
        '<b>Thermochemical calorie</b>\n'
        '1 cal (th) = 4.184 J (exact)'
    ),
    'cal (it)': (
        '<b>International Table calorie (IT)</b>\n'
        '1 cal (it) = 4.1868 J (exact)'
    ),
    'ft-pdl': (
        '<b>Foot‑poundal</b>\n'
        '1 ft-pdl = 0.0421401100938048 J (exact)'
    ),
    'ft⋅lbf': (
        '<b>Foot‑pound force (ft⋅lbf)</b>\n'
        '1 ft⋅lbf = 1.3558179483314004 J (exact)'
    ),
    'Btu (th)': (
        '<b>British thermal unit (thermochemical)</b>\n'
        '1 Btu (th) = 1054.3502644383 J'
    ),
    'Btu (it)': (
        '<b>British thermal unit (International Table, IT)</b>\n'
        '1 Btu (it) = 1055.05585262 J'
    ),
    'thm (US)': (
        '<b>Therm (United States)</b>\n'
        '1 thm (US) = 100 000 Btu (it) = 105 480 400 J'
    ),
    'thm (EC)': (
        '<b>Therm (European Community)</b>\n'
        '1 thm (US) = 100 000 Btu (th) ≈ 105 505 585.257 J'
    ),
}


# angle
# area
# digital
# energy
# force
# fuel
# length
# mass
# numbers
# power
# pressure
# speed
# temperature
# force
# time
# volume


# units: (title, decimal, pattern, ![minor]derived, ![minor]constant)


quantities = {

    # concept: smallest unit first (exception: energy)

    'angle': {
        'title': _('Angle'),
        'pattern': (
            (_('Units of measurement'), ''),
        ),
        'units': (
            (_('Second, "'), Decimal('1'), 0),
            (_("Minute, '"), Decimal('60'), 0),
            (_('Grad, ^g'), Decimal('3240'), 0),
            (_('Degree, °'), Decimal('3600'), 0),
            (_('Radian, rad'), Decimal((648000) / math.pi), 0),
            (_('Milliradian, mrad'), Decimal((648000) / 1000 / math.pi), 0),
            # 648000 = 3600 * 180
        ),
    },

    'area': {
        'title': _('Area'),
        'pattern': (
            (_('Metric system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
        ),
        'units': (
            # Metric system
            (_('Square nanometer, nm^2'), Decimal('1'), 0, True),
            (_('Square micrometer μm^2'), Decimal('1E+6'), 0, True),
            (_('Square millimeter, mm^2'), Decimal('1E+12'), 0),
            (_('Square centimeter, cm^2'), Decimal('1E+14'), 0),
            (_('Square decimeter, dm^2'), Decimal('1E+16'), 0, True),
            (_('Square meter, m^2'), Decimal('1E+18'), 0),
            (_('Square dekameter, dam^2'), Decimal('1E+20'), 0, True),
            (_('Are, a'), Decimal('1E+20'), 0),
            (_('Square hectometer, hm^2'), Decimal('1E+22'), 0, True),
            (_('Hectare, ha'), Decimal('1E+22'), 0),
            (_('Square kilometer, km^2'), Decimal('1E+24'), 0, True),
            (_('Square astronomical unit, au^2'),
                Decimal('2.2379522915281197E+40'), 0),
            # Imperial and US customary systems
            (_('Square inch, in^2'), Decimal('6.4516E+14'), 1),
            (_('Square foot, ft^2'), Decimal('92903039999997600'), 1),
            (_('Square foot (US), ft^2'), Decimal('92903411613275790'), 1),
            (_('Square yard, yd^2'), Decimal('836127359999986200'), 1),
            (_('Acre, ac'), Decimal('4.0468564224E+21'), 1),
            (_('Acre (US), ac'), Decimal('4.0468726099999997E+21'), 1),
            (_('Square mile, mi^2'), Decimal('2.589988110336E+24'), 1),
            (_('Square mile (US), mi^2'), Decimal('2.58999847031952E+24'), 1),
        ),
    },

    'digital': {
        'title': _('Digital data'),
        'pattern': (
            (_('Data transfer rates'), ''),
            (_('Size of files and data'), ''),
            (_('Binary contexts'), ''),
        ),
        'units': (
            # Data transfer rates
            (_('Bit, b'), Decimal('1'), 0),
            (_('Kilobit, Kb'), Decimal('1E+3'), 0),
            (_('Megabit, Mb'), Decimal('1E+6'), 0),
            (_('Gigabit, Gb'), Decimal('1E+9'), 0),
            (_('Terabit, Tb'), Decimal('1E+12'), 0),
            (_('Petabit, Pb'), Decimal('1E+15'), 0, True),
            (_('Exabit, Eb'), Decimal('1E+18'), 0, True),
            # Size of files and data
            (_('Byte, B'), Decimal('8'), 1),
            (_('Kilobyte, KB'), Decimal('8E+3'), 1),
            (_('Megabyte, MB'), Decimal('8E+6'), 1),
            (_('Gigabyte, GB'), Decimal('8E+9'), 1),
            (_('Terabyte, TB'), Decimal('8E+12'), 1),
            (_('Petabyte, PB'), Decimal('8E+15'), 1, True),
            (_('Exabyte, EB'), Decimal('8E+18'), 1, True),
            # Binary contexts
            (_('Kibibyte, KiB'), Decimal('8192'), 2),
            (_('Mebibyte, MiB'), Decimal('8388608'), 2),
            (_('Gibibyte, GiB'), Decimal('8589934592'), 2),
            (_('Tebibyte, TiB'), Decimal('8796093022208'), 2),
            (_('Pebibyte, PiB'), Decimal('9007199254740992'), 2, True),
            (_('Exbibyte, EiB'), Decimal('9223372036854775808'), 2, True),
        )
    },

    # attention: the base unit is the Joule
    'energy': {
        'title': _('Energy'),
        'pattern': (
            (_('Joule units'), ''),
            (_('Electrical energy'), ''),
            (_('Other energy units'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
        ),
        'units': (
            # Joule units
            (_('Attojoule, aJ'), Decimal('1E-18'), 0, True),
            (_('Nanojoule, nJ'), Decimal('1E-9'), 0, True),
            (_('Microjoule, μJ'), Decimal('1E-6'), 0, True),
            (_('Millijoule, mJ'), Decimal('1E-3'), 0, True),
            (_('Joule, J'), Decimal('1'), 0),  # base unit
            (_('Kilojoule, kJ'), Decimal('1E+3'), 0),
            (_('Megajoule, MJ'), Decimal('1E+6'), 0),
            (_('Gigajoule, GJ'), Decimal('1E+9'), 0, True),
            (_('Terajoule, TJ'), Decimal('1E+12'), 0, True),
            # Electrical energy
            (_('Watt-hour, Wh'),
                Decimal('3.6E+3'), 1, False, constants['Wh']),
            (_('Kilowatt-hour, kWh'), Decimal('3.6E+6'), 1),
            (_('Megawatt-hour, MWh'), Decimal('3.6E+9'), 1),
            (_('Gigawatt-hour, GWh'), Decimal('3.6E+12'), 1, True),
            # Other energy units
            (_('Electronvolt, eV'),
                Decimal('1.602176634E-19'), 2, False, constants['eV']),
            (_('Erg, erg'), Decimal('1E-7'), 2, False, constants['erg']),
            (_('Calorie (th), cal'),
                Decimal('4.184'), 2, False, constants['cal (th)']),
            (_('Calorie (it), cal'),
                Decimal('4.1868'), 2, False, constants['cal (it)']),
            (_('Kilocalorie (th), kcal'), Decimal('4184'), 2),
            (_('Kilocalorie (it), kcal'), Decimal('4186.8'), 2),
            # Imperial and US customary systems
            (_('Foot-poundal, ft-pdl'),
                Decimal('0.0421401100938048'), 3, False, constants['ft-pdl']),
            (_('Foot-pound, ft⋅lbf'),
                Decimal('1.3558179483314004'), 3, False, constants['ft⋅lbf']),
            (_('British thermal unit (th), Btu'),
                Decimal('1054.3502644383'), 3, False, constants['Btu (th)']),
            (_('British thermal unit (it), Btu'),
                Decimal('1055.05585262'), 3, False, constants['Btu (it)']),
            (_('Therm (US), thm'),
                Decimal('105480400'), 3, False, constants['thm (US)']),
            (_('Therm (EC), thm'),
                Decimal('105505585.257'), 3, False, constants['thm (EC)']),
        )
    },

    'force': {
        'title': _('Force'),
        'pattern': (
            (_('Newton units'), ''),
            (_('Other force units'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
            (_('Legacy units'), 'legacy'),
        ),
        'units': (
            # Newton units
            (_('Attonewton, aN'), Decimal('1'), 0, True),
            (_('Femtonewton, fN'), Decimal('1E+3'), 0, True),
            (_('Piconewton, pN'), Decimal('1E+6'), 0, True),
            (_('Nanonewton, nN'), Decimal('1E+9'), 0, True),
            (_('Micronewton, μN'), Decimal('1E+12'), 0, True),
            (_('Millinewton, mN'), Decimal('1E+15'), 0),
            (_('Centinewton, cN'), Decimal('1E+16'), 0, True),
            (_('Decinewton, dN'), Decimal('1E+17'), 0, True),
            (_('Newton, N'), Decimal('1E+18'), 0),
            (_('Dekanewton, daN'), Decimal('1E+19'), 0, True),
            (_('Hectonewton, hN'), Decimal('1E+20'), 0, True),
            (_('Kilonewton, kN'), Decimal('1E+21'), 0),
            (_('Meganewton, MN'), Decimal('1E+24'), 0),
            (_('Giganewton, GN'), Decimal('1E+27'), 0, True),
            (_('Teranewton, TN'), Decimal('1E+30'), 0, True),
            (_('Petanewton, PN'), Decimal('1E+33'), 0, True),
            (_('Exanewton, EN'), Decimal('1E+36'), 0, True),
            # Other force units
            (_('Dyne, dyn'), Decimal('1E+13'), 1),
            (_('Kilogram-force, kgf'), Decimal('9806650000000272000'), 1),
            (_('Ton-force (metric), tf'), Decimal('9.80665E+21'), 1),
            # Imperial and US customary systems
            (_('Poundal, pdl'), Decimal('138254954375999900'), 2),
            (_('Kip, kip'), Decimal('4.448221615E+21'), 2),
            (_('Ton-force (short)'), Decimal('8.89644323E+21'), 2),
            (_('Ton-force (long)'), Decimal('9.964016418E+21'), 2),
            # Legacy units
            (_('Pond-force, lbf'), Decimal('4448221615254771700'), 3),
        )
    },

    'fuel': {
        'title': _('Fuel consumption'),
        'pattern': (
            (_('Metric system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
        ),
        'units': (
            # Metric system
            (_('Meter per liter, m/L'), 'm/L', 0),
            (_('Kilometer per liter, km/L'), 'km/L', 0),
            (_('Liters per 100 kilometers, L/100 km'), 'L/100 km', 0),
            # Imperial and US customary systems
            (_('Mile per gallon (US), mpg(us)'), 'mpg(us)', 1),
            (_('Mile per gallon (UK), mpg(uk)'), 'mpg(uk)', 1),
        )
    },

    'length': {
        'title': _('Length'),
        'pattern': (
            (_('Metric system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
            (_('Nautical units of length'), ''),
            (_('Astronomical distance units'), ''),
        ),
        'units': (
            # Metric system
            (_('Picometer, pm'), Decimal('1'), 0, True),
            (_('Nanometer, nm'), Decimal('1E+3'), 0, True),
            (_('Micrometer, μm'), Decimal('1E+6'), 0),
            (_('Millimeter, mm'), Decimal('1E+9'), 0),
            (_('Centimeter, cm'), Decimal('1E+10'), 0),
            (_('Decimeter, dm'), Decimal('1E+11'), 0, True),
            (_('Meter, m'), Decimal('1E+12'), 0),
            (_('Kilometer, km'), Decimal('1E+15'), 0),
            # Imperial and US customary systems
            (_('Inch, in'), Decimal('2.54E+10'), 1),
            (_('Inch (US), in'), Decimal('25400050800'), 1),
            (_('Foot, ft'), Decimal('3.048E+11'), 1),
            (_('Foot (US), ft'), Decimal('304800609601.21906'), 1),
            (_('Yard, yd'), Decimal('9.144E+11'), 1),
            (_('Mile, mi'), Decimal('1.609344E+15'), 1),
            (_('Statute mile (US), mi'), Decimal('1609347218694436'), 1),
            # Nautical units of length
            (_('Nautical mile, nmi'), Decimal('1.852E+15'), 2),
            # Astronomical distance units
            (_('Astronomical unit, au'), Decimal('1.4959787069100001E+23'), 3),
            (_('Light-year, ly'), Decimal('9.4607304725808E+27'), 3),
            (_('Parsec, pc'), Decimal('3.085677581E+28'), 3),
        ),
    },

    'mass': {
        'title': _('Weight and Mass'),
        'pattern': (
            (_('Metric system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
            (_('Masses of celestial bodies'), ''),
            (_('Legacy units'), 'legacy'),
        ),
        'units': (
            # Metric system
            (_('Microgram, μg'), Decimal('1'), 0, True),
            (_('Milligram, mg'), Decimal('1E+3'), 0),
            (_('Gram, g'), Decimal('1E+6'), 0),
            (_('Kilogram, kg'), Decimal('1E+9'), 0),
            (_('Tonne, t'), Decimal('1E+12'), 0),
            (_('Kiloton, kt'), Decimal('1E+15'), 0, True),
            # Imperial and US customary systems
            (_('Grain, gr'), Decimal('64798.91'), 1),
            (_('Pennyweight, pwt'), Decimal('1555173.84'), 1),
            (_('Carat, ct'), Decimal('2E+5'), 1),
            (_('Ounce, oz'), Decimal('28349523.125'), 1),
            (_('Pound, lbs'), Decimal('453592370'), 1),
            (_('Hundredweight (US, short), cwt'), Decimal('45359237000'), 1),
            (_('Hundredweight (UK, long), cwt'), Decimal('50802345440'), 1),
            (_('Quarter (US), qr'), Decimal('11339809250'), 1),
            (_('Quarter (UK), qr'), Decimal('12700586360'), 1),
            (_('Stone, st'), Decimal('6350293180'), 1),
            (_('Ton (short), ton'), Decimal('907184740000'), 1),
            (_('Ton (long), ton'), Decimal('1016046908800'), 1),
            # Masses of celestial bodies
            (_("Moon mass"), Decimal('7.348E+31'), 2),
            (_("Earth mass"), Decimal('5.9722E+33'), 2),
            (_("Solar mass"), Decimal('1.988416E+39'), 2),
            # Legacy units
            (_('Quintal, q'), Decimal('1E+11'), 3),
        )
    },

    'numbers': {
        'title': _('Numbers'),
        'pattern': (
            (_('Numeral systems'), ''),
        ),
        'units': (
            (_('Decimal'), 'decimal', 0),
            (_('Hexadecimal'), 'hexadecimal', 0),
            (_('Octal'), 'octal', 0),
            (_('Binary'), 'binary', 0),
        )
    },

    'power': {
        'title': _('Power'),
        'pattern': (
            (_('Watt-based units'), ''),
            (_('Other power units'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
            (_('Legacy units'), 'legacy'),
        ),
        'units': (
            # Watt-based units
            (_('Attowatt, aW'), Decimal('1'), 0, True),
            (_('Femtowatt, fW'), Decimal('1E+3'), 0, True),
            (_('Picowatt, pW'), Decimal('1E+6'), 0, True),
            (_('Nanowatt, nW'), Decimal('1E+9'), 0, True),
            (_('Microwatt, µW'), Decimal('1E+12'), 0, True),
            (_('Milliwatt, mW'), Decimal('1E+15'), 0, True),
            (_('Centiwatt, nW'), Decimal('1E+16'), 0, True),
            (_('Deciwatt, dW'), Decimal('1E+17'), 0, True),
            (_('Watt, W'), Decimal('1E+18'), 0),
            (_('Dekawatt, daW'), Decimal('1E+19'), 0, True),
            (_('Hectowatt, hW'), Decimal('1E+20'), 0, True),
            (_('Kilowatt, kW'), Decimal('1E+21'), 0),
            (_('Megawatt, MW'), Decimal('1E+24'), 0),
            (_('Gigawatt, GW'), Decimal('1E+27'), 0),
            (_('Terawatt, TW'), Decimal('1E+30'), 0, True),
            (_('Petawatt, PW'), Decimal('1E+33'), 0, True),
            (_('Exawatt, EW'), Decimal('1E+36'), 0, True),
            # Other power units
            (_('Erg per second, erg/s'), Decimal('1E+11'), 1),
            (_('Calorie (it) per hour, cal/h'),
                Decimal('1163000000000007'), 1),
            (_('Calorie (it) per second, cal/s'),
                Decimal('4186799999999929000'), 1),
            (_('Ton of refrigeration, TR'), Decimal('3.516852842E+21'), 1),
            # Imperial and US customary systems
            (_('BTU (th) per hour, Btu/h'), Decimal('292874999992899260'), 2),
            (_('Foot pound-force per hour'), Decimal('376616096758177'), 2),
            (_('Foot pound-force per second'),
                Decimal('1355817948329443300'), 2),
            # Legacy units
            (_('Horsepower (imperial), hp'), Decimal('74569987158227022'), 3),
            (_('Horsepower (metric), hp'), Decimal('73549875E+13'), 3),
            (_('Horsepower (electric), hp'), Decimal('746E+18'), 3),
            (_('Horsepower (boiler), hp'), Decimal('9.8095E+21'), 3),
        )
    },

    'pressure': {
        'title': _('Pressure'),
        'pattern': (
            (_('Pascal units'), ''),
            (_('Other pressure units'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
        ),
        'units': (
            # Pascal units
            (_('Attopascal, aPa'), Decimal('1'), 0, True),
            (_('Femtopascal, fPa'), Decimal('1E+3'), 0, True),
            (_('Picopascal, pPa'), Decimal('1E+6'), 0, True),
            (_('Nanopascal, nPa'), Decimal('1E+9'), 0, True),
            (_('Micropascal, µPa'), Decimal('1E+12'), 0, True),
            (_('Millipascal, mPa'), Decimal('1E+15'), 0, True),
            (_('Centipascal, cPa'), Decimal('1E+16'), 0, True),
            (_('Decipascal, dPa'), Decimal('1E+17'), 0, True),
            (_('Pascal, Pa'), Decimal('1E+18'), 0),
            (_('Dekapascal, daPa'), Decimal('1E+19'), 0, True),
            (_('Hectopascal, hPa'), Decimal('1E+20'), 0, True),
            (_('Kilopascal, kPa'), Decimal('1E+21'), 0),
            (_('Megapascal, MPa'), Decimal('1E+24'), 0),
            (_('Gigapascal, GPa'), Decimal('1E+27'), 0),
            (_('Terapascal, TPa'), Decimal('1E+30'), 0, True),
            (_('Petapascal, PPa'), Decimal('1E+33'), 0, True),
            (_('Exapascal, PPa'), Decimal('1E+36'), 0, True),
            # Other pressure units
            (_('Millibar, mbar'), Decimal('1E+20'), 1),
            (_('Millimetre of mercury, mmHg'), Decimal('1.33322387E+20'), 1),
            (_('Torr'), Decimal('133322368421082810000'), 1),
            (_('Atmosphere (technical), at'), Decimal('9.80665E+22'), 1),
            (_('Bar, bar'), Decimal('1E+23'), 1),
            (_('Atmosphere (standard), atm'), Decimal('1.01325E+23'), 1),
            # Imperial and US customary systems
            (_('Inch of mercury (60°F), inHg'), Decimal('3.37685E+21'), 2),
            (_('Inch of mercury (32°F), inHg'), Decimal('3.38638E+21'), 2),
            (_('Pound per square inch, psi'),
                Decimal('6.894757293E+21'), 2),
            (_('Kilopound per square inch, ksi'),
                Decimal('6.894757293E+24'), 2),
        )
    },

    'speed': {
        'title': _('Speed'),
        'pattern': (
            (_('Metric system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
            (_('Other speed units'), ''),
        ),
        'units': (
            # Metric system
            (_('Millimeter per Hour, mm/h'), Decimal('1'), 0, True),
            (_('Millimeter per Minute, mm/min'), Decimal('60'), 0, True),
            (_('Millimeter per Second, mm/s'), Decimal('3600'), 0, True),
            (_('Centimeter per Hour, cm/h'), Decimal('10'), 0, True),
            (_('Centimeter per Minute, cm/min'), Decimal('600'), 0, True),
            (_('Centimeter per Second, cm/s'), Decimal('36000'), 0, True),
            (_('Meter per Hour, m/h'), Decimal('1000'), 0, True),
            (_('Meter per Minute, m/min'), Decimal('60000'), 0),
            (_('Meter per Second, m/s'), Decimal('3600000'), 0),
            (_('Kilometer per Hour, km/h'), Decimal('1000000'), 0),
            (_('Kilometer per Minute, km/min'), Decimal('60000000'), 0),
            (_('Kilometer per Second, km/s'), Decimal('3600000000'), 0, True),
            # Imperial and US customary systems
            (_('Feet per Hour, ft/h'), Decimal('304.8'), 1, True),
            (_('Feet per Minute, ft/min'), Decimal('18288'), 1),
            (_('Feet per Second, ft/s'), Decimal('1097280'), 1),
            (_('Yard per Hour, yd/h'), Decimal('914.4'), 1, True),
            (_('Yard per Minute, yd/min'), Decimal('54864'), 1, True),
            (_('Yard per Second, yd/s'), Decimal('3291840'), 1),
            (_('Mile per Hour, mi/h'), Decimal('1609344'), 1),
            (_('Mile per Minute, mi/min'), Decimal('96560640'), 1, True),
            (_('Mile per Second, mi/s'), Decimal('5793638400'), 1, True),
            # Other speed units
            (_('Knot, kn'), Decimal('1852000'), 2),
            (_('Mach (SI)'), Decimal('1062167040'), 2),
            (_('Mach (20°C, 1 atm)'), Decimal('1236960000'), 2),
            (_('Cosmic velocity - first'), Decimal('28440000000'), 2),
            (_('Cosmic velocity - second'), Decimal('40320000000'), 2),
            (_('Cosmic velocity - third'), Decimal('60012000000'), 2),
            (_("Earth's velocity"), Decimal('107154000000'), 2),
            (_('Speed of light (vacuum)'), Decimal('1079252848799998'), 2),
        )
    },

    'temperature': {
        'title': _('Temperature'),
        'pattern': (
            (_('SI system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
            (_('Legacy units'), 'legacy'),

        ),
        'units': (
            # SI system
            (_('Celsius, °C'), 'celsius', 0),
            (_('Kelvin, K'), 'kelvin', 0),
            # Imperial and US customary systems
            (_('Fahrenheit, °F'), 'fahrenheit', 1),
            (_('Rankine, °R'), 'rankine', 1),
            # Legacy units
            (_('Reaumur, °r'), 'reaumur', 2),
        )
    },

    'time': {
        'title': _('Time'),
        'pattern': (
            (_('Units of time'), ''),
        ),
        'units': (
            (_('Attosecond, as'), Decimal('1'), 0, True),
            (_('Femtosecond, fs'), Decimal('1E+3'), 0, True),
            (_('Picosecond, fs'), Decimal('1E+6'), 0, True),
            (_('Nanosecond, ns'), Decimal('1E+9'), 0),
            (_('Microsecond, μs'), Decimal('1E+12'), 0),
            (_('Millisecond, ms'), Decimal('1E+15'), 0),
            (_('Second, s'), Decimal('1E+18'), 0),
            (_('Minute, min'), Decimal('6E+19'), 0),
            (_('Hour, h'), Decimal('3.6E+21'), 0),
            (_('Day, d'), Decimal('8.64E+22'), 0),
            (_('Week'), Decimal('6.048E+23'), 0),
            (_('Month'), Decimal('2.628E+24'), 0),
            (_('Year (365 days), y'), Decimal('3.1535999999999997E+25'), 0),
            (_('Decade'), Decimal('3.155759999E+26'), 0),
            (_('Century'), Decimal('3.155759999E+27'), 0),
            (_('Millennium'), Decimal('3.155759999E+28'), 0),
        )
    },

    'volume': {
        'title': _('Volume'),
        'pattern': (
            (_('Metric system'), ''),
            (_('Imperial and US customary systems'), 'imperial'),
        ),
        'units': (
            # Metric system
            (_('Cubic millimeter, mm^3'), Decimal('1'), 0),
            (_('Cubic centimeter, cm^3'), Decimal('1E+3'), 0),
            (_('Cubic decimeter, dm^3'), Decimal('1E+6'), 0),
            (_('Cubic meter, m^3'), Decimal('1E+9'), 0),
            (_('Cubic kilometer, km^3'), Decimal('1E+18'), 0),
            (_('Milliliter, mL'), Decimal('1E+3'), 0),
            (_('Liter, L'), Decimal('1E+6'), 0),
            # Imperial and US customary systems
            (_('Cubic inch, in^3'), Decimal('16387.064'), 1),
            (_('Cubic foot, ft^3'), Decimal('28316846.592'), 1),
            (_('Cubic yard, yd^3'), Decimal('764554857.984'), 1),
            (_('Cubic mile, mi^3'), Decimal('4168181825440539600'), 1),
            (_('Acre - inch, ac⋅in'), Decimal('102790153129'), 1),
            (_('Acre - foot, ac⋅ft'), Decimal('1233481837548'), 1),
            (_('Acre - foot (US), ac⋅ft'), Decimal('1233489238468'), 1),
            (_('Ounce, oz'), Decimal('28413.0625'), 1),
            (_('Ounce (US), oz'), Decimal('29573.529562'), 1),
            (_('Gill, gi'), Decimal('142065.3125'), 1),
            (_('Gill (US), gi'), Decimal('118294.11825'), 1),
            (_('Pint, pt'), Decimal('568261.25'), 1),
            (_('Pint (US), pt'), Decimal('473176.473'), 1),
            (_('Quart, qt'), Decimal('1136522.5'), 1),
            (_('Quart (US), qt'), Decimal('946352.946'), 1),
            (_('Gallon, gal'), Decimal('4546090'), 1),
            (_('Gallon (US), gal'), Decimal('3785411.784'), 1),
            (_('Barrel, bbl'), Decimal('163659240'), 1),
            (_('Barrel (US), bbl'), Decimal('119240471.2'), 1),
            (_('Barrel (oil), bbl'), Decimal('158987294.93'), 1),
        )
    },

}


# ------------------------------------------------------------------------------


def conversion(quantity: str,
               index: int,
               value: Decimal | str,
               precision: int,
               quantize: int,
               scientific: int) -> list | None:

    _quantize = f'{0:.{quantize}f}'

    getcontext().prec = precision
    units = quantities[quantity]['units']
    result = []

    match quantity:

        case 'temperature':
            if type(value) is Decimal:
                temperature = find_temperature(units[index][1], value)
                for t in temperature:
                    try:
                        v = t.quantize(Decimal(_quantize))
                    except BaseException:
                        pass
                    v = v.normalize()
                    result.append(str(v))

        case 'numbers':
            return convert_numbers(units[index][1], value)

        case 'fuel':
            return convert_fuel(units[index][1], value, _quantize, scientific)

        case _:
            if type(value) is str:
                return None
            base_value = value * units[index][1]  # to the lowest value
            # unit conversion
            for u in units:
                v = base_value / u[1]
                result.append(value_processing(v, _quantize, scientific))

    return result if len(result) > 0 else None


# ------------------------------------------------------------------------------


def find_temperature(identifier: str, value: Decimal):

    KELVIN_OFFSET = Decimal('273.15')
    RANKINE_OFFSET = Decimal('459.67')
    FRACTION_9_5 = Decimal('9') / Decimal('5')
    FRACTION_5_9 = Decimal('5') / Decimal('9')
    FRACTION_4_5 = Decimal('4') / Decimal('5')
    FRACTION_5_4 = Decimal('5') / Decimal('4')

    match identifier:
        case 'celsius':
            celsius = value
            kelvin = celsius + KELVIN_OFFSET
            fahrenheit = celsius * FRACTION_9_5 + Decimal('32')
            rankine = kelvin * FRACTION_9_5
            reaumur = celsius * FRACTION_4_5

        case 'kelvin':
            kelvin = value
            celsius = kelvin - KELVIN_OFFSET
            fahrenheit = kelvin * FRACTION_9_5 - RANKINE_OFFSET
            rankine = kelvin * FRACTION_9_5
            reaumur = celsius * FRACTION_4_5

        case 'fahrenheit':
            fahrenheit = value
            celsius = (fahrenheit - Decimal('32')) * FRACTION_5_9
            kelvin = celsius + KELVIN_OFFSET
            rankine = fahrenheit + RANKINE_OFFSET
            reaumur = celsius * FRACTION_4_5

        case 'rankine':
            rankine = value
            kelvin = rankine * FRACTION_5_9
            celsius = kelvin - KELVIN_OFFSET
            fahrenheit = rankine - RANKINE_OFFSET
            reaumur = celsius * FRACTION_4_5

        case 'reaumur':
            reaumur = value
            celsius = reaumur * FRACTION_5_4
            kelvin = celsius + KELVIN_OFFSET
            fahrenheit = celsius * FRACTION_9_5 + Decimal('32')
            rankine = fahrenheit + RANKINE_OFFSET

        case _:
            print(f'Error: "{identifier}" unknown identifier')
            return []

    # checking for physically impossible values
    if kelvin < 0:
        kelvin = 0
    if rankine < 0:
        rankine = 0

    # order is important
    return [
        celsius,
        kelvin,
        fahrenheit,
        rankine,
        reaumur,
    ]


# ------------------------------------------------------------------------------


def convert_numbers(identifier: str, value: Decimal | str) -> list[str] | None:

    # important: all return values ​​must be strings

    if type(value) is Decimal:
        value_int = int(value.to_integral_value(rounding='ROUND_HALF_UP'))
        value_str = str(value_int)
    elif type(value) is str:
        value_str = value
        if identifier == 'hexadecimal':
            try:
                value_int = int(value_str, 16)
            except ValueError:
                return None
        else:
            return None

    match identifier:
        case 'decimal':
            result = [
                value_str,                   # decimal
                hex(value_int)[2:].upper(),  # hexadecimal
                oct(value_int)[2:],          # octal
                bin(value_int)[2:],          # binary
            ]
        case 'hexadecimal':
            result = [
                str(value_int),
                value_str,
                oct(value_int)[2:],
                bin(value_int)[2:],
            ]
        case 'octal':
            d = int(value_str, 8)
            result = [
                str(d),
                hex(d)[2:].upper(),
                value_str,
                bin(d)[2:],
            ]
        case 'binary':
            try:
                d = int(value_str, 2)
            except ValueError:
                return None
            result = [
                str(d),
                hex(d)[2:].upper(),
                oct(d)[2:],
                value_str,
            ]

    return result


def convert_fuel(identifier: str,
                 value: Decimal | str,
                 quantize: str,
                 scientific: int) -> list[str] | None:

    try:
        v = Decimal(str(value))
    except BaseException as err:
        print('Error, invalid value: ' + str(err))
        return None

    if v <= 0:
        return ['0', '0', '0', '0', '0']

    # coefficients
    MPG_US_TO_L100KM = Decimal('235.21458335647424250')
    MPG_UK_TO_L100KM = Decimal('282.48093626943037818')

    # base value
    try:
        match identifier:
            case 'L/100 km': base_value = v
            case 'km/L': base_value = Decimal('100') / v
            case 'm/L': base_value = Decimal('100000') / v
            case 'mpg(us)': base_value = MPG_US_TO_L100KM / v
            case 'mpg(uk)': base_value = MPG_UK_TO_L100KM / v
            case _:
                print('Error: unknown identifier')
                return None
    except BaseException as err:
        print('Error getting base value: ' + str(err))
        return None

    # conversion in strict order
    try:
        conversions = [
            ('m/L', Decimal('100000') / base_value),
            ('km/L', Decimal('100') / base_value),
            ('L/100 km', base_value),
            ('mpg(us)', MPG_US_TO_L100KM / base_value),
            ('mpg(uk)', MPG_UK_TO_L100KM / base_value),
        ]
        result = []
        for i in conversions:
            result.append(value_processing(i[1], quantize, scientific))
        return result
    except BaseException as err:
        print('Error during conversion: ' + str(err))
        return None


# ------------------------------------------------------------------------------


def value_processing(value: Decimal, quantize: str, scientific: int) -> str:
    try:
        value = value.quantize(Decimal(quantize))
    except BaseException:
        pass  # todo: error?
    value = value.normalize()

    exponent = value.as_tuple().exponent
    digits = len(value.as_tuple().digits)

    if isinstance(exponent, int) and exponent > 0:
        if digits + exponent < scientific:
            if value == value.to_integral_value():  # check
                value = Decimal(int(value))

    return str(value)
