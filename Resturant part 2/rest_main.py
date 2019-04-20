from tkinter import*
import random
import time;
import datetime

root= Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management")
root.configure(background="black")

Tops = Frame(root, width = 1350,height = 100,bd =14,relief ="raise")
Tops.pack(side= TOP)

F1 = Frame(root, width = 900,height = 650,bd =8,relief ="raise")
F1.pack(side= LEFT)

F2 = Frame(root, width = 440,height = 650,bd =8,relief ="raise")
F2.pack(side= RIGHT)

F1a = Frame(F1, width = 900,height = 330,bd =8,relief ="raise")
F1a.pack(side= TOP)

F2a = Frame(F1, width = 900,height = 320,bd =6,relief ="raise")
F2a.pack(side= BOTTOM)

Ft2 = Frame(F2, width = 440,height = 450,bd =12,relief ="raise")
Ft2.pack(side= TOP)

Fb2 = Frame(F2, width = 440,height = 250,bd =16,relief ="raise")
Fb2.pack(side= BOTTOM)

F1aa = Frame(F1a, width = 400,height = 330,bd =16,relief ="raise")
F1aa.pack(side= LEFT)

F1ab = Frame(F1a, width = 400,height = 330,bd =16,relief ="raise")
F1ab.pack(side= RIGHT)

F2aa = Frame(F2a, width = 450,height = 330,bd =14,relief ="raise")
F2aa.pack(side= LEFT)

F2ab = Frame(F2a, width = 450,height = 330,bd =14,relief ="raise")
F2ab.pack(side= RIGHT)

Tops.configure(background="black")
F1.configure(background="black")
F2.configure(background="black")

lblInfo = Label(Tops, font=("arial",70,"bold"), text = "  Cafe Management Systems  ",bd=10)
lblInfo.grid(row=0,column=0)
#========================Functions====================


def qExit():
    root.destroy()
    return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Coffee.set("0")
    E_Espresso.set("0")
    E_IceCoffee.set("0")
    E_Cappuccino.set("0")
    E_american_coffee.set("0")
    E_italian_coffee.set("0")
    E_milk_tea.set("0")
    E_black_tea.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    E_Black_forest.set("0")
    E_Red_velvet.set("0")
    E_Vanilla_cake.set("0")
    E_Choco_cake.set("0")
    E_Amul_Cream.set("0")
    E_Lassi.set("0")
    E_Boston_cream.set("0")
    E_Strawberry_cake.set("0")

    txtCoffee.configure(stste=DISABLED)
    txtamerican_coffee.configure(stste=DISABLED)
    txtAmul_Cream.configure(stste=DISABLED)
    txtBlack_forest.configure(stste=DISABLED)
    txtblack_tea.configure(stste=DISABLED)
    txtBoston_cream.configure(stste=DISABLED)
    txtCappuccino.configure(stste=DISABLED)
    txtChoco_cake.configure(stste=DISABLED)
    txtEspresso.configure(stste=DISABLED)
    txtIceCoffee.configure(stste=DISABLED)
    txtitalian_coffee.configure(stste=DISABLED)
    txtLassi.configure(stste=DISABLED)
    txtmilk_tea.configure(stste=DISABLED)
    txtRed_velvet.configure(stste=DISABLED)
    txtStrawberry_cake.configure(stste=DISABLED)
    txtVanilla_cake.configure(stste=DISABLED)



