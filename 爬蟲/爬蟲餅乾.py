#抓取網頁原始碼
import urllib.request as req
def getData(url):
    request=req.Request(url,headers={
    "Cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"})

    with req.urlopen(request)as response:
        data=response.read().decode("utf-8")
    # print(data)
    #解析   
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)
    #上一頁
    nextLink=root.find("a",string="‹ 上頁")
    return(nextLink["href"])
#抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/gossiping/index.html"
pageURL="https://www.ptt.cc"+getData(pageURL)  
count=0
print(pageURL)
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)   
    count+=1
    print(pageURL)
