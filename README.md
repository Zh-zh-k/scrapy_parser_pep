# Scrapy Parser PEP

Парсер документов PEP с сайта [peps.python.org](https://peps.python.org/), реализованный на фреймворке Scrapy.

Парсер собирает:
- номер PEP;
- название PEP;
- статус PEP.

Результаты сохраняются в два CSV-файла:
- `pep_<дата-время>.csv` — список всех PEP;
- `status_summary_<дата-время>.csv` — сводка по статусам и общее количество документов.

## Технологии

- Python
- Scrapy
- pytest

## Установка

Клонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone <URL_репозитория>
cd scrapy_parser_pep
```

Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate
```

Для Windows:

```bash
venv\Scripts\activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Запуск парсера

Из корневой директории проекта выполните:

```bash
scrapy crawl pep
```

После завершения работы парсера в директории `results/` будут созданы два CSV-файла:

- `pep_<дата-время>.csv`
- `status_summary_<дата-время>.csv`

## Запуск тестов

```bash
pytest
```

или:

```bash
python -m pytest
```

## Как работает проект

Паук `PepSpider` собирает ссылки на документы PEP и переходит на страницу каждого документа.

Для каждого PEP формируется объект `PepParseItem` со следующими полями:
- `number` — номер PEP;
- `name` — название PEP;
- `status` — статус PEP.

Основной CSV-файл со списком PEP формируется через механизм Scrapy Feeds.

Сводка по статусам создаётся в `PepParsePipeline`. Pipeline подсчитывает количество документов в каждом статусе и добавляет итоговую строку `Total` с общим количеством PEP.