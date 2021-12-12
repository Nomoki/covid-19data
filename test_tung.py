import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import tkinter as tk

def get_covid19_report(url):
    response = requests.get(url)
    data = response.json()
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return data

url = 'https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all'
get_covid19_report(url)

with open('data.json') as f:
    raw = json.load(f)
    df = pd.read_json('data.json')


response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")

getdata = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
print("Daily report covid")
print(getdata.json()[0]['total_case'])
newcase = response.json()[0]['new_case']
total_case = response.json()[0]['total_case']
new_case_excludeabroad = response.json()[0]['new_case_excludeabroad']
total_case_excludeabroad = response.json()[0]['total_case_excludeabroad']
new_death = response.json()[0]['new_death']
total_death = response.json()[0]['total_death']
new_recovered = response.json()[0]['new_recovered']
total_recovered = response.json()[0]['total_recovered']
update_date = response.json()[0]['update_date']

df = pd.read_json('https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all')
df.info()
pd.DataFrame(df)

#ดึงเคสล่าสุด 5 เคสจาก json url(getdata) มาใส่ตัวแปร
timeline_5_day = [getdata.json()[-5]['txn_date'], getdata.json()[-4]['txn_date'], \
            getdata.json()[-3]['txn_date'], getdata.json()[-2]['txn_date'], getdata.json()[-1]['txn_date']]
newcase1 = [getdata.json()[-5]['new_case'], getdata.json()[-4]['new_case'], \
            getdata.json()[-3]['new_case'], getdata.json()[-2]['new_case'], getdata.json()[-1]['new_case']]
new_recovered1 = [getdata.json()[-5]['new_recovered'], getdata.json()[-4]['new_recovered'], \
            getdata.json()[-3]['new_recovered'], getdata.json()[-2]['new_recovered'], getdata.json()[-1]['new_recovered']]

def createNewWindow():
    newWindow = tk.Toplevel(app)
    lbl = tk.Label(newWindow,text= "ผู้ป่วยติดเชื้อใหม่ "+ str(newcase)).pack()
    newWindow.geometry("500x500")
    plt.plot(timeline_5_day, newcase1, 'go-')
    plt.plot(timeline_5_day, new_recovered1, 'ro-')
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Number of Cases')
    plt.title('Number of Reported Cases Each Month')
    plt.legend(['New case', 'New recovered'])
    plt.show()

    

new_death1 = [getdata.json()[-5]['new_death'], getdata.json()[-4]['new_death'], \
            getdata.json()[-3]['new_death'], getdata.json()[-2]['new_death'], getdata.json()[-1]['new_death']]


def createNewWindow_new_death():
    newWindow = tk.Toplevel(app)
    lbl = tk.Label(newWindow,text= "จำนวนผู้เสียชีวิต "+ str(new_death)).pack()
    newWindow.geometry("500x500")
    plt.bar(timeline_5_day, new_death1)
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Number of Cases')
    plt.title('Number of Reported Cases Each Month')
    plt.legend(['New death'])
    plt.show()


app = tk.Tk()
app.title('Report Covid-19')
label = tk.Label(text= "ผู้ป่วยติดเชื้อใหม่ "+ str(newcase)).pack()
label = tk.Label(text= "ผู้ป่วยติดเชื้อสะสม "+ str(total_case)).pack()
label = tk.Label(text= "ผู้ป่วยติดเชื้อใหม่ไม่รวมผู้ติดเชื้อต่างประเทศ "+ str(new_case_excludeabroad)).pack()
label = tk.Label(text= "ผู้ป่วยติดเชื้อสะสมไม่รวมผู้ติดเชื้อต่างประเทศ "+ str(total_case_excludeabroad)).pack()
label = tk.Label(text= "ผู้เสียชีวิตรายใหม่ "+ str(new_death)).pack()
label = tk.Label(text= "ผู้เสียชีวิตสะสม "+ str(total_death)).pack()
label = tk.Label(text= "ผู้ได้รับการรักษาใหม่ "+ str(new_recovered)).pack()
label = tk.Label(text= "ผู้ได้รับการรักษาสะสม "+ str(total_recovered)).pack()
label = tk.Label(text= "วันที่๊ Update ข้อมูล "+ str(update_date)).pack()
buttonExample = tk.Button(app, 
              text="Graph",
              command=createNewWindow).pack()
buttonExample = tk.Button(app, 
              text="new_death",
              command=createNewWindow_new_death).pack()

app.geometry("500x500")
app.mainloop()