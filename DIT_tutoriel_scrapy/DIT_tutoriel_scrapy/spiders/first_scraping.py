import scrapy

class fnac_spyder(scrapy.Spider):
	name= 'fnac_scraping'
	start_urls=['https://www.jumia.ci/']

	def parse(self, response) :
		#parse fonction 
		dic_article={
		'article':response.css('div.name::text').getall(),
		'article_price':response.css('div.prc::text').getall()
		}
		
		yield dic_article
		




