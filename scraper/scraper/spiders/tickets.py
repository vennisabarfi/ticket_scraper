from pathlib import Path

import scrapy


class TicketSpider(scrapy.Spider):
    name = "tickets"
    
    start_urls = [
        # "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
        "https://www.ticketmaster.com/search?q=kendrick+lamar",
    ]
        
    
    def parse(self, response):
        # page = response.url.split("/")[-1]
        # filename = f"quotes-{page}.html"
        filename = "kendrick.html"
        scripts = response.css('script :: text').getall()
        
        
        Path(filename).write_bytes(scripts)
        self.log(f"Saved file {filename}")
        
                # extend script to add log file that saves info for every crawl
        
    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             "text": quote.css("span.text::text").get(),
    #             "author": quote.css("small.author::text").get(),
    #             "tags": quote.css("div.tags a.tag::text").getall(),
    #         }