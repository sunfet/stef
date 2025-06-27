import requests

url = 'https://xy58x144x119x78xy2408y8763y0yf02y2yy78xy.mcdn.bilivideo.cn:4483/upgcxcode/65/08/29646130865/29646130865-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1746539201&tag=&nbs=1&platform=pc&gen=playurlv3&og=cos&oi=1972307642&trid=0000df340d55393e4fc38046e584beee702u&os=mcdn&mid=19705865&uipk=5&upsig=54a95433a40bbc951ee3c380906b1395&uparams=e,deadline,tag,nbs,platform,gen,og,oi,trid,os,mid,uipk&mcdnid=50026589&bvc=vod&nettype=0&bw=84295&f=u_0_0&agrr=0&buvid=3656C052-7B3A-74D1-6629-88B92A4476FD81487infoc&build=0&dl=0&orderid=0,3'


'''
    1. 状态码 200 成功 403 拒绝 404 失败 405  方法错误 500 服务器错误 412 请求错误
    2. 响应的内容


B站反爬第一步:
    1. 找到视频的网址
    2. 打开开发者工具
    3. 刷新页面
    4. 找到视频的网址
    5. 复制视频的网址
    6. 粘贴到代码中
    7. 运行代码
    8. 保存视频
但是网站需要做一定的安全检查
user-agent: 浏览器的标识,你用的什么浏览器
referer: 来源,引荐页,你是从哪个页面找到我的
cookie: 登录信息
'''
#伪装浏览器
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
'referer':'https://www.bilibili.com/video/BV1f2L6zTEQ9/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=55323dcd0a891ca0b4e87896e1a8bd00'}
#提交伪装信息
res = requests.get(url,headers=headers)
print(res.status_code)
open('1号女嘉宾.MP4','wb').write(res.content)

#下载的视频只有部分,没有声音,找到音频的网址
url1 ='https://xy36x156x206x140xy.mcdn.bilivideo.cn:8082/v1/resource/29646130865-1-30232.m4s?agrr=0&build=0&buvid=3656C052-7B3A-74D1-6629-88B92A4476FD81487infoc&bvc=vod&bw=85859&deadline=1746539201&dl=0&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv3&mcdnid=50026589&mid=19705865&nbs=1&nettype=0&og=hw&oi=1972307642&orderid=0%2C3&os=mcdn&platform=pc&sign=1cd45a&tag=&traceid=trNCMmLFvxLOAE_0_e_N&uipk=5&uparams=e%2Ctag%2Cplatform%2Coi%2Cgen%2Cos%2Cog%2Cdeadline%2Cuipk%2Ctrid%2Cmid%2Cnbs&upsig=c1c57f0191da5238b44444b595ca879f'

headers1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
'referer':'https://www.bilibili.com/video/BV1f2L6zTEQ9/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=55323dcd0a891ca0b4e87896e1a8bd00'}

res1 = requests.get(url1,headers=headers1)
print(res1.status_code)
open('1号女嘉宾.MP3','wb').write(res1.content)

#合并视频和音频
