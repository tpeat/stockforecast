# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class Model(Item):
    # define the fields for your item here like:
    DATE = Field()
    CLOSE = Field()
    VOLUME = Field()
    OPEN = Field()
    HIGH = Field()
    LOW = Field()
    
