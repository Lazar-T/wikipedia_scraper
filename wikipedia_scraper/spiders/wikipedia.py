# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"  # Name of our spider

    # Only allow links from en.wikipedia.com
    allowed_domains = ['en.wikipedia.com']

    # Our random article url
    seed = 'https://en.wikipedia.org/wiki/Special:Random'

    # Create a list comprehension in start_urls
    # that will get sent to parse function.
    start_urls = [seed for page in range(1000)]

    def parse(self, response):
        # Scraping title from the random article page
        title = response.xpath('//h1/text()').extract_first()

        # Put two of these items into a dictionary
        items = {
            'Title': title,
            'Page Url': response.url}

        # If we don't call yield, items won't be written in a csv file.
        yield items
