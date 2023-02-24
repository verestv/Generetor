from tkinter import *
from tkinter import ttk
import hashlib
import winsound
import threading


def hsh(root,button):
    global hpop
    hpop = Toplevel(root)
    hpop.geometry('515x350+680+180')
    hpop.resizable(False,False)
    hpop.config(bg = '#FFF8DC')
    hpop.iconbitmap('rand.ico')

    button.config(state='disabled')

    def on_popup_close():
        button.config(state="normal")
        hpop.destroy()


    c = ttk.Style()
    c.configure('TMenubutton', font=('Helvetica', 12))


    def error_pop_up(errorT):
        global popM
        popM = Toplevel(hpop)
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


    def getHash():
        try:
            hashtext.delete('1.0','end')
            path = path_entry.get()
            hash_type = hashes.get()
            if hash_type == 'md5':
                hsh = hashlib.md5()
            if hash_type == 'sha1':
                hsh = hashlib.sha1()
            if hash_type == 'sha224':
                hsh = hashlib.sha224()
            if hash_type == 'sha256':
                hsh = hashlib.sha256()
            if hash_type == 'sha384':
                hsh = hashlib.sha384()
            if hash_type == 'sha512':
                hsh = hashlib.sha512()
            else:
                pass
            with open(path,'rb') as file:
                hash = file.read()
                hsh.update(hash)
                hashtext.insert(INSERT,hsh.hexdigest())
        except:
            error = 'Incorrect path or this type of file is not supported'
            error_pop_up(error)
    
        
    hash_types = ['sha256','md5','sha1','sha224','sha256','sha384','sha512']
    hashes = StringVar()
    hashes.set(hash_types[0])

    dropH = ttk.OptionMenu(hpop,hashes,*hash_types,style='TMenubutton')
    dropH.pack(anchor = NW,padx = 7 , pady = 25,ipady = 3,ipadx = 20)

    hash_type_label = Label(hpop,text = 'Hash type',bg = '#FFF8DC',font=("Times New Roman bold", 12))
    hash_type_label.place(x = 28 , y = 0)

    path_entry = Entry(hpop,width =41  ,font=("Times New Roman", 18))
    path_entry.pack(anchor=N , pady = 20)

    path_label = Label(hpop , text= 'Enter full path to the file',bg = '#FFF8DC',font=("Times New Roman", 18))
    path_label.place(x =132 , y = 68)

    gethashbtn = ttk.Button(hpop ,text= 'Get the hash',style='my.TButton',command=getHash)
    gethashbtn.pack(anchor=N,ipadx=10 ,ipady=8)

    hashtext = Text(hpop ,width = 49 , height=3 , font=("Times New Roman", 15))
    hashtext.pack(anchor = N ,pady = 20)

    hpop.protocol("WM_DELETE_WINDOW", on_popup_close)

    

