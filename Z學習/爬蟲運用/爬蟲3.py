# #抓取網頁原始碼
# import urllib.request as req
# import ssl

# url = "https://www.dgpa.gov.tw/typh/daily/nds.html"
# ctx = ssl._create_unverified_context()  # 不驗證 SSL 憑證

# request = req.Request(url, headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# })

# with req.urlopen(request, context=ctx) as response:
#     data = response.read().decode("utf-8")

# print(data)

import urllib.request as req
url="https://www.ptt.cc/bbs/gossiping/index.html"
request=req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"})
with req.urlopen(request)as response:
    data=response.read().decode("utf-8")
# print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a !=None:
        print(title.a.string)