# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose , TakeFirst
from w3lib.html import remove_tags
import re

def rating_to_number(rating):
    if rating == 'One':
        return 1
    elif rating == 'Two':
        return 2
    elif rating == 'Three':
        return 3
    elif rating == 'Four':
        return 4
    elif rating == 'Five':
        return 5
    else:
        return 0
    
def convert_price(price):
    numeric_price = re.sub(r'[^\d.]', '', price)
    new_price = float(numeric_price)
    return new_price


class BooksItem(scrapy.Item):
    title = scrapy.Field(input_processor = MapCompose(remove_tags) ,output_processor = TakeFirst())
    rating = scrapy.Field(input_processor = MapCompose(remove_tags,rating_to_number),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags, convert_price),output_processor = TakeFirst())

    # define the fields for your item here like:
    # name = scrapy.Field()
    