#========================checkbutton==========================
def chkbutton_value():
    if(var1.get()==1):
        txtCoffee.configure(state=NORMAL)
    elif var1.get() == 0:
        txtCoffee.configure(state=DISABLED)
        E_Coffee.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
    if (var3.get() == 1):
        txtIceCoffee.configure(state=NORMAL)
    elif var3.get() == 0:
        txtIceCoffee.configure(state=DISABLED)
        E_IceCoffee.set("0")
    if (var4.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif var4.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")
    if (var5.get() == 1):
        txtamerican_coffee.configure(state=NORMAL)
    elif var5.get() == 0:
        txtamerican_coffee.configure(state=DISABLED)
        E_american_coffee.set("0")
    if (var6.get() == 1):
        txtitalian_coffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtitalian_coffee.configure(state=DISABLED)
        E_italian_coffee.set("0")
    if (var7.get() == 1):
        txtmilk_tea.configure(state=NORMAL)
    elif var7.get() == 0:
        txtmilk_tea.configure(state=DISABLED)
        E_milk_tea.set("0")
    if (var8.get() == 1):
        txtblack_tea.configure(state=NORMAL)
    elif var8.get() == 0:
        txtblack_tea.configure(state=DISABLED)
        E_black_tea.set("0")
    if (var9.get() == 1):
        txtBlack_forest.configure(state=NORMAL)
    elif var9.get() == 0:
        txtBlack_forest.configure(state=DISABLED)
        E_Coffee.set("0")
    if (var10.get() == 1):
        txtRed_velvet.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRed_velvet.configure(state=DISABLED)
        E_Red_velvet.set("0")
    if (var11.get() == 1):
        txtVanilla_cake.configure(state=NORMAL)
    elif var11.get() == 0:
        txtVanilla_cake.configure(state=DISABLED)
        E_Vanilla_cake.set("0")
    if (var12.get() == 1):
        txtChoco_cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtChoco_cake.configure(state=DISABLED)
        E_Choco_cake.set("0")
    if (var13.get() == 1):
        txtAmul_Cream.configure(state=NORMAL)
    elif var13.get() == 0:
        txtAmul_Cream.configure(state=DISABLED)
        E_Amul_Cream.set("0")
    if (var14.get() == 1):
        txtLassi.configure(state=NORMAL)
    elif var14.get() == 0:
        txtLassi.configure(state=DISABLED)
        E_Lassi.set("0")
    if (var15.get() == 1):
        txtBoston_cream.configure(state=NORMAL)
    elif var15.get() == 0:
        txtBoston_cream.configure(state=DISABLED)
        E_Boston_cream.set("0")
    if (var16.get() == 1):
        txtStrawberry_cake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtStrawberry_cake.configure(state=DISABLED)
        E_Strawberry_cake.set("0")

def CostofItems():
    Item1=float(E_Coffee.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_IceCoffee.get())
    Item4 = float(E_italian_coffee.get())
    Item5 = float(E_american_coffee.get())
    Item6 = float(E_black_tea.get())
    Item7 = float(E_milk_tea.get())
    Item8 = float(E_Cappuccino.get())

    Item9 = float(E_Black_forest.get())
    Item10 = float(E_Boston_cream.get())
    Item11 = float(E_Red_velvet.get())
    Item12 = float(E_Lassi.get())
    Item13 = float(E_Strawberry_cake.get())
    Item14 = float(E_Vanilla_cake.get())
    Item15 = float(E_Amul_Cream.get())
    Item16 = float(E_Choco_cake.get())

    PriceofDrinks = (Item1 * 120) + (Item2 * 200) + (Item3 * 100) + (Item4 * 400) + (Item5 * 220) + (Item6* 60) + (Item7 * 80) + (Item8 * 400)

    PriceofCakes = (Item9 * 600) + (Item10 * 300) + (Item11 *500 ) + (Item12 * 100) + (Item13 *400 ) + (Item14 * 300) + (Item15 *50 ) + (Item16 * 200)

    DrinksPrice = "Rs", str("%.1f"%(PriceofDrinks))
    CakesPrice = "Rs", str("%.1f"%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="Rs", str("%.1f"%(50))
    ServiceCharge.set(SC)
    SubTotalofItems = "Rs",str("%.1f"%(PriceofDrinks + PriceofCakes + 50))
    SubTotal.set(SubTotalofItems)

    Tax = "Rs",str("%.1f"%((PriceofDrinks + PriceofCakes + 50)*0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 50)*0.15)
    TC ="Rs",str("%.1f"%(PriceofDrinks + PriceofCakes + 50 + TT))
    TotalCost.set(TC)


def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10900,50000)
    randomRef=str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END,"Receipt Ref:\t\t\t"+ Receipt_Ref.get() + "\t\t"+ DateofOrder.get()+"\n")
    txtReceipt.insert(END,"ITEMS\t\t\t\t\t"+"Cost Of Items \n\n")
    txtReceipt.insert(END,"Coffee:\t\t\t\t\t"+E_Coffee.get()+ "\n")
    txtReceipt.insert(END,"Espresso:\t\t\t\t\t"+E_Espresso.get()+ "\n")
    txtReceipt.insert(END,"Ice Coffee:\t\t\t\t\t"+E_IceCoffee.get()+ "\n")
    txtReceipt.insert(END,"Cappuccino:\t\t\t\t\t"+E_Cappuccino.get()+ "\n")
    txtReceipt.insert(END,"American Coffee:\t\t\t\t\t"+E_american_coffee.get()+ "\n")
    txtReceipt.insert(END, "Italian Coffee:\t\t\t\t\t" + E_italian_coffee.get() + "\n")
    txtReceipt.insert(END, "MilkTea:\t\t\t\t\t" + E_milk_tea.get() + "\n")
    txtReceipt.insert(END, "BlackTea:\t\t\t\t\t" + E_black_tea.get() + "\n")
    txtReceipt.insert(END, "Black Forest:\t\t\t\t\t" + E_Black_forest.get() + "\n")
    txtReceipt.insert(END, "Red velvet:\t\t\t\t\t" + E_Red_velvet.get() + "\n")
    txtReceipt.insert(END, "vanilla Cake\t\t\t\t\t" + E_Vanilla_cake.get() + "\n")
    txtReceipt.insert(END, "Choco Cake\t\t\t\t\t" + E_Choco_cake.get() + "\n")
    txtReceipt.insert(END, "Amul Cream\t\t\t\t\t" + E_Amul_Cream.get() + "\n")
    txtReceipt.insert(END, "Lassi\t\t\t\t\t" + E_Lassi.get() + "\n")
    txtReceipt.insert(END, "Boston Cream\t\t\t\t\t" + E_Boston_cream.get() + "\n")
    txtReceipt.insert(END, "Strawberry Cake\t\t\t\t\t" + E_Strawberry_cake.get() + "\n")
    txtReceipt.insert(END, "Cost Of Drinks\t\t" +CostofDrinks.get() +"\tTaxPaid:\t\t"+PaidTax.get()+"\n")
    txtReceipt.insert(END, "Cost Of Cakes\t\t" + CostofCakes.get() + "\tSub Total:\t\t" + SubTotal.get() + "\n")
    txtReceipt.insert(END, "Cost Of Drinks\t\t" + ServiceCharge.get() + "\tTotal Cost:\t\t" + TotalCost.get() + "\n")







