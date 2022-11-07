from tkinter import *
from tkinter.font import Font

mainWindow = Tk()
mainWindow.geometry("700x832")
mainWindow.configure(bg='#FAECD8')
mainWindow.title('คำนวณพื้นที่สี่เหลี่ยม')

topic_font = Font (
    family="Angsana New",
    size=22,
    weight='bold'
)

big_font = Font (
    family="Angsana New",
    size=18,
    weight='bold'
) #fontของหัวข้อพื้นที่สี่เหลี่ยม-ปุ่มคำนวณ-ค่าพื้นที่

small_font = Font (
    family="Angsana New",
    size=16,
    weight='normal'
) #fontของหัวข้อที่ให้ผู้ใช้งานกรอก

def kite_result(event):
    label_result_kite_cm.configure(text=(float(textbox_side_kite_1.get()) * float(textbox_side_kite_2.get()))/2)
    label_result_kite_m.configure(text=(float(textbox_side_kite_1.get())/100 * float(textbox_side_kite_2.get())/100)/2)

def square_result(event):
    label_result_rectangle_cm.configure(text=float(textbox_width_rectangle.get()) * float(textbox_length_rectangle.get()))
    label_result_rectangle_m.configure(text=float(textbox_width_rectangle.get())/100 * float(textbox_length_rectangle.get())/100)

def trapezoid_result(event):
    label_result_trapezoid_cm.configure(text=((float(textbox_side_trapezoid_1.get()) + float(textbox_side_trapezoid_2.get()))
                                             * float(textbox_high_trapezoid.get()))/2)
    label_result_trapezoid_m.configure(text=((float(textbox_side_trapezoid_1.get())/100 + float(textbox_side_trapezoid_2.get())/100)
                                             * float(textbox_high_trapezoid.get())/100)/2)

#หัวข้อคำนวณพื้นที่สี่เหลี่ยม
label_topic = Label(mainWindow, text="คำนวณพื้นที่สี่เหลี่ยม 3 ประเภท", fg='white', font=topic_font, bg="#2D224D", width=30)
label_topic.grid(row=0, column=0)

#พื้นที่สี่เหลี่ยมรูปว่าว
label_kite = Label(mainWindow, text="พื้นที่สี่เหลี่ยมรูปว่าว", fg='white', font=big_font, bg="#0B354D", width=25)
label_kite.grid(row=1, column=0, pady=10)

label_side_kite_1 = Label(mainWindow, text="เส้นทแยงมุม 1 (cm.)", fg='white', font=small_font, bg="#397596", width=15)
label_side_kite_1.grid(row=1, column=1, pady=10)
textbox_side_kite_1 = Entry(mainWindow, bg="#C5D8E2")
textbox_side_kite_1.grid(row=1, column=2, pady=10)

label_side_kite_2 = Label(mainWindow, text="เส้นทแยงมุม 2 (cm.)", fg='white', font=small_font, bg="#397596", width=15)
label_side_kite_2.grid(row=2, column=1)
textbox_side_kite_2 = Entry(mainWindow, bg="#C5D8E2")
textbox_side_kite_2.grid(row=2, column=2)

calculate_button_kite = Button(mainWindow,text="คำนวณ", fg='white', font=big_font, bg="#1580b9", width=10, height=1)
calculate_button_kite.bind('<Button-1>',kite_result)
calculate_button_kite.grid(row=2, column=0, pady=3)

label_result_kite_cm = Label(mainWindow, text="ค่าพื้นที่สี่เหลี่ยมรูปว่าว (ตร.ซม.)", fg='white', font=big_font, bg="#235470")
label_result_kite_cm.grid(row=3, column=0, pady=10)
label_result_kite_m = Label(mainWindow, text="ค่าพื้นที่สี่เหลี่ยมรูปว่าว (ตร.ม.)", fg='white', font=big_font, bg="#235470")
label_result_kite_m.grid(row=3, column=1, pady=10)

