from datetime import datetime
name=input("ENTER THE NAME:")
# LIST OF ITEMS IN SUPERMARKET
list="""
Rice                 Rs  45/kg
Curd                 Rs  30/450gms
Facewash             Rs  249/each
Hairoil              Rs   350/each
Cashew               Rs   999/kg
Pumpkinseeds         Rs   600/kg
Mushroom             Rs   240/kg
Panneer              Rs   300/kg
"""
# DECLARATION
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
# RATES OF ITEMS
items={"Rice":45,"Curd":30,"Facewash":249,"Hairoil":350,"Cashew":999,"Pumpkinseeds":600,"Mushroom":240,"Panner":300}
option=int(input("FOR LIST OF ITEMS PRESS 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inpt1=int(input("PRESS 1 TO BUY, PRESS 2 TO EXIT:"))
    if inpt1==2:
        break
    if inpt1==1:
        item=input("ENTER YOUR ITEM:")
        quantity=int(input("ENTER YOUR QUANTITY:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice = gst+totalprice
        else:
            print("SORRY YOUR ENTER ITEM IS NOT AVAILABLE:")
    else:
        print("YOU ENTERED A WRONG ITEM")
    inpt=input("DO YOU NEED BILL YES OR NO:")
    if inpt=="yes":
        pass
        if finalprice !=0:
              print(25*"=","SureshBabu Super Market",25*"=")
              print(25*" ","Srikakaulam",25*" ")
              print("Name:-",name,30*" ","Date:-",datetime.now())
              print(75*" ")
              print("Sno",8*" ","items",8*" ","quantity",3*" ","price", )
              for i in range(len(pricelist)):
                  print(i,8* " ",1*" ", ilist[i],12 * " ", qlist[i],9* " ", plist[i],5 * " ")
                  print(75 * "-")
                  print(50 * " ", "totalamount:", "Rs", totalprice)
                  print("gst", 25 * " ", "Rs", gst)
                  print(75 * "-")
                  print(50 * " ", "finalamount:", "Rs", finalprice)
                  print(75 * "-")
                  print(20*" ","This Is Computer Generated Invoice !",20*" ")
                  print(75 * "-")
                  print(20*" ","Thanks for visiting",20* " ")
                  print(75 * "-")



