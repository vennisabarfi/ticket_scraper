from pathlib import Path

import scrapy


class TicketSpider(scrapy.Spider):
    name = "tickets"
    
    start_urls = [
        # "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
        "https://www.ticketmaster.com/search?q=beyonce",
    ]
        
    
    # def parse(self, response):
    #     # page = response.url.split("/")[-1]
    #     # filename = f"quotes-{page}.html"
    #     filename = "kendrick.html"
    #     # work on this
    #     # class="sc-1g6xjqc-0 jKmtvh"
    #     scripts = response.css('div.sc-1g6xjqc-0 jKmtvh').getall()
        
        
    #     Path(filename).write_bytes(scripts)
    #     self.log(f"Saved file {filename}")
        
                # extend script to add log file that saves info for every crawl
        
    def parse(self, response):
        # page = response.url.split("/")[-1]
        # filename = f"quotes-{page}.html"
        filename = "beyonce.json"
        # work on this
        # class="sc-1g6xjqc-0 jKmtvh"
        scripts = response.css('div.sc-1g6xjqc-0 jKmtvh').getall()
        main_content = response.css('main#main-content')

    # Extract all items under the <main> tag
        items = main_content.css('*').getall()  # * selects all elements under <main>
        path2 = "test.html"
    
        Path(path2).write_bytes(main_content)
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             "text": quote.css("span.text::text").get(),
    #             "author": quote.css("small.author::text").get(),
    #             "tags": quote.css("div.tags a.tag::text").getall(),
    #         }