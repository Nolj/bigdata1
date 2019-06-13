import requests
import json

# 拿取腾讯招聘的url url存在json了，所以到hesder里拿取url                                                                                                                                       
url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1560412509418&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

response = requests.get(url)
# 把后台传过来的数据转成字典
dict1 =json.loads(response.text)

# 建立一个空的列表，把我们要的数据放到里面，从而得到他的长度
item = []
for i in dict1["Data"]["Posts"]:
    item.append(i)

# 循环输出工作岗位

for i in range(len(item)):
    print(dict1["Data"]["Posts"][i]["RecruitPostName"])
    print(dict1["Data"]["Posts"][i]["CountryName"])
    print(dict1["Data"]["Posts"][i]["LocationName"])
