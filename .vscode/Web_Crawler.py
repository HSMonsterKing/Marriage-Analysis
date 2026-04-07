from multiprocessing.pool import ThreadPool
import requests as req
from time import time

def url_response(data):
    path, url = data
    r = req.get(url)
    
    with open(path + ".json", 'wb') as f:
        f.write(r.content)

urls = [
("2018_01_10140-01-02-2_臺中市 結婚人數按性別、年齡、原屬國籍(地區)及婚前婚姻狀況分暨其結婚年齡之第一四分位數、中位數、第三四分位數與平均數(按發生日期).JSON", "https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=28e43506-087a-4912-8d9b-aba999757f1c")
,("2018_01_10140-01-03-2_臺中市 結婚人數按性別、單一年齡、五歲年齡及初婚、再婚分 (按發生日期).JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=5707ec45-12bd-4587-ba04-20eddf3e46c0")
,("2018_01_10140-01-04-2_臺中市 結婚對數按男女雙方年齡分(按發生日期).JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=83bddfbe-17c0-4c9e-b7ac-ee50f4a6427a")
,("2018_01_10140-01-05-2_臺中市 初婚人數按性別、年齡及教育程度分暨其結婚年齡中位數(按發生日期).JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=d6fc32fe-5cde-4247-93ff-145cf2441e05")
,("2018_01_10140-03-01-2_臺中市各區 離婚人數按離婚者性別及年齡分 (按發生日期).JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=c46cc29b-d7b1-4f53-8319-fc68dc0bcf27")
,("2018_01_10140-03-02-2_臺中市各區 離婚對數按男方年齡及女方原屬國籍(地區)與年齡分(按發生日期）.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=18cd3b39-34ec-4a09-9f6b-e346e61698ba")
,("2018_01_10140-03-03-2_臺中市各區 離婚對數按男方教育程度及女方原屬國籍(地區)與教育程度分(按發生日期).JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=22f4c41b-1988-4345-bfb5-37c344521a19")
,("2018_10140-03-08-2 臺中市各區 離婚人數按離婚者性別及年齡分 (按登記日期).JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=f5b2db9e-69f6-4cb8-aa1b-5d87fd8fdc4a")
,("2018_01_30220-01-04-2_臺中市山地平地原住民婚姻狀況.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=a5e6b01e-ab21-4df3-8162-d392113cb219")
,("2018_10_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=b3c5d2df-0c37-410e-9108-577e7671a0ab")
,("2018_09_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=ac474b5d-be13-499c-9bdb-1c0928fdcbd3")
,("2018_08_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=716597d3-3be5-46f4-b37d-adc938cfa219")
,("2018_07_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=ad2823c9-2109-449b-b908-25783dc7242a")
,("2018_06_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=d778f3f6-57eb-416e-8736-b0b8a2cb46fc")
,("2018_05_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=28da7db1-2521-4e77-97ad-bb26589a560d")
,("2018_04_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=2e02fb34-2bd2-4a7f-bda9-6fb16337bb97")
,("2018_03_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=737af98d-912e-4d67-94b3-11f5162312cd")
,("2018_02_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=f236f7ea-8213-455a-aa9f-529a025dc709")
,("2018_01_10140-03-21-2_臺中市各區 離婚人數按離婚者男女雙方原屬國籍(地區)分.JSON","https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=220a4a8f-bc05-4393-9f0c-6efd611c809f")
]

start = time()

pool = ThreadPool(5)

for _ in pool.imap_unordered(url_response, urls):
    pass

pool.close()
pool.join()

print("完成時間:", time() - start)