#==========================


#=====================Variables=================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()


E_Coffee=StringVar()
E_Espresso=StringVar()
E_IceCoffee=StringVar()
E_Cappuccino=StringVar()
E_american_coffee=StringVar()
E_italian_coffee=StringVar()
E_milk_tea=StringVar()
E_black_tea=StringVar()

E_Black_forest=StringVar()
E_Red_velvet=StringVar()
E_Vanilla_cake=StringVar()
E_Choco_cake=StringVar()
E_Amul_Cream=StringVar()
E_Lassi=StringVar()
E_Boston_cream=StringVar()
E_Strawberry_cake=StringVar()


E_Coffee.set("0")
E_Espresso.set("0")
E_IceCoffee.set("0")
E_Cappuccino.set("0")
E_american_coffee.set("0")
E_italian_coffee.set("0")
E_milk_tea.set("0")
E_black_tea.set("0")

E_Black_forest.set("0")
E_Red_velvet.set("0")
E_Vanilla_cake.set("0")
E_Choco_cake.set("0")
E_Amul_Cream.set("0")
E_Lassi.set("0")
E_Boston_cream.set("0")
E_Strawberry_cake.set("0")

DateofOrder.set(time.strftime("%d/%m.%y"))


#======================drinks=====================
Coffee = Checkbutton(F1aa,text="Coffee \t",variable = var1,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 0,sticky=W)

