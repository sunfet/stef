import scrapy


class Git2Spider(scrapy.Spider):
    name = "git2"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        #从登陆页面获取post
        token = response.xpath('//*[@id="login_field"]').extract_first()
        post_data = {
            'commit':'Sign in',
            'authenticity_token':token, 
            'login':'sunfet',
            'password':'1234567890',
            'webauthn-support':'supported'

        }


        #发送请求
        yield scrapy.FormRequest(
            url='https://github.com/session',
            formdata=post_data,
            callback=self.after_login
            )
    def after_login(self, response):
        #登陆成功后，获取个人主页
        yield scrapy.Request(
            'https://github.com/sunfet',callback=self.check_login
        )
    def check_login(self, response):
        #检查登陆成功
        print(response.xpath('/html/head/style[1]/text()').extract_first())