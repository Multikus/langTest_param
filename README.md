# Автотест для проверки выбора языка

**ОБРАЩАЮ ВНИМАНИЕ**

1. Если запустить без параметров в виде pytest -v test_items.py - тест будет провален т.к по умолчанию стоит язык ru ошибка выпадет в assert
2. Также поу молчанию настройка стоит на браузер FireFox

Для запуска можно использовать 

pytest -v --language=es test_items.py - тест будет пройден в браузере FireFox
pytest -v --language=fr test_items.py - тест будет пройден в браузере FireFox, тест не провалится т.к. я добавил в assert логическое или
pytest -v --browser_name=chrome --language=es test_items.py - тест будет пройден в браузере Chrome
pytest -v --browser_name=chrome --language=fr test_items.py - тест будет пройден в браузере Chrome, тест не провалится т.к. я добавил в assert логическое или


