from tkinter import *
import math
MainWindow = Tk()
MainWindow.title('คำนวณค่า BMI')
MainWindow.configure(bg='#b9e3f9')

def leftClickButton(event):
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if result >= 30.0:
        labelResultLevel.configure(text = "อ้วนมาก")
    elif result >= 25.0 and result <= 29.9:
        labelResultLevel.configure(text = "อ้วน")
    elif result >= 23.0 and result <= 24.9:
        labelResultLevel.configure(text = "น้ำหนักเกิน")
    elif result >= 18.6 and result <= 22.9:
        labelResultLevel.configure(text = "น้ำหนักปกติ")
    elif result < 18.5:
        labelResultLevel.configure(text = "ผอมเกินไป")

labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.)",fg = 'white',font = ('Prompt',17,'bold'),bg = "#384c57",width=12)
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text = "น้ำหนัก (kg.)",fg = 'white' , font = ('Prompt',17,'bold'),bg = "#3b5867",width=12)
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวณ",fg = 'white', font = ('Prompt',17,'bold'),bg = "#1580b9")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text = "ค่า BMI",fg = 'white', font = ('Prompt',17,'bold'),bg = "#0c344a")
labelResult.grid(row=2,column=1)

labelResultLevel = Label(MainWindow,text = "ระดับ BMI",fg = 'white', font = ('Prompt',17,'bold'),bg = "#23546f")
labelResultLevel.grid(row=3,column=1)

MainWindow.mainloop()