# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FarfetchItem(scrapy.Item):
    product = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    product_link = scrapy.Field()
    image_link = scrapy.Field()


