from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Listbox
from tkinter import IntVar
from tkinter import BooleanVar
from tkinter import Frame

def form(geometry="500x300",title="",is_center=True):
    f=Tk()
    f.geometry(geometry)
    f.title(title)
    if is_center: tkcenter(f)
    return f

def toplevel(geometry="500x300",title="",is_center=True):
    f=Toplevel()
    f.geometry(geometry)
    f.title(title)
    if is_center: tkcenter(f)
    return f

def frame(form,bg=None):
    if bg != None:
        return Frame(form,bg)
    else:
        return Frame(form)
    


def button(form,text="Button",command=None):
     btn = ttk.Button(form,text=text)
     if command != None:
        btn.config(command =command)  
     return btn
def label(form,text="Label"):
    return ttk.Label(form,text=text)

def entry(form):
    txt=ttk.Entry(form)
    return txt

def strVar():
    return StringVar()

def intVar():
    return IntVar()

def doubleVar():
  return DoubleVar()

def booleanVar():
    return BooleanVar()


def textbox(form,variable=None,isnum = False,read_only=False,password =False):
    
    def numberonly(text):
        if str.isdigit(text):
            return True
        elif text == "":
            return True
        else:
            return False
        
    reg_fun =form.register(numberonly)
    txt=ttk.Entry(form)
    if isnum : 
        txt.config(validate="key",validatecommand=(reg_fun,"%P"))
    if variable!=None:
        txt.config(textvariable=variable)
    if read_only ==True:
        txt.config(state="readonly")
    if password ==True:
        txt.cinfig(show="*")
        
    return txt

def radio(form,text="radio",value=0,variable=None):
    rdo=ttk.Radiobutton(form,text=text,value=value)
    if variable !=None:
        rdo.config(variable=variable)
    return rdo

def checkbox(form,text="CheckBox",variable =None):
    cbx =ttk.Checkbutton(form ,text =text)
    if variable != None:
        cbx.config(variable = variable)
    return cbx

def combobox(form,values=None, readonly=False):
    cbx=ttk.Combobox(form)
    if values != None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state="readonly")
    return cbx

def listbox(form,values=None):
    lbx=Listbox(form)
    if values != None:
        i=0
        for x in values:
            lbx.insert(i,x)
            i+=1
    return lbx

def tkcenter(form):
    form.update()
    fw = form.winfo_width()
    fh =form.winfo_height()
    sw =form.winfo_screenwidth()
    sh =form.winfo_screenheight()
    x =(sw-fw) / 2
    y =(sh - fh) / 2 
    form.geometry("%dx%d+%d+%d" %(fw,fh,x,y))

def bgall(form,bg):
    form.update()
    ctrls = form.winfo_children()
    form.config(bg=bg)
    my = ttk.Style()
    my.configure("TCheckbutton",background =bg)
    my.configure("TRadiobutton",background =bg)
    
    for c in ctrls:
        if c.winfo_class() =="Frame" :bgall(c,bg)
        try:
            c["background"]=bg
        except:
            pass
              
def fontall(form,font):
    form.update()
    ctrls = form.winfo_children()
    my =ttk.Style()
    my.configure("TButton",font =font)
    my.configure("TEntry",font =font)
    my.configure("TRadiobutton",font =font)
    my.configure("TCheckbutton",font =font)
    for c in ctrls:
      if c.winfo_class() =="Frame" :fontall(c,font)       
      try:
          c["font"]=font
      except:
           pass
    

def fgall(form,fg):
    form.update()
    ctrls=form.winfo_children()
    my =ttk.Style()
    my.configure("TButton",foreground =fg)
    my.configure("TRadiobutton",foreground =fg)
    my.configure("TCheckbutton",foreground =fg)
    for c in ctrls:
        if c.winfo_class() =="Frame" :fgall(c,fg)
        
        try:
            c["foreground"]=fg
        except:
            pass

def justall(form,just):
    form.update()
    ctrls=form.winfo_children()
    my =ttk.Style()
    my.configure("TButton",justify = just)
    my.configure("TRadiobutton",justify =just)
    my.configure("TCheckbutton",justify =just)
    for c in ctrls:
        if c.winfo_class() =="Frame" :justall(c,just)
        
        try:
            c["justify"]=just
        except:
            pass

