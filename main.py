
import requests
import tkinter as tk

response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
print("Daily report covid")
newcase = response.json()[0]['new_case']
total_case = response.json()[0]['total_case']
new_case_excludeabroad = response.json()[0]['new_case_excludeabroad']
total_case_excludeabroad = response.json()[0]['total_case_excludeabroad']
new_death = response.json()[0]['new_death']
total_death = response.json()[0]['total_death']
new_recovered = response.json()[0]['new_recovered']
total_recovered = response.json()[0]['total_recovered']
update_date = response.json()[0]['update_date']

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


app.geometry("500x500")
app.mainloop()
