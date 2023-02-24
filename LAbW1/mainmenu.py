from tkinter import *
from tkinter import ttk       
from idlelib.tooltip import Hovertip
from prng import prngmenu
from passwd import pwd
from hashing import hsh

def prng():
    prngmenu(root,rng_button)
def password(): 
    pwd(root,pswd_button)
def hashing():
    hsh(root,hash_button)


root = Tk()
root.geometry('765x300+550+150')
root.config(bg = '#FFF8DC')
root.title('Gensome')
root.iconbitmap('rand.ico')
root.resizable(False,False)

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 12))

welcome = Label(root,text='WELCOME TO GENSOME',bg = '#FFF8DC',font=("Times New Roman bold", 40),justify=CENTER)
welcome.pack(pady=50)

action = Label(root,text = 'What would you like to do?',bg ='#FFF8DC',font=("Times New Roman bold", 20),justify=CENTER)
action.place(x = 210 ,y = 130)

rng_button = ttk.Button(root,text="PRNG",style='my.TButton', command=prng)
rng_button.pack(side = LEFT ,padx = 50,ipady=15, ipadx=15)
myTip = Hovertip(rng_button,'Random Number Generator:\nGenerates you random numbers in range u specified\nAlso can generate u binary and hexademical formats.'
                 ,hover_delay=0)

pswd_button = ttk.Button(root,text="Generate/check password", style='my.TButton',command=password)
pswd_button.pack(side =LEFT,padx = 40 ,ipady = 15 ,ipadx = 15 )
myTip = Hovertip(pswd_button,'Generates you strong password or \n u can check how strong your password is.',hover_delay=0)

hash_button = ttk.Button(root, text="Hashing",style='my.TButton', command=hashing)
hash_button.pack(side=LEFT, padx = 50,ipady=15, ipadx=15)
myTip = Hovertip(hash_button,'Choose type of hash function and get hash of what you need.',hover_delay=0)


root.mainloop()