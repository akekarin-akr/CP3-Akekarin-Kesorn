from tkinter import *

def leftClickbutton(event):
    calculatedata = float(textBoxWeight.get()) / ((float(textBoxHeight.get()) / 100) ** 2)
    labelResult.configure(text= "BMI : %.1f" % calculatedata)
    if calculatedata >= 30.0:
        labelAnalyze.configure(text= "อ้วนมาก", font= ("angsana new", 18))
    elif calculatedata >= 25.0:
        labelAnalyze.configure(text="อ้วน", font= ("angsana new", 18))
    elif calculatedata >= 23.0:
        labelAnalyze.configure(text="น้ำหนักเกิน", font= ("angsana new", 18))
    elif calculatedata >= 18.6:
        labelAnalyze.configure(text="น้ำหนักปกติ เหมาะสม", font= ("angsana new", 18))
    else:
        labelAnalyze.configure(text="ผอมเกินไป", font= ("angsana new", 18))

MainWindow = Tk()
MainWindow.title("คำนวณค่า BMI")
labelHeight = Label(MainWindow, text= "Height(cm.)")
labelHeight.grid(row=0, column= 0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row= 0, column= 1)
labelWeight = Label(MainWindow, text= "Weight(kg.)")
labelWeight.grid(row= 1, column= 0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row= 1, column= 1)
calculateButton = Button(MainWindow, text= "Calculate")
calculateButton.bind("<Button-1>", leftClickbutton)
calculateButton.grid(row=2, column= 0)
labelResult = Label(MainWindow, text="Result")
labelResult.grid(row= 2, column= 1)
labelAnalyze = Label(MainWindow, text= "Analyze")
labelAnalyze.grid(row= 3, column = 1)
MainWindow.mainloop()
