import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        if response.url == 'https://peps.python.org/':
            yield response.follow('/numerical/', callback=self.parse)
            return

        pep_links = response.css('a[href*="/pep-"]::attr(href)').getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1').xpath('string(.)').getall()[1].strip()

        number = response.url.rstrip('/').split('pep-')[-1]
        number = str(int(number))

        status = response.xpath(
            '//dt[normalize-space()="Status:"]'
            '/following-sibling::dd[1]//text()'
        ).get().strip()

        yield PepParseItem(
            number=number,
            name=title,
            status=status,
        )
