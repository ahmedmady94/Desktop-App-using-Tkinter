import tkinter as tk
from tkinter import *
import math
import pandas as pd
from tkinter import font as tkFont


df= pd.read_csv('data.csv')
df
K= dict(zip(df['Gas'],df['Ratio of Specific Heat K']))
M= dict(zip(df['Gas'],df['Molar Mass']))


root=tk.Tk()

canvas= tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)



instructions= tk.Label(root,text='Calculate exhaust velocity & impulse for rocket engine',font="Raleway")
instructions.grid(columnspan=3,column=0,row=0)

label1 = tk.Label(root, text='Select your fuel type:',font=('Helvetica', 10, 'bold'))
label1.configure(font=("Helvetica",10,"bold"))
label1.grid(columnspan=1,column=0,row=1)


OPTIONS = ['Acetylene', 'Air, Standard', 'Ammonia', 'Argon', 'Benzene',
       'N-butane', 'Carbon Dioxide', 'Carbon Monoxide', 'Chlorine',
       'Ethane', 'Ethyl alcohol', 'Ethyl chloride', 'Ethylene', 'Helium',
       'Heptane', 'Hexane', 'Hydrochloric acid', 'Hydrogen',
       'Hydrogen chloride', 'Hydrogen sulphide', 'Methane',
       'Methyl alcohol', 'Methyl chloride', 'Natural Gas (Methane)',
       'Nitrogen', 'Oxygen', 'Pentane', 'Propane', 'R-11', 'R-12', 'R-22',
       'R-114', 'R-123', 'R-134a', 'Steam (water)', 'Sulphur dioxide',
       'Toulene']

variable = StringVar(root)
variable.set(OPTIONS[-3]) # default value
w = OptionMenu(root, variable, *OPTIONS)
w.grid(columnspan=3,column=0,row=1)
w.config(font=('Helvetica',(12)),bg='yellow',width=12)


label2 = tk.Label(root, text='Enter your chamber temperature:',fg='red',font=('Helvetica', 10, 'bold'))
label2.configure(font=("Helvetica",10,"bold"))
label2.grid(columnspan=3,column=0,row=2)



entry1 = tk.Entry (root,font=("Helvetica", 12))
entry1.grid(columnspan=3,column=0,row=3)



def callback():
    print ('You selected the fuel: ',variable.get())
    fuel_type=variable.get()
    Tc=int(entry1.get())
    
    R=8.31
    k= K.get(fuel_type)
    m= M.get(fuel_type)/1000
    Ve= round(math.sqrt(((2*k)/(k-1))* R* Tc/m),2)
    impulse= round(Ve/9.81,2)
    
    text_box=tk.Text(root,fg='blue',height=2,width=50,padx=15,pady=15,font=("Helvetica", 10))
    text_box.insert(END,f'exhaust velocity equals: {Ve} m/s \nspecific impulse equals: {impulse} s')
    text_box.tag_configure('center',justify='center')
    text_box.tag_add('center','end')
    text_box.grid(columnspan=3,column=0,row=5)


canvas= tk.Canvas(root,width=600,height=250)
canvas.grid(columnspan=3)

MyButton = tk.Button(root, text="Submit", font="Raleway",bg='#20bebe',fg='white',width=15,height=2,command=lambda:callback())
MyButton.grid(columnspan=3,column=0,row=4)



canvas= tk.Canvas(root,width=600,height=250)
canvas.grid(columnspan=3)







root.mainloop()