#พื้นที่สี่เหลี่ยมผืนผ้า
label_rectangle = Label(mainWindow, text="พื้นที่สี่เหลี่ยมผืนผ้า", fg='white', font=big_font, bg="#5A0E0E", width=25)
label_rectangle.grid(row=4, column=0, pady=15)

label_width_rectangle = Label(mainWindow, text="ด้านกว้าง (cm.)", fg='white', font=small_font, bg="#A74040", width=15)
label_width_rectangle.grid(row=4, column=1, pady=10)
textbox_width_rectangle = Entry(mainWindow, bg="#E4BBBB")
textbox_width_rectangle.grid(row=4, column=2, pady=10)

label_length_rectangle = Label(mainWindow, text="ด้านยาว (cm.)", fg='white', font=small_font, bg="#A74040", width=15)
label_length_rectangle.grid(row=5, column=1)
textbox_length_rectangle = Entry(mainWindow, bg="#E4BBBB")
textbox_length_rectangle.grid(row=5, column=2)

calculate_button_rectangle = Button(mainWindow,text="คำนวณ", fg='white', font=big_font, bg="#C13C3C", width=10, height=1)
calculate_button_rectangle.bind('<Button-1>',square_result)
calculate_button_rectangle.grid(row=5, column=0, pady=3)

label_result_rectangle_cm = Label(mainWindow, text="ค่าพื้นที่สี่เหลี่ยมผืนผ้า (ตร.ซม.)", fg='white', font=big_font, bg="#8D4040")
label_result_rectangle_cm.grid(row=6, column=0, pady=10)
label_result_rectangle_m = Label(mainWindow, text="ค่าพื้นที่สี่เหลี่ยมผืนผ้า (ตร.ม.)", fg='white', font=big_font, bg="#8D4040")
label_result_rectangle_m.grid(row=6, column=1, pady=10)

#พื้นที่สี่เหลี่ยมคางหมู
label_trapezoid = Label(mainWindow, text="พื้นที่สี่เหลี่ยมคางหมู", fg='white', font=big_font, bg="#62400D", width=25)
label_trapezoid.grid(row=7, column=0, pady=15)

label_high_trapezoid = Label(mainWindow, text="ความสูง (cm.)", fg='white', font=small_font, bg="#B67C39", width=15)
label_high_trapezoid.grid(row=7, column=1, pady=10)
textbox_high_trapezoid = Entry(mainWindow, bg="#E0CD9A")
textbox_high_trapezoid.grid(row=7, column=2, pady=10)

label_side_trapezoid_1 = Label(mainWindow, text="ด้านคู่ขนาน1 (cm.)", fg='white', font=small_font, bg="#B67C39", width=15)
label_side_trapezoid_1.grid(row=8, column=1)
textbox_side_trapezoid_1 = Entry(mainWindow, bg="#E0CD9A")
textbox_side_trapezoid_1.grid(row=8, column=2)

label_side_trapezoid_2 = Label(mainWindow, text="ด้านคู่ขนาน2 (cm.)", fg='white', font=small_font, bg="#B67C39", width=15)
label_side_trapezoid_2.grid(row=9, column=1)
textbox_side_trapezoid_2 = Entry(mainWindow, bg="#E0CD9A")
textbox_side_trapezoid_2.grid(row=9, column=2)

calculate_button_trapezoid = Button(mainWindow,text="คำนวณ", fg='white', font=big_font, bg="#D19828", width=10, height=1)
calculate_button_trapezoid.bind('<Button-1>',trapezoid_result)
calculate_button_trapezoid.grid(row=8, column=0, pady=5)

label_result_trapezoid_cm = Label(mainWindow, text="ค่าพื้นที่สี่เหลี่ยมคางหมู (ตร.ซม.)", fg='white', font=big_font, bg="#8D7840")
label_result_trapezoid_cm.grid(row=10, column=0, pady=10)
label_result_trapezoid_m = Label(mainWindow, text="ค่าพื้นที่สี่เหลี่ยมคางหมู (ตร.ม.)", fg='white', font=big_font, bg="#8D7840")
label_result_trapezoid_m.grid(row=10, column=1, pady=10)

mainWindow.mainloop()