Espresso = Checkbutton(F1aa,text="Espresso \t",variable = var2,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 1,sticky=W)

IceCoffee = Checkbutton(F1aa,text="Ice Coffee \t",variable = var3,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 2,sticky=W)

Cappuccino = Checkbutton(F1aa,text="Cappuccinoo \t",variable = var4,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 3,sticky=W)

american_coffee = Checkbutton(F1aa,text="American Coffee \t",variable = var5,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 4,sticky=W)

italian_coffee = Checkbutton(F1aa,text="Italian Coffee \t",variable = var6,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 5,sticky=W)

milk_tea = Checkbutton(F1aa,text="Milk Tea \t",variable = var7,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 6,sticky=W)

black_tea = Checkbutton(F1aa,text="Black Tea \t",variable = var8,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 7,sticky=W)

#=========================cakes====================

Black_forest = Checkbutton(F1ab,text="BlackForest \t",variable = var9,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 0,sticky=W)

Red_velvet = Checkbutton(F1ab,text="Red Velvet \t",variable = var10,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 1,sticky=W)

Vanilla_cake = Checkbutton(F1ab,text="Vanilla Cake \t",variable = var11,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 2,sticky=W)

Choco_cake = Checkbutton(F1ab,text="Choco cake \t",variable = var12,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 3,sticky=W)

Amul_Cream = Checkbutton(F1ab,text="Amul Icecream \t",variable = var13,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 4,sticky=W)

Lassi = Checkbutton(F1ab,text="Lassi \t",variable = var14,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 5,sticky=W)

Boston_cream = Checkbutton(F1ab,text="Boston Cream \t",variable = var15,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 6,sticky=W)

Strawberry_cake = Checkbutton(F1ab,text="StrawBerry Cake \t",variable = var16,onvalue= 1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row = 7,sticky=W)

#========================Enter Widget for drinks=============

txtCoffee = Entry(F1aa,font=("arial",16,"bold"),bd=8,textvariable=E_Coffee,width=6,justify="left",state=DISABLED)
txtCoffee.grid(row=0,column=1)
txtEspresso = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Espresso,justify="left",state=DISABLED)
txtEspresso.grid(row=1,column=1)
txtIceCoffee = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_IceCoffee,justify="left",state=DISABLED)
txtIceCoffee.grid(row=2,column=1)
txtCappuccino = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Cappuccino,justify="left",state=DISABLED)
txtCappuccino.grid(row=3,column=1)
txtamerican_coffee = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_american_coffee,justify="left",state=DISABLED)
txtamerican_coffee.grid(row=4,column=1)
txtitalian_coffee = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_italian_coffee,justify="left",state=DISABLED)
txtitalian_coffee.grid(row=5,column=1)
txtmilk_tea = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_milk_tea,justify="left",state=DISABLED)
txtmilk_tea.grid(row=6,column=1)
txtblack_tea = Entry(F1aa,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_black_tea,justify="left",state=DISABLED)
txtblack_tea.grid(row=7,column=1)

#=========================Enter Widget for skins================

