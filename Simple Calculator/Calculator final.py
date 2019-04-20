from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set(operator)

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""


cal = Tk()
cal.title("Calculator final")
operator= ""
text_Input= StringVar()
txtDisplay= Entry(cal,font=("arial",20,"bold"),textvariable=text_Input,bd = 30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick(7),font=("arial",20,"bold"),text="7",bg="powder blue").grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick(8),font=("arial",20,"bold"),text="8",bg="powder blue").grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8,command=lambda:btnClick(9),fg="black",font=("arial",20,"bold"),text="9",bg="powder blue").grid(row=1,column=2)

Addition=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick("+"),font=("arial",20,"bold"),text="+",bg="powder blue").grid(row=1,column=3)

#--------------------------------------------------------------------------------------------------------------

btn4=Button(cal,padx=16,bd=8,command=lambda:btnClick(4),fg="black",font=("arial",20,"bold"),text="4",bg="powder blue").grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8,command=lambda:btnClick(5),fg="black",font=("arial",20,"bold"),text="5",bg="powder blue").grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8,command=lambda:btnClick(6),fg="black",font=("arial",20,"bold"),text="6",bg="powder blue").grid(row=2,column=2)

subtraction=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick("-"),font=("arial",20,"bold"),text="-",bg="powder blue").grid(row=2,column=3)

#--------------------------------------------------------------------------------------------------------------

btn1=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick(1),font=("arial",20,"bold"),text="1",bg="powder blue").grid(row=3,column=0)

btn2=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick(2),font=("arial",20,"bold"),text="2",bg="powder blue").grid(row=3,column=1)

btn3=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick(3),font=("arial",20,"bold"),text="3",bg="powder blue").grid(row=3,column=2)

multiply=Button(cal,padx=16,bd=8,fg="black",command=lambda:btnClick("*"),font=("arial",20,"bold"),text="*",bg="powder blue").grid(row=3,column=3)

#--------------------------------------------------------------------------------------------------------------

btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",command=lambda:btnClick(0),font=("arial",20,"bold"),text="0",bg="powder blue").grid(row=4,column=0)

btnClear=Button(cal,padx=16,pady=16,bd=8,fg="black",command=btnClearDisplay,font=("arial",20,"bold"),text="C",bg="powder blue").grid(row=4,column=1)

btnEquals=Button(cal,padx=16,pady=16,bd=8,fg="black",command=btnEqualsInput,font=("arial",20,"bold"),text="=",bg="powder blue").grid(row=4,column=2)

division=Button(cal,padx=16,pady=16,bd=8,fg="black",command=lambda:btnClick("/"),font=("arial",20,"bold"),text="/",bg="powder blue").grid(row=4,column=3)


cal.mainloop()
