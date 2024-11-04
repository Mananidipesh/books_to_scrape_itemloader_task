import scrapy
import re
from books.items import BooksItem
from scrapy.loader import ItemLoader

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # titles = response.css('article.product_pod h3 a::attr(title)').getall()
        # for title in titles:
        #     print('title:', title)
        #     print('ratings',)
        books = response.css('article.product_pod')
        for book in books:
            book_item = ItemLoader(item=BooksItem() , selector=book)
            book_item.add_css('title' ,'article.product_pod h3 a')
            # book_item.add_css('rating' ,'p.star-rating::attr(class)')
            rating = book.css('p.star-rating::attr(class)').re(r'star-rating (\w+)')
            book_item.add_value('rating', rating[0])
            book_item.add_css('price', 'article.product_pod p.price_color')

            yield book_item.load_item()

            # title = book.css('article.product_pod h3 a::attr(title)').get()
            # ratings = book.css('article.product_pod p.star-rating::attr(class)').re(r'star-rating (\w+)')[0]
            # price = book.css('article.product_pod p.price_color::text').get()
            # print()
            # print('title1:' , title)
            # print()
            # print('rating:', ratings)
            # print()
            # print('price:',price)
            
            # book_details = {
            #     "title" : title ,
            #     "ratings" : ratings , 
            #     "price" : price
            # }
            # yield book_details
