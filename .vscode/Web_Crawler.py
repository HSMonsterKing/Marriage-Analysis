from multiprocessing.pool import ThreadPool
import requests as req
from time import time

def url_response(data):
    path, url = data
    r = req.get(url)
    
    with open(path + ".json", 'wb') as f:
        f.write(r.content)

urls = [
("2018_01_10140-01-02-2_臺中市 結婚人數按性別、年齡、原屬國籍(地區)及婚前婚姻狀況分暨其結婚年齡之第一四分位數、中位數、第三四分位數與平均數(按發生日期)", "https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=28e43506-087a-4912-8d9b-aba999757f1c")
]

start = time()

pool = ThreadPool(5)

for _ in pool.imap_unordered(url_response, urls):
    pass

pool.close()
pool.join()

print("完成時間:", time() - start)