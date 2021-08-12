.PHONY: po mo

po:
    # 1) - create files
	xgettext -L python --output=messages.pot main.py app_interface.kv
	xgettext -L python --output=po\en.po main.py app_interface.kv
	xgettext -L python --output=po\ru.po main.py app_interface.kv
	# 2) in files set charset to utf-8
	# 3) update po/en.po and po/ru.po content
	msgmerge --update --no-fuzzy-matching --backup=off po/en.po messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off po/ru.po messages.pot
	# 4) add translations to po/ru.po to msgstr

mo:
	#for windows cmd:
	mkdir po
	xgettext -L python --output=messages.pot main.py app_interface.kv
	mkdir data\locales\en\LC_MESSAGES
	mkdir data\locales\ru\LC_MESSAGES
	#for linux shell:
	mkdir po
	mkdir -p data/locales/en/LC_MESSAGES
	mkdir -p data/locales/ru/LC_MESSAGES
    # 5) update translations
	msgfmt -c -o data/locales/en/LC_MESSAGES/langapp.mo po/en.po
	msgfmt -c -o data/locales/ru/LC_MESSAGES/langapp.mo po/ru.po


# to update:
    xgettext -L python --output=messages.pot main.py app_interface.kv
    msgmerge --update --no-fuzzy-matching --backup=off po/en.po messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off po/ru.po messages.pot
    msgfmt -c -o data/locales/en/LC_MESSAGES/langapp.mo po/en.po
	msgfmt -c -o data/locales/ru/LC_MESSAGES/langapp.mo po/ru.po
