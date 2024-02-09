from mysqldb import *
from tools import *

def create_table():
    is_create=dbrun("""
      CREATE TABLE IF NOT EXISTS ITEAM_EBAY(
        item_id int primary key,
        items_name varchar(99),
        purchase_price DOUBLE,
        items_price DOUBLE ,
        quantity int ,
        sold varchar(99)
        )
""")
    if is_create:msgbox("table is created")                    
    


bg ="light blue"
fg ="navy"
ft = "verdana 16"
pad =3
frm =form("800x600","ebay report")

button(frm,"create table",create_table).pack(pady=pad)

itemId_var    = intVar()
itemname_var  = strVar()
quantity_var   = intVar()
purchase_price_var    = doubleVar()
selling_price_var    = doubleVar()
sold_var       = strVar()

def check_item():
    if frm.winfo_children()[2].get().strip()=="":
        msgbox("Item ID is Empty..!")
        frm.winfo_children()[2].focus()
        return False
    elif itemname_var.get().strip()=="":
        msgbox("item name is empty!")
        frm.winfo_children()[4].focus()
        return False
    elif frm.winfo_children()[6].get().strip() == "":
        msgbox("the purchase price is Empty..!")
        frm.winfo_children()[6].focus()
        return False
    elif frm.winfo_children()[8].get().strip() == "":
        msgbox("the selling price is Empty..!")
        frm.winfo_children()[8].focus()
        return False
    elif sold_var.get().strip() =="":
        msgbox("can you cinfirm if is sold or nn")
        frm.winfo_children()[10].focus()
        return False
    else:
        return True
    
    
def clear_item():
    
    itemId_var.set(dbautonum("ITEAM_EBAY","item_id"))
    itemname_var.set("")
    quantity_var.set("")
    purchase_price_var.set("")
    selling_price_var.set("")
    sold_var.set("")
    frm.winfo_children()[13].config(state="enable")
    frm.winfo_children()[14].config(state="enable")
    frm.winfo_children()[15].config(state="disable")
    frm.winfo_children()[16].config(state="disable")
    frm.winfo_children()[4].focus()
def add_item():
    if check_item():
       is_add = dbrun("insert into ITEAM_EBAY values(%d,'%s',%d,%0.2f,%0.2f,'%s')" % ( itemId_var.get(),itemname_var.get(),quantity_var.get(),purchase_price_var.get(),selling_price_var.get(),sold_var.get() ))
       if is_add:msgbox("item is added...!")
       clear_item()
   
def find_item():
    enum= inbox("Enter item id")
    if enum =="": enum=0
    rows = dbget("select * from ITEAM_EBAY where item_id  ="+str(enum))
    if len(rows) <1:
        msgbox("Item not found...!")
    else:
         row=rows[0]
         itemId_var.set(row[0])
         itemname_var.set(row[1])
         quantity_var.set(row[2])
         purchase_price_var.set(row[3])
         selling_price_var.set(row[4])
         sold_var.set(row[5])
         frm.winfo_children()[13].config(state="disable")
         frm.winfo_children()[15].config(state="enable")
         frm.winfo_children()[16].config(state="enable")
def edit_item():
    if check_itm():
        is_edit=dbrun("update ITEAM_EBAY set item_id='"+str(itemId_var.get())+"',items_name='"+itemname_var.get()+"',purchase_price='"+str(purchase_price_var.get())+"',items_price='"+str(selling_price_var.get())+"',quantity='"+str(quantity_var.get())+"',sold ='"+sold_var.get()+"' WHERE item_id="+str(itemId_var.get()))     
        if is_edit: msgbox("Employee is edited...")
        clear_item()
    
def del_item():
    if msgask("do you want to delete the item...!"):
        is_del = dbrun("delete from ITEAM_EBAY where item_id=" +str(itemId_var.get()))
        if is_del:msgbox("employee is deleted......")
        clear_item()
       
label(frm,"item_id").pack()
textbox(frm,itemId_var,True).pack(pady=pad)
itemId_var.set(dbautonum("ITEAM_EBAY","item_id"))

label(frm,"item_name").pack()
textbox(frm,itemname_var).pack(pady=pad)

label(frm,"purchase_price").pack()
textbox(frm,purchase_price_var).pack(pady=pad)

label(frm,"selling_price").pack()
textbox(frm,selling_price_var).pack(pady=pad)

label(frm,"quantity").pack()
textbox(frm,quantity_var,True).pack(pady=pad)

label(frm,"sold").pack()
textbox(frm,sold_var).pack(pady=pad)

button(frm,"Add item",add_item).pack(pady=pad)
button(frm,"Find item",find_item).pack(pady=pad)
button(frm,"Edit item",edit_item).pack(pady=pad)
button(frm,"Delete item",del_item).pack(pady=pad)
button(frm,"Clear fields",clear_item).pack(pady=pad)
button(frm,"Exit",lambda:frm.destroy).pack(pady=pad)
                           


tkcenter(frm)
bgall(frm,bg)
fgall(frm,fg)
fontall(frm,ft)
justall(frm,"center")
widthall(frm,30)

clear_item()

frm.mainloop
