# small-ozon-parser
# Какие страницы загружать?
✅ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/reviews

✅ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/reviews/?sort=created_at_desc – Сортировка комментариев будет по новизне, что 
предпочтительнее для задания (ИМХО)

✅ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/reviews/?sort=created_at_desc&page=2 – То же самое, но открывается вторая страница с отзывами

❌ https://www.ozon.ru/product/smartfon-apple-iphone-12-64gb-191318834/ – Нужно прогружать отзывы

# Как нажать на все ссылки "Читать далее...":
Некоторые комментарии слишком длинные и озон их сворачивает. Чтобы развернуть комментарии на определённой странице, нужно выполнить следующий скрипт в инструментах разработчика:

```document.querySelectorAll('[data-review-id] > div:nth-child(2) > div:nth-child(2) span').forEach(element => element.click())```
<ul><li>Ctrl+C</li>
  <li>Нажать F12 в браузере</li>
  <li>Перейти в консоль</li>
  <li>Ctrl+V</li>
  <li>Enter</li></ul>


# Куда закидывать .html файлы веб-страниц?
В папку /html. Программа читает только файлы с разрешением .html

# Куда записывается вывод?
В файл result.txt
