import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = Counter()

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = results_dir / f'status_summary_{timestamp}.csv'

        total = sum(self.statuses.values())

        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])

            for status, count in self.statuses.items():
                writer.writerow([status, count])

            writer.writerow(['Total', total])
