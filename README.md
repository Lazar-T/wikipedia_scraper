 wikipedia_scraper
==================

###About

Spider built with [Scrapy](http://scrapy.org/). Scrapes [random articles](https://en.wikipedia.org/wiki/Special:Random) from [en.wikipedia.org](https://en.wikipedia.org/wiki/Main_Page) and gets data such as page url and title.

###Screenshot

![Screenshot](http://i.imgur.com/QWYx2Ad.png)

### Installation and Running
```
git https://github.com/Lazar-T/wikipedia_scraper
cd wikipedia_scraper
scrapy crawl wikipedia
```
####To get csv output
```
scrapy crawl wikipedia -o <filename>.csv
```
