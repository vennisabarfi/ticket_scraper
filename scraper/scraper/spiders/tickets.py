from pathlib import Path

import scrapy
import chompjs
import json 
import base64
# check this out:
# https://stackoverflow.com/questions/68958514/pip-install-chompjs-in-scrapy-virtual-environment-under-anaconda-showing-errors


class TicketSpider(scrapy.Spider):
    name = "tickets"
    
    start_urls = [
        # "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
        "https://www.ticketmaster.com/search?q=beyonce",
    ]
        
    
    def parse(self, response):
        # page = response.url.split("/")[-1]
        # filename = f"quotes-{page}.html"
        filename = "test.txt"
        # work on this
        # class="sc-1g6xjqc-0 jKmtvh"
        scripts = response.css('div.sc-1g6xjqc-0jKmtvh').getall()
        
        javascript = response.css("script::text").get()
        data = chompjs.parse_js_object(javascript)
        data_convert = json.dumps(data, indent=2)
        print(data_convert)
        Path(filename).write_bytes((data_convert))
        
        self.log(f"Saved file {filename}")
        
                # extend script to add log file that saves info for every crawl
        
    # def parse(self, response):
    #     # page = response.url.split("/")[-1]
    #     # filename = f"quotes-{page}.html"
    #     filename = "beyonce.json"
    #     # work on this
    #     # class="sc-1g6xjqc-0 jKmtvh"
    #     scripts = response.css('div.sc-5b932363-0 j0DkC').getall()
    #     main_content = response.css('main#main-content')

    # # Extract all items under the <main> tag
    #     items = main_content.css('*').getall()  # * selects all elements under <main>
    #     path2 = "tests.html"

    #     # for item in items:
    #     #     print(item)
    #     items_str = "\n".join(items)
    #     scripts_str = "\n".join(scripts)
        
    #     print(scripts_str)
        
    #     Path(path2).write_text(items_str)
    #     # Path(filename).write_bytes(response.body)
    #     self.log(f"Saved file {filename}")
    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             "text": quote.css("span.text::text").get(),
    #             "author": quote.css("small.author::text").get(),
    #             "tags": quote.css("div.tags a.tag::text").getall(),
    #         }