txtBlack_forest = Entry(F1ab,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Black_forest,justify="left",state=DISABLED)
txtBlack_forest.grid(row=0,column=1)
txtRed_velvet = Entry(F1ab,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Red_velvet,justify="left",state=DISABLED)
txtRed_velvet.grid(row=1,column=1)
txtVanilla_cake = Entry(F1ab,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Vanilla_cake,justify="left",state=DISABLED)
txtVanilla_cake.grid(row=2,column=1)
txtChoco_cake = Entry(F1ab,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Choco_cake,justify="left",state=DISABLED)
txtChoco_cake.grid(row=3,column=1)
txtAmul_Cream = Entry(F1ab,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Amul_Cream,justify="left",state=DISABLED)
txtAmul_Cream.grid(row=4,column=1)
txtLassi = Entry(F1ab,font=("arial",16,"bold"),bd=8,width=6,textvariable=E_Lassi,justify="left",state=DISABLED)
txtLassi.grid(row=5,column=1)
txtBoston_cream = Entry(F1ab,font=("arial",16,"bold"),bd=8,textvariable=E_Boston_cream,width=6,justify="left",state=DISABLED)
txtBoston_cream.grid(row=6,column=1)
txtStrawberry_cake = Entry(F1ab,font=("arial",16,"bold"),bd=8,textvariable=E_Strawberry_cake,width=6,justify="left",state=DISABLED)
txtStrawberry_cake.grid(row=7,column=1)

#========================Information===========================

lblReceipt = Label(Ft2,font=("arial",12,"bold"),text = "Receipt",bd=2,anchor="w")
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt = Text(Ft2,font=("arial",11,"bold"),bd=8,width = 59,height = 22,bg="white")
txtReceipt.grid(row=1,column=0)

#===================Cost Items Information====================

lblCostofDrinks=Label(F2aa,font=("arial",16,"bold"),text="Cost Of Drinks",bd=8,anchor="w")
lblCostofDrinks.grid(row=2,column=0,sticky=W)
txtCostofDrinks=Entry(F2aa,font=("arial",16,"bold"),bd=8,justify="left",insertwidth=2, textvariable=CostofDrinks)
txtCostofDrinks.grid(row = 2,column = 1)

lblCostofCakes=Label(F2aa,font=("arial",16,"bold"),text="Cost Of Cakes",bd=8,anchor="w")
lblCostofCakes.grid(row=3,column=0,sticky=W)
txtCostofCakes=Entry(F2aa,font=("arial",16,"bold"),bd=8,justify="left",insertwidth=2, textvariable=CostofCakes)
txtCostofCakes.grid(row = 3,column = 1)

lblServiceCharge=Label(F2aa,font=("arial",16,"bold"),text="Service Charge",bd=8,anchor="w")
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(F2aa,font=("arial",16,"bold"),bd=8,justify="left",insertwidth=2, textvariable=ServiceCharge)
txtServiceCharge.grid(row = 4,column = 1)
#==================payment information======================
lblPaidTax=Label(F2ab,font=("arial",16,"bold"),text="Paid Tax",bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(F2ab,font=("arial",16,"bold"),bd=8,justify="left", textvariable=PaidTax,insertwidth=2)
txtPaidTax.grid(row = 2,column = 1)

lblSubTotal=Label(F2ab,font=("arial",16,"bold"),text="Sub Total",bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(F2ab,font=("arial",16,"bold"),bd=8,justify="left",textvariable=SubTotal,insertwidth=2)
txtSubTotal.grid(row = 3,column = 1)

lblTotalCost=Label(F2ab,font=("arial",16,"bold"),text="Total",bd=8)
lblTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(F2ab,font=("arial",16,"bold"),bd=8,justify="left",textvariable=TotalCost,insertwidth=2)
txtTotalCost.grid(row = 4,column = 1)

#========================Buttons===============================
btnTotal=Button(Fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=5,text="Total",command=CostofItems).grid(row=0,column=0)
btnReceipt=Button(Fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)
btnReset=Button(Fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=5,text="Reset",command=Reset).grid(row=0,column=2)
btnExit=Button(Fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=5,text="Exit",command=qExit).grid(row=0,column=3)


root.mainloop()

