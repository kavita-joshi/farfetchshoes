import scrapy

from ..items import FarfetchItem #from items importing FarfetchItem class

class farfetch(scrapy.Spider): # inheriting class farfetch from scrapy.Spider

    name = 'farfetch' # name of the spider
    page_number = 2 # defining variable for storing the page_number

    # URL used for scraping
    # scraping all the products from the men shoes section
    start_urls = [
        "https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx",
        "https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=2&view=90&scale=282"

    ]

    def parse(self, response): #

        items = FarfetchItem() # making an instance of class from items file

        product = response.css("p._d85b45::text").extract() # extracting product name from farfetch website
        brand = response.css("h3._346238::text").extract()  # extracting the brand name
        price = response.css("div._6356bb span::text").extract()  # extracting the price of the product
        product_link = response.css("a._5ce6f6::attr(href)").extract() # extracting the product_link of the product
        image_link = response.css("img::attr(src)").extract() # extracting the image_link of the product


        # storing product details into items
        items["product"] = product
        items["brand"] = brand
        items["price"] = price
        items["product_link"] = product_link
        items["image_link"] = image_link

        for items in zip(product, brand, price, product_link, image_link):
            scraped_info = {
                "product" : items[0],
                "brand" : items[1],
                "price" : items[2],
                "product_link" : items[3],
                "image_link" : items[4]
            }

            yield scraped_info # used as a return statement in scrapy


        # pagination method to scrape all the products from every pages

        next_page = "https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=" + str(farfetch.page_number) + "&view=90&scale=283"
        if farfetch.page_number <= 171:
            farfetch.page_number += 1
            yield response.follow(next_page, callback = self.parse)




