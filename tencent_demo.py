import requests
import json

def get_response(page):
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1560233347472&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn'%(str(page))
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    return response.content.decode('utf-8')

def parse_content(page):
    content = get_response(page)
    content = json.loads(content,encoding='utf-8')
    for i in content['Data']['Posts']:
        print(i)

if __name__ == "__main__":
    page = int(input('请输入要爬取的页码：'))
    for i in range(page):
        print('-----爬取第%d页-----'%(i+1))
        parse_content(i+1)