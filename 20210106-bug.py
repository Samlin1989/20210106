import requests
from bs4 import BeautifulSoup
"""
爬PTT電影版,並可指定爬幾頁
"""
#
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }


url = "https://www.ptt.cc/bbs/movie/index.html"

html = requests.get(url, headers = headers)
result = BeautifulSoup(html.content, "html.parser") #使用bs內建的html解析器(parser)來解析html代碼

titles = result.find_all('div', class_ = "title", limit = 20)#從解析的內容,濾出所有<div class= "title">...</div>  (class_:因為class已經是拍審預設字,故加底線分辨)

for i, item in enumerate(titles): #輪詢(enumeratr) 所有的結果
    if item.find("a"): #找出含有a標籤的內容
        a = item.find("a") #(將上一行找出的超連結)指定給a
        print("#{}標題: {} \n 連結:https://www.ptt.cc{}".format(i+1, a.string, a.get('href')))# a.string=擷取文字 'href'=超連結


#print(res.text)








"""
# 儲存網頁內容
fn = 'out.txt'
with open(fn, 'wb') as file_Obj:                        # 以二進位儲存
    for diskStorage in res.iter_content(10240): # Response物件處理
        size = file_Obj.write(diskStorage)           # Response物件寫入
        print(size)                                  # 列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)
"""