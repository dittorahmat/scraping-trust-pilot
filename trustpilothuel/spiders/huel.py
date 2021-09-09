import scrapy
#from trustpilothuel.items import TrustpilothuelItem


class HuelSpider(scrapy.Spider):
    name = 'huel'
    #allowed_domains = ['trustpilot.com']
    start_urls = ['https://uk.trustpilot.com/review/huel.com']

    def parse(self, response):
        for review in response.xpath('//article[@class="review"]'):
            yield {
                'name' : review.css('div.consumer-information__name ::text').get().strip(),
                'location' : review.css('div.consumer-information__location > span ::text').get(),
                'review_title' : review.css('div.review-content__body > h2 > a ::text').get().strip(),
                'review_content' : review.css('div.review-content__body > p ::text').get(default='').strip(),
                'rating' : review.css('div.star-rating.star-rating--medium > img ::attr(alt)').get(),
                'review_date' : review.css('span > time ::attr(datetime)').get(),
            }





