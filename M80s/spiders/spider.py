import scrapy

from M80s.items import JobItem


class DmozSpider(scrapy.spiders.Spider):
    name="51job"
    allowed_domains = ['jobs.51job.com', 'search.51job.com']
    start_urls = [
        'https://search.51job.com/list/000000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25AE%259E%25E4%25B9%25A0%25E7%2594%259F,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    def parse(self,response):
        nextpageurl = response.xpath("//*[@id=\"rtNext\"]/@href").extract()[0]
        print(nextpageurl)
        for i in response.xpath("//*[@id=\"resultList\"]//div[@class='el']"):
                jobitem = JobItem()
                jobitem['job_name']=i.xpath("p/span/a[@target='_blank']//@title").extract()
                jobitem['company_name']=i.xpath("span[@class='t2']//@title").extract()
                jobitem['address']=i.xpath("span[@class='t3']//text()").extract()
                jobitem['salary']=i.xpath("span[@class='t4']//text()").extract()
                jobitem['time']=i.xpath("span[@class='t5']//text()").extract()
                yield jobitem
        yield scrapy.Request(nextpageurl,callback=self.parse)
        #get detail url for every job
    #     yield scrapy.Request(detailurl,callback=self.getDetail)
    # def getDetail(self,response):
    #     item=JobItem()
    #     #get filed
    #     return item