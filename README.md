# small-ozon-parser
# Как запустить?
У вас должен быть установлен питон и настроены переменные среды. В оболочке (cmd.exe) в папке small-ozon-parser печатаем:

```pip install -r requirements.txt``` – Установка зависимостей


```python main.py``` – Запуск проги

У меня олдовая версия питона и я не проверил файл requirements.txt, так что, если не сработало, то вбивайте:

```pip install beautifulsoup4```
# Какие страницы загружать?
К сожалению, перейти по этим ссылкам и получить отзывы у меня не получается. Чтобы скачать нужную страницу нужно с главной страницы товара нажать по надписи "отзывы и вопосы о товаре". Можете найти через Ctrl+F.

✅ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/reviews

✅ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/reviews/?sort=created_at_desc – Сортировка комментариев будет по новизне, что 
предпочтительнее для задания (ИМХО)

✅ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/reviews/?sort=created_at_desc&page=2 – То же самое, но открывается вторая страница с отзывами

❌ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/ – Нужно прогружать отзывы

# Как нажать на все ссылки "Читать полностью":
Перед скачиванием веб-страниц лучше развернуть комментарии. Чтобы развернуть комментарии на странице, нужно выполнить следующий скрипт в инструментах разработчика:

```document.querySelectorAll('[data-review-id] > div:nth-child(2) > div:nth-child(2) span').forEach(element => element.click())```

Последовательность действий:
<ul><li>Ctrl+C</li>
  <li>Нажать F12 в браузере</li>
  <li>Перейти в консоль</li>
  <li>Ctrl+V</li>
  <li>Enter</li></ul>


# Куда закидывать файлы веб-страниц?
В папку /html. Программа читает только файлы с разрешением .html

# Куда записывается вывод?
В файл result.txt

# Что-то не работает?
пишите в Issues