def widthall(form,mywidth):
    form.update()
    ctrls=form.winfo_children()
    my =ttk.Style()
    my.configure("TButton",width = mywidth)
    my.configure("TRadiobutton",width =mywidth)
    my.configure("TCheckbutton",width =mywidth)
    for c in ctrls:
        if c.winfo_class() =="Frame" :widthall(c,mywidth)
        
        try:
            c["width"]=mywidth
        except:
            pass

def msgbox(text):
    messagebox.showinfo("",text)
    
def msgask(text):
    return messagebox.askyesno("",text)
def inbox(text):
    f =Toplevel()
    f.title(text)
    f.geometry("400x200")
    f.resizable(False,False)
    tkcenter(f)
    ttk.Label(f,text =text,font ="None 15").pack(pady=10)
    sv =StringVar()
    txt=ttk.Entry(f,font="None 15",width=35,textvariable =sv)
    txt.pack(pady=10 )
    txt.bind("<Return>",lambda my: f.destroy())
    ttk.Style().configure("inbox.TButton",font="None 15")
    ttk.Button(f,text="ok",command =lambda:f.destroy(),style ="inbox.TButton").pack(pady=10)
    txt.focus()
    f.grab_set()
    f.wait_window()
 
    return sv.get()

def inboxnum(text,numberonly=False):
   
    
    #fm=Tk()
    fm=Toplevel()
    fm.geometry("500x300")
    fm.title("ines")
    fm.resizable(False,False)
    tkcenter(fm)
    ttk.Label(fm,text="text",font ="None 15").pack(pady=10)
    sv=StringVar()
    def numberonly(text):
        if str.isdigit(text):
            return True
        elif text == "":
            return True
        else:
            return False
    reg_fun =fm.register(numberonly)
    txt=ttk.Entry(fm,font ="None 15",textvariable=sv)
    if numberonly: 
        txt.config(validate="key",validatecommand=(reg_fun,"%P"))
    txt.pack(pady=10)
    txt.bind("<Return>",lambda my:f.destroy())
    ttk.Style().configure("inboxTButton",font ="None 15")
    ttk.Button(fm,text="ok",command=lambda:fm.destroy(),style="inbox.TButton").pack()
    
    fm.grab_set()
    txt.focus()
    fm.wait_window()
    return sv.get()


def combine_funcs(*funcs):
    def combined_func(*args,**kwargs):
        for f in funcs:
            f(*args, **kwargs)

            
    return combined_func


class table:
    tbl = None
    columns = None
    rows = None
    table_index = -1
    all_labels = []
    selected_rows = []

    def __init__(this, form, columns, rows):
        this.tbl = Frame(form)
        this.columns = columns
        this.rows = rows

    def columns_count(this):
        return len(this.columns) - 1

    def rows_count(this):
        return len(this.rows)

    def get_index(this):
        return this.table_index

    def get_row(this):
        this.all_labels[this.table_index]

   def bind(this):
        r = len(this.rows)
        c = len(this.columns)
        this.columns.insert(0, "...")
        colcount = 0
        for col in this.columns:
            lbl = label(this.tbl, col)
            lbl.config(borderwidth=2, relief="solid")
            lbl.grid(row=0, column=colcount, sticky="nsew")
            colcount += 1

        lbx = listbox(this.tbl)
        lbx.grid(row=1, column=0, rowspan=r, sticky="nsew")

        for x in range(r):
            lbx.insert(END, f"{this.rows[x][0]} - {this.rows[x][1]}")

        def select_row(event):
            index = lbx.curselection()[0]
            clear_lbl()
            mark_lbl(this.all_labels[index], index)

        lbx.bind("<<ListboxSelect>>", select_row)

        for x in range(r):
            lbls = []
            for y in range(c):
                lbl = label(this.tbl, str(this.rows[x][y]))
                lbl.config(borderwidth=2, relief="solid")
                lbl.grid(row=x + 1, column=y + 1, sticky="nsew")
                lbls.append(lbl)

            this.all_labels.append(lbls)

        def clear_lbl():
            for lbl in this.all_labels:
                for lbl2 in lbl:
                    lbl2.config(background=this.tbl["background"])

        def mark_lbl(labels, index):
            this.table_index = index
            for lb in labels:
                lb.config(background="#e1e1e1")

        this.tbl.pack()
  
