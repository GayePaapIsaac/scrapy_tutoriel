import scrapy

class fnac_spyder(scrapy.Spider):
	name= 'fnac_scraping'
	start_urls=['https://www.jumia.ci/']

	def parse(self, response) :
		dic_article={}
		#extration des liens de la page fnac
		#article=response.css('span.categoryMosaic-title::text').get()
		#likn_article=response.css('a::attr(href)').extract()
		#article_name=response.css('div.name::text').getall()
		#article_price=response.css('div.prc::text').getall()

		dic_article={
		'article':response.css('div.name::text').getall()+str('\n').strip(""),
		'article_price':response.css('div.prc::text').getall()
		}
		
		return dic_article[0]
		#yield dic_article# {
		#	'article':article_name,
		#	'article_price':article_price,
		#	#'likn_article':likn_article,
		#}



		'''
		for link in response.css("div.crs row _no-g -fw-nw _6cl-4cm -pvxs"):
			yield {
			'article': link.css('div.name::text').get(),
			'price': link.css('div.prc::text').get(),
			#'tags': link.css('div.tags a.tag::text').getall(),
			}
		'''


		#links=response.css('a::attr(href)').extract()
		#browse and extract for all links

		#for link in links :
		#	yield scrapy.Request(link, callback=)


