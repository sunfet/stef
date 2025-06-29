import scrapy


class Git1Spider(scrapy.Spider):
    name = "git1"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/sunfet"]

    def start_requests(self):
        url = self.start_urls[0]
        temp = '_octo=GH1.1.2091629167.1747576874; _device_id=084e2e646e63e1632ebe4a7084955f18; saved_user_sessions=38278973%3AGZ3h681BP1mBsbiDGszN36tRrqt5UKXPchsYWh_CoQ9vBrfW; user_session=GZ3h681BP1mBsbiDGszN36tRrqt5UKXPchsYWh_CoQ9vBrfW; __Host-user_session_same_site=GZ3h681BP1mBsbiDGszN36tRrqt5UKXPchsYWh_CoQ9vBrfW; logged_in=yes; dotcom_user=sunfet; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=dark; tz=Asia%2FShanghai; _gh_sess=zeosOP%2BGlyEK07LknAx%2FEhmCHpTf0tTTqxtgu5Qp%2BepFcMTZCUg%2Bpldo7WoIU5WUeEVxyVZupXOVLAseJ6W%2F2QbXfZh3MciWxiadwUzfkCCnAPKgaQKH2RL%2FuxwWawtk%2FB6rkzpuobpWN7hJQPZRjcke3lHbu23wYL8CnkUU%2BpIglUnHPrOmkdvmDFG%2FN0SlfEl%2FWF2EODLDVaopdO1ADbYiyrr2VBlWmSptvC27SLWUH6cYfQBU6aWuIquN7%2B5D%2FXE87GdoSfyjKVss%2FBKHDMiAi46SD3Q6GXEIAo3QIedWzlzUP0bJ%2FnwQb9W%2BmnMJY5ftQbSt2OG2swPKCLCQes%2FCcAm7QRgCeIgTGVvzkUU%2BKcLXSPf%2FMRQlxxmA3oMM--I383Lk3ZMbOyGTjp--gPTHyYiJxH2iQmz1BnwEHA%3D%3D'
        cookies = {data.split('=')[0]:data.split('=')[-1]for data in temp.split('; ')}
        yield scrapy.Request(
            url=url, 
            cookies=cookies, 
            callback=self.parse
            )

    def parse(self, response):
        print(response.xpath('/html/head/style[1]/text()').extract_first())
