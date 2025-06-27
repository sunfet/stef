import requests
from lxml import etree

class Tieba(object):

    def __init__(self,tieba_name):
        self.url = 'https://tieba.baidu.com/f?kw={}'.format(tieba_name)
        print(self.url)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
        }

    def get_data(self,url):
        print(f"正在请求 URL: {url}") # 添加这行，打印正在请求的URL
        try:
            response = requests.get(url,headers=self.headers, timeout=30)
            with open('temp.html','wb',encoding='utf-8') as f:
                f.write(response.content)
            print("请求成功") # 添加这行，请求成功时打印
            return response.content
        except Exception as e:
            print(f"请求发生错误: {e}") # 添加这行，捕获异常时打印错误信息
            return None # 或者返回一个标志表示请求失败
    
    def parse_data(self,data):
        #如获取的对象被引用,则使用替换
        #data = data.encode().replace('<!--','').replace('-->','')
        #创建element对象
        html = etree.HTML(data)

        el_list = html.xpath('//*[@id="thread_list"]/li[5]/div/div[2]/div[1]/div[1]/a')
        #print(len(el_list)) #验证能读取到几个
        data_list = []

        for el in el_list:
            temp = {}
            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + el.xpath('./@href')[0]
            data_list.append(temp)

            #获取下一页,找翻页URL的时候尽量不要用索引
            try:
                next_url ='https:' + html.xpath('//a[@class="next pagination-item"]/@href')[0]
                #next_url = 'https:' + html.xpth('//a[contains(text(),'下一页>')]/@href') [0] 
            except:
                next_url = None


        return data_list,next_url
    
    #保存文件
    def save_data(self,data_list):
        for data in data_list:
            print(data)

    def run(self):
        print("进入 run 方法") # 添加这行来确认是否进入 run 方法
        next_url = self.url
        while True:
            data = self.get_data(next_url)
            data_list,next_url = self.parse_data(data)
            self.save_data(data_list)
            if next_url is None:
                break
        #先来思路
        #url
        #headers
        #发送请求      
        #获取响应
        #判断是否终结(是否有下一页)
        

if __name__ == "__main__":
    tieba = Tieba('孙笑川')
    tieba.run()
