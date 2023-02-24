from tkinter import *
from tkinter import ttk
from idlelib.tooltip import Hovertip
from OnlyNumber import notnumrestrict
import random
import time
import winsound
import threading

def prngmenu(root,button):
    global rngpop
    rngpop = Toplevel(root)
    rngpop.geometry('515x350+680+180')
    rngpop.resizable(False,False)
    rngpop.config(bg = '#FFF8DC')
    rngpop.iconbitmap('rand.ico')
    button.config(state='disabled')

    def on_popup_close():
        button.config(state="normal")
        rngpop.destroy()

    random.seed(int(time.time()))

    def error_pop_up(errorT):
        global popM
        popM = Toplevel(rngpop)
        popM.title('Error')
        popM.geometry('370x75+752+300')
        popM.iconbitmap('warning.ico')
        popM.resizable(False,False)
        def leave():
            popM.destroy()
        def playw():
            global playwin
            playwin = winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        lebwarn = Label(popM,text=errorT,font=("Times New Roman", 14))
        lebwarn.pack(pady=5,anchor=N)
        gotit = ttk.Button(popM,text='Got it',command=leave)
        gotit.pack(pady=0,anchor=S)
        th = threading.Thread(target = playw,args=[])
        th.start()
    

    def gen_binary():
        try:
            widout.configure(state="normal")
            widout.delete('1.0','end')
            count = int(entrycount.get())
            binary_nums = []
            while count > 0:
                rand = random.randint(0,1)
                binary_nums.append(rand)
                count -=1
            widout.insert(INSERT,binary_nums)
        except:
            error = 'Please fill "Count" field'
            error_pop_up(error)
        finally:
            widout.configure(state="disabled")


    def gen_hex():
        try:
            widout.configure(state="normal")
            widout.delete('1.0','end')
            count = int(entrycount.get())
            hexvals = '0123456789ABCDF'
            hex_list=[]
            while count > 0:
                one_element =''
                el = random.choices(hexvals,k=2)
                for x in el:
                    one_element +=x 
                hex_list.append(one_element)
                count -=1
            widout.insert(INSERT,hex_list)
        except:
            error = 'Please fill "Count" field'
            error_pop_up(error)
        finally:
            widout.configure(state="disabled")


    def rand_nums():
        try:
            widout.configure(state="normal")
            widout.delete('1.0','end')
            min = int(entryfrom.get())
            max = int(entryto.get())
            count = int(entrycount.get())
            numbers =[]
            if (max-min) == 1:
                numlist = [min,max]
                randn = random.randint(min,max)
                numlist.remove(randn)
                while count>0:
                    numbers.append(randn)
                    count -= 1
                    if count == 0:
                        break
                    numbers.append(numlist[0])
                    count -=1
                widout.insert(INSERT,numbers)
            elif (max==min):
                errort = 'Min and Max numbers should not be the same'
                error_pop_up(errort)

            else:            
                try:
                    while count > 0:
                        rand = random.randint(min,max)
                        numbers.append(rand)
                        count -=1
                    widout.insert(INSERT,numbers)
                except:
                    errortext = 'Please enter values in correct order(to>from)'
                    error_pop_up(errortext)
            
        except:
            errort = 'Please fill empty fields'
            error_pop_up(errort)
        finally:
            widout.configure(state="disabled")

            

    def clearText():
        widout.configure(state="normal")
        widout.delete("1.0","end")
        entryto.delete(0, END)
        entryfrom.delete(0, END)
        entrycount.delete(0, END)
        widout.configure(state="disabled")
        
   
    r = ttk.Style()
    r.configure('my.TButton', font=('Helvetica', 12))
    global widout
    f = Frame(rngpop)
    f.place(x=7,y=7)
    scrollbar = Scrollbar(f)
    widout = Text(f , width = 60 ,height = 13,wrap = 'word',yscrollcommand=scrollbar.set)
    scrollbar.config(command=widout.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    widout.configure(state="disabled")
    widout.pack(side="left")
    
    fromlab = Label(rngpop,bg = '#FFF8DC',text = 'From',font =('Times' , 17))
    fromlab.place(x = 20,y = 230)
    entryfrom = Entry(rngpop,width =4,font=("Times New Roman", 14))
    entryfrom.place(x = 80 , y = 233)
    notnumrestrict(entryfrom , rngpop)

    tolab = Label(rngpop,bg = '#FFF8DC' ,text = 'to',font =('Times' , 17))
    tolab.place(x = 130, y = 230)
    entryto = Entry(rngpop,width =4,font=("Times New Roman", 14))
    entryto.place(x = 158 , y = 233)
    notnumrestrict(entryto , rngpop)
    myTipR = Hovertip(entryto,'max value is 9999',hover_delay=0)

    countlab = Label(rngpop,bg = '#FFF8DC' ,text = 'Count',font =('Times' , 17))
    countlab.place(x = 20,y = 270)
    entrycount = Entry(rngpop,width =4,font=("Times New Roman", 14))
    entrycount.place(x = 90 , y = 273)
    notnumrestrict(entrycount , rngpop)
    myTipR = Hovertip(entrycount,'max value is 9999',hover_delay=0)

    clearbtn = ttk.Button(rngpop , text = 'Clear',style='my.TButton',command=clearText)
    clearbtn.pack(ipady=5, ipadx=7,anchor=SW , side= LEFT , pady = 7 ,padx = 15)
    gennumbers = ttk.Button(rngpop,text = 'Generate random numbers',style='my.TButton',command=rand_nums)
    gennumbers.pack(ipady = 10, ipadx=15,anchor=SE,side=RIGHT,pady = 65,padx=10)
    
    genbinary = ttk.Button(rngpop,text = 'Generate binary',command=gen_binary)
    genbinary.place(x = 390,y =300)
    myTipR = Hovertip(genbinary,'Fill "Count" field with number of desired binary values\n and push button to get them',hover_delay=0)

    genhex = ttk.Button(rngpop,text = 'Generate hex',command= gen_hex)
    genhex.place(x=300,y =300)
    myTipR = Hovertip(genhex,'Fill "Count" field with number of desired hex values\n and push button to get them',hover_delay=0)

    rngpop.protocol("WM_DELETE_WINDOW", on_popup_close)


   
    

    




