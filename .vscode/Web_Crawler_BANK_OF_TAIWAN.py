import tkinter as tk
from tkinter import scrolledtext as st
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox as msg
import pyodbc
#爬蟲:抓取臺灣銀行美金匯率並存入Azure SQL

ww = tk.Tk()
ww.title("我的Python視窗")
ww.geometry("800x600")

def ConnectSQL(dbName,userName,pwd):
    srv = "marriage-analysis.database.windows.net"
    sqlConn = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
               srv + ";DATABASE=" + dbName + ";UID=" + userName + ";PWD=" + pwd)
    try:
        coxn = pyodbc.connect(sqlConn)
        return coxn
    except Exception as e:
        msg.showerror("失敗", str(e))
def Btn4_Click():
    myurl="https://rate.bot.com.tw/xrt/quote/l6m/USD"
    ans=""
    result=requests.get(myurl)
    result.encoding="utf-8"
    bs=BeautifulSoup(result.text,"html.parser")

    ans1=bs.find_all("td",{"class":"text-center"})
    for zz in ans1:
        ans += zz.text + "\n"

    ans2 = bs.find_all("td", {"class": "rate-content-sight text-right print_table-cell"})
    for zz in ans2:
        ans += zz.text + "\n"

    St1.delete("1.0","end")
    St1.insert("1.0",ans)

def Btn5_Click():
    myurl="https://rate.bot.com.tw/xrt/quote/l6m/USD"
    ans=""
    result=requests.get(myurl)
    result.encoding="utf-8"
    bs=BeautifulSoup(result.text,"html.parser")

    ans1=bs.find_all("td",{"class":"text-center"})
    lst1=[]
    for zz in ans1:
        lst1.append(zz.text)
    lst2=[]
    for i in range (0,len(lst1),2):
        lst2.append(lst1[i])
    del lst1

    lst3 = []
    ans2 = bs.find_all("td", {"class": "rate-content-sight text-right print_table-cell"})
    for zz in ans2:
        lst3.append(zz.text)

    final_lst=[]
    for i in range (len(lst2)):
        ll=[]
        ll.append(lst2[i])
        ll.append(lst3[i])
        ll.append(lst3[i+1])
        final_lst.append(ll)

    print(final_lst)

    St1.delete("1.0","end")
    St1.insert("1.0",final_lst)
    cnn = ConnectSQL("Marriage-Analysis", "stanleyoreo", "Zxcv1234")
    tsql = "INSERT INTO [美金匯率] VALUES(?,?,?)"
    for i in range(len(final_lst)):
        cnn.execute(tsql, (str(final_lst[i][0]),float(final_lst[i][1]),float(final_lst[i][2])))
        cnn.commit()  # 認可交易行為
    cnn.close()
    La1["text"] = "新增資料成功"
    msg.showinfo("成功", "新增資料成功")

La1=tk.Label(ww,text="請輸入：",bg="yellow",width=10)
La1.place(x=10,y=10)
Btn4=tk.Button(ww,text="按鈕4",width=10,height=1,command=Btn4_Click)
Btn5=tk.Button(ww,text="按鈕5",width=10,height=1,command=Btn5_Click)
St1=st.ScrolledText(ww,wrap=tk.WORD)
Btn4.place(x=200,y=100)
Btn5.place(x=300,y=100)
St1.place(x=10,y=200)


ww.mainloop()