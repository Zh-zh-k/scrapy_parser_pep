import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from pep_parse.settings import RESULTS_DIR

BASE_DIR = Path(__file__).resolve().parent.parent


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = Counter()

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = (
            self.results_dir / f'status_summary_{timestamp}.csv'
        )

        total = sum(self.statuses.values())

        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            rows = [
                ('Статус', 'Количество'),
                *self.statuses.items(),
                ('Total', total),
            ]

            writer.writerows(rows)
