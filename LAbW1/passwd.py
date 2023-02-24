from tkinter import *
from tkinter import ttk
import random
import string
import re
from idlelib.tooltip import Hovertip
import pyperclip

def pwd(root,button):
    global pswdpop
    pswdpop = Toplevel(root)
    pswdpop.geometry('515x350+680+180')
    pswdpop.resizable(False,False)
    pswdpop.config(bg = '#FFF8DC')
    pswdpop.iconbitmap('rand.ico')
    button.config(state='disabled')

    def on_popup_close():
        button.config(state="normal")
        pswdpop.destroy()

    def gen_passwd():
        pwdtext.delete('1.0','end')
        length = random.randint(16,25)
        letters = string.ascii_letters
        digits = string.digits
        punct = string.punctuation

        num_letters = round(length*0.6)
        num_digits = round(length*0.3)
        num_punctuation = length - num_letters -num_digits

        ush_password = ''
        for i in range(num_letters):
            ush_password+=random.choice(letters)
        for i in range(num_digits):
            ush_password+=random.choice(digits)
        for i in range(num_punctuation):
            ush_password+=random.choice(punct)

        password_list = list(ush_password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        pyperclip.copy(password)
        pwdtext.insert(INSERT,password)


    def st_checker():
        upper_pattern = re.compile(r'[A-Z]')
        lower_pattern = re.compile(r'[a-z]')
        digit_pattern = re.compile(r'\d')
        symbol_pattern = re.compile(r'[!@#$%^&*()_+=\[\]{};:\'",.<>/?\\|~-]')
        
        with open('common-passwords.txt','r') as com:
            common = com.read().splitlines()
        password = enter_password.get()
        score = 0
        if len(password) > 8:
            score+=1
        if len(password) > 10:
            score+=1
        if len(password) > 14:
            score+=1
        if len(password) > 16:
            score+=1
        if upper_pattern.search(password):
            score += 2
        if lower_pattern.search(password):
            score += 1
        if digit_pattern.search(password):
            score += 1
        if symbol_pattern.search(password):
            score += 2

        if score < 4:
            if password in common:
                scoresheet.config(text = '0/10', fg='#962E2A')
            
            elif len(password)<=8:
                scoresheet.config(text = '0/10', fg='#962E2A')
            else:    
                scoresheet.config(text = f'{score}/10', fg='#962E2A')

        if 4<=score<7:
            scoresheet.config(text = f'{score}/10', fg='#EDCD44')

        if score >=7:
            scoresheet.config(text = f'{score}/10', fg='#7C8363')


    pwdgenlabel = Label(pswdpop,text='Generate strong password',bg = '#FFF8DC',font=("Times New Roman bold", 30),justify=CENTER)
    pwdgenlabel.pack(pady=20)

    pwdtext = Text(pswdpop,height = 0 ,width = 35 , font=("Times New Roman", 20))
    pwdtext.pack(padx = 15)

    c = ttk.Style()
    c.configure('my.TButton', font=('Helvetica', 12))

    gen_button = ttk.Button(pswdpop, text="Generate",style='my.TButton',command=gen_passwd)
    gen_button.pack(pady = 5,ipady=5, ipadx=15)

    checkerlab = Label(pswdpop,text = 'Check your password strength',bg = '#FFF8DC',font=("Times New Roman bold", 25),justify=CENTER)
    checkerlab.pack(pady=10)

    pswdenter = Label(pswdpop,text = 'Strength level',bg = '#FFF8DC',font=("Times New Roman bold", 15))
    pswdenter.pack(pady=10,padx = 40,anchor=SE)

    enter_password = Entry(pswdpop,width =20 ,font=("Times New Roman", 20))
    enter_password.pack(anchor=SW,padx = 15)
    myTipC = Hovertip(enter_password,'Enter your password to check how strong it is',hover_delay=0)

    scoresheet = Label(pswdpop,text = '0/10',bg = '#FFF8DC',font=("Times New Roman bold", 18))
    scoresheet.place(x = 410 ,y=289)

    check_button = ttk.Button(pswdpop, text="Check",style='my.TButton',command=st_checker)
    check_button.place(width = 65,y = 290,x = 305)

    pswdpop.protocol("WM_DELETE_WINDOW", on_popup_close)

