# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrustpilothuelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    review_title = scrapy.Field()
    review_content = scrapy.Field()
    rating = scrapy.Field()
    review_date = scrapy.Field()


