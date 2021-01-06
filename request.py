import requests

#url = "https://www.google.com"
#htmlfile = requests.get(url)
#print(htmlfile)

###
url = 'http://www.gzaxxc.com/file_not_existed'  # 錯誤的網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                        # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
###

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://www.ntu.edu.tw/'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()

print("偽裝瀏覽器擷取網路資料成功")
print(htmlfile.text)