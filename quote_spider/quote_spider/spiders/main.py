from typing import Any

import scrapy

import json

from itemadapter import ItemAdapter
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from scrapy.item import Item, Field

class QuoteItem(Item):
    tags = Field()
    author = Field()
    quote = Field()

class AuthorItem(Item):
    fullname = Field()
    born_location = Field()
    born_date = Field()
    description = Field()

class QuotesPipline():
    quotes = []
    authors = []

    def process_item(self, item, spiser):
        adapter = ItemAdapter(item)
        if "fullname" in adapter.keys():
            self.authors.append({
                "fullname": adapter["fullname"],
                "born_date": adapter["born_date"],
                "born_location": adapter["born_location"],
                "description": adapter["description"]
            })
        if "quote" in adapter.keys():
            self.quotes.append({
                "tags": adapter["tags"],
                "author": adapter["author"],
                "quote": adapter["quote"]
            })
        return
    def close_spider(self, spider):
        with open("qoutes.json", "w", encoding="utf-8") as fh:
            json.dump(self.quotes, fh, ensure_ascii=False)
        with open("authors.json", "w", encoding="utf-8") as fh2:
            json.dump(self.authors, fh2, ensure_ascii=False)
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {"ITEM_PIPELINES": {QuotesPipline: 300}}

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            tags = quote.xpath("div[@class='tags']/a/text()").extract()
            author = quote.xpath("span/small/text()").get().strip()
            q = quote.xpath("span[@class='text']/text()").get().strip()
            yield QuoteItem(tags=tags, author=author, quote=q)
            yield response.follow(url=self.start_urls[0] + quote.xpath("span/a/@href").get(), callback=self.parse_author)
        next_link = quote.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
    def parse_author(self, response, *args):
        author = response.xpath("/html//div[@class='author-details']")
        fullname = author.xpath("h3[@class='author-title']/text()").get().strip()
        born_date = author.xpath("p/span[@class='author-born-date']/text()").get().strip()
        born_location = author.xpath("p/span[@class='author-born-location']/text()").get().strip()
        description = author.xpath("div[@class='author-description']/text()").get().strip()
        yield AuthorItem(fullname=fullname, born_date=born_date, born_location=born_location, description=description)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()