import os
from pathlib import Path
from bs4 import BeautifulSoup

result = []
html = ''
for path in os.listdir(r"html"):
    with open(file=f"html\\{path}", encoding='utf-8', mode='r') as f:
        if Path(path).suffix == 'html':
            html = '\n'.join(f.readlines())

soup = BeautifulSoup(html, 'html.parser')

# развернуть комментарии (нажать на все ссылки "Читать далее..."):
# document.querySelectorAll('[data-review-id] > div:nth-child(2) > div:nth-child(2) span').forEach(element => element.click())

for soup in soup.select('[data-review-id] > div:nth-child(2) > div:nth-child(2) span'):
    soup: BeautifulSoup

    if 'Комментарий' in soup.parent.parent.get_text():
        string = soup.get_text().replace(' ', '')
        string = string.replace('\n', ' ')

        result.append(f"){string}\n")

with open(file='result.txt', encoding='utf-8', mode='w') as f:
    f.writelines(result)
