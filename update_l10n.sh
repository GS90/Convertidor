#!/bin/bash

xgettext -o po/convertidor.pot --files-from=po/POTFILES.in

msgmerge --update --backup='off' po/ru.po po/convertidor.pot

exit 0
