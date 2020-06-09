import scrapy 


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape"
    start_urls = [
        'https://www.coursera.org/courses?',
    ]

    def parse(self, response):
        for class_name in response.css('li.ais-InfiniteHits-item'):
            yield{
                'classname': class_name.css('div.card-info.vertical-box h2.color-primary-text.card-title.headline-1-text::text').get(),
                'partnet_name':class_name.css('span.partner-name::text').get(),
                'rating':class_name.css('span.ratings-text::text').get(),
                'difficulty': class_name.css('span.difficulty::text').get(),
                'enrollment-number':class_name.css('span.enrollment-number::text').get()

            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
           yield response.follow(next_page, callback=self.parse)