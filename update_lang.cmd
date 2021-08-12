xgettext -L python --output=messages.pot main.py app_interface.kv
msgmerge --update --no-fuzzy-matching --backup=off po/en.po messages.pot
msgmerge --update --no-fuzzy-matching --backup=off po/ru.po messages.pot
msgfmt -c -o data/locales/en/LC_MESSAGES/langapp.mo po/en.po
msgfmt -c -o data/locales/ru/LC_MESSAGES/langapp.mo po/ru.po