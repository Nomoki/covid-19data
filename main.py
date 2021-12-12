import requests
import matplotlib.pyplot as plt
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

getdataprovince = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces")
response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
getdatadender = requests.get("https://covid19.ddc.moph.go.th/api/Cases/round-3-line-lists")

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
province = getdataprovince.json()[0]['province']
Gender = getdatadender.json()['data'][0]['gender']


df = pd.read_json('https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all')
df.info()
pd.DataFrame(df)



def createNewWindow():
    newWindow = tk.Toplevel(app)
    lbl = tk.Label(newWindow,text= "ผู้ป่วยติดเชื้อใหม่ "+ str(newcase)).pack()
    newWindow.geometry("1000x1000")
    df['txn_date'] = df['txn_date'].astype('datetime64')
    df['txn_date'].groupby([df['txn_date'].dt.year, df['txn_date'].dt.month]).count().plot()
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Number of Cases')
    plt.title('Number of Reported Cases Each Month')
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
label = tk.Label(text= "จังหวัด "+ str(province)).pack()
label = tk.Label(text= "เพศ "+ str(Gender)).pack()
buttonExample = tk.Button(app, 
              text="Graph",
              command=createNewWindow).pack()
              


app.geometry("500x500")
app.mainloop()
