import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, title
import pandas as pd
import json
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


response = requests.get(
    "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")

getdata = requests.get(
    "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
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

df = pd.read_json(
    'https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all')
df.info()
pd.DataFrame(df)

# ดึงเคสล่าสุด 5 เคสจาก json url(getdata) มาใส่ตัวแปร
timeline_5_day = [getdata.json()[-5]['txn_date'], getdata.json()[-4]['txn_date'],
                getdata.json()[-3]['txn_date'], getdata.json()[-2]['txn_date'], getdata.json()[-1]['txn_date']]
newcase1 = [getdata.json()[-5]['new_case'], getdata.json()[-4]['new_case'],
            getdata.json()[-3]['new_case'], getdata.json()[-2]['new_case'], getdata.json()[-1]['new_case']]
new_recovered1 = [getdata.json()[-5]['new_recovered'], getdata.json()[-4]['new_recovered'],
                getdata.json()[-3]['new_recovered'], getdata.json()[-2]['new_recovered'], getdata.json()[-1]['new_recovered']]


def createNewWindow():
    figure(figsize=(12, 8), dpi=70, label='New Case & New recovered')
    plt.plot(timeline_5_day, newcase1, 'bo-')
    plt.plot(timeline_5_day, new_recovered1, 'go-')
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Number of Cases')
    plt.title('Number of New Case and New recovered Cases Each Day')
    plt.legend(['New case', 'New recovered'])
    plt.show()


new_death1 = [getdata.json()[-5]['new_death'], getdata.json()[-4]['new_death'],
              getdata.json()[-3]['new_death'], getdata.json()[-2]['new_death'], getdata.json()[-1]['new_death']]


def createNewWindow_new_death():
    figure(figsize=(12, 8), dpi=70, label='New Death')
    
    plt.plot(timeline_5_day, new_death1, 'ro-')
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Number of Cases')
    plt.title('Number of New Death Cases Each Day')
    plt.legend(['New death'])
    plt.show()

def createNewWindow_new_recovered():
    figure(figsize=(12, 8), dpi=70,label='New Recovered')
    plt.plot(timeline_5_day, new_recovered1, 'go-')
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Number of Cases')
    plt.title('Number of New Recovered Cases Each Day')
    plt.legend(['New death'])
    plt.show()

app = tk.Tk()
app.title('Report Covid-19')

canvas = tk.Canvas(app, height=700, width=800)
canvas.pack()

bg = ImageTk.PhotoImage(file="covid.png")
canvas.create_image( 0, 0, image = bg, anchor = "nw")
def resize_image(e):
    global image, resized, image2
    image = Image.open("covid.png")
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
app.bind("<Configure>", resize_image)

frame1 = tk.Frame(app, bg='#A51717', bd=5)
frame1.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.15, anchor='n')

label1 = tk.Label(frame1, text="ผู้ป่วยติดเชื้อรายใหม่\n+ "+ str(newcase), font=("TH SarabunPSK", 24), bg='#A51717', fg="#FFFFFF")
label1.place(relwidth=1, relheight=1)

frame2 = tk.Frame(app, bg='#891414', bd=5)
frame2.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.12,anchor='n')

label2 = tk.Label(frame2, text="ผู้ป่วยติดเชื้อสะสม\n+ " + str(total_case), font=("TH SarabunPSK", 20), bg='#891414', fg="#FFFFFF")
label2.place(relwidth=1, relheight=1)

frame3 = tk.Frame(app, bg='#343434', bd=5)
frame3.place(relx=0.25, rely=0.45, relwidth=0.4, relheight=0.12,anchor='n')

label5 = tk.Label(frame3, text="ผู้เสียชีวิตรายใหม่\n" + str(new_death), font=("TH SarabunPSK", 20), bg='#343434', fg="#FFFFFF")
label5.place(relwidth=1, relheight=1)

frame4 = tk.Frame(app, bg='#343434', bd=5)
frame4.place(relx=0.75, rely=0.45, relwidth=0.4, relheight=0.12,anchor='n')

label6 = tk.Label(frame4, text="ผู้เสียชีวิตสะสม\n" + str(total_death), font=("TH SarabunPSK", 20), bg='#343434', fg="#FFFFFF")
label6.place(relwidth=1, relheight=1)

frame5 = tk.Frame(app, bg='#0E2085', bd=5)
frame5.place(relx=0.25, rely=0.65, relwidth=0.4, relheight=0.22,anchor='n')

label3 = tk.Label(frame5, text="ผู้ป่วยไม่รวมผู้ติดเชื้อต่างประเทศ", font=("TH SarabunPSK", 18), bg='#0E2085', fg="#FFFFFF")
label3.pack(side='top')

label5 = tk.Label(frame5, text="ผู้ติดเชื้อรายใหม่\n+ " + str(new_case_excludeabroad), font=("TH SarabunPSK", 16), bg='#0E2085', fg="#FFFFFF")
label5.pack(side='top')

label4 = tk.Label(frame5, text="ผู้ติดเชื้อสะสม\n" +str(total_case_excludeabroad), font=("TH SarabunPSK", 16), bg='#0E2085', fg="#FFFFFF")
label4.pack(side='top')

frame6 = tk.Frame(app, bg='#22732B', bd=5)
frame6.place(relx=0.75, rely=0.65, relwidth=0.4, relheight=0.22,anchor='n')

label7 = tk.Label(frame6, text="ผู้ได้รับการรักษาใหม่\n+ " + str(new_recovered), font=("TH SarabunPSK", 18), bg='#22732B', fg="#FFFFFF")
label7.pack(side='top')

label8 = tk.Label(frame6, text="\nผู้ได้รับการรักษาสะสม\n" + str(total_recovered), font=("TH SarabunPSK", 18), bg='#22732B', fg="#FFFFFF")
label8.pack(side='top')

frame7 = tk.Frame(app, bg='#22732B')
frame7.place(relx=0.5, rely=0.9, relwidth=0.5, relheight=0.05,anchor='n')

buttonG = tk.Button(frame7, text="กราฟผู้ติดเชื้อรายใหม่", command=createNewWindow)
buttonG.pack(side='left', fill='both', expand=True)

buttonD = tk.Button(frame7, text="กราฟผู้เสียชีวิตรายวัน", command=createNewWindow_new_death)
buttonD.pack(side='left', fill='both', expand=True)

buttonR = tk.Button(frame7, text="กราฟผู้ได้รับการรักษาใหม่",command=createNewWindow_new_recovered)
buttonR.pack(side='left', fill='both', expand=True)

app.mainloop()
