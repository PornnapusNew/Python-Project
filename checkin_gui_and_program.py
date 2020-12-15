
import os
#operating systems are a collection of functions that causes the running process to be
#  completely replaced by the program passed as an argument to the function.
import pickle
import sys
import os
from subprocess import call

import tkinter as tk

details_list=[]


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab") #Opens a file for appending in binary mode.
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO) #save()is class below that save info
    pickle.dump(a,f,protocol=2)
    f.close()
    listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
    

    fo=open("recipt.txt","w+") #Opens a file for writing and reading.
    for h in range(0,5): # 5 lines to print out in recipt file
        fo.write(listq[h]+"\r\n") #\r\n is to enter new line in in every program 
    fo.close()
    call(["python", "recipt.py"])
    restart_program() #restart everytime when the latest user check in



u = list()
Small = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Medium = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
Large = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)
ExtraLarge = (41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv) 


class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO



class LOCKER_checkin:


    def __init__(self):
        self.NAME=""
        self.ADDERESS=""
        self.MOBILE=""
        self.DAYS=0
        self.price=0
        self.room=0





        def chk_name():
            while True:

                self.k = str(self.name.get())

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True: #chk that name is string
                    self.NAME=self.k
                    self.Text1.insert(tk.INSERT, "Name has been inputed""\n")
                    break
                else:
                    self.Text1.insert(tk.INSERT, "Invalid input please input a valid name""\n")

                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get()) #self.addr is tk.StringVar() at entry5


                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True:
                    self.ADDERESS=self.g
                    self.Text1.insert(tk.INSERT, "Address has been inputed""\n")
                    break
                else:
                    self.Text1.insert(tk.INSERT, "Invalid input please input a valid address""\n")

                    break

        def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(tk.INSERT, "Mobile number has been inputed""\n")
                    break
                else:
                    self.Text1.insert(tk.INSERT, "Invalid input please input a valid mobile number""\n")
                break

        def chk_day():
            while True:

                self.l = str(self.days.get())

                if self.l.isdigit() == True and len(self.l) != 0:
                    self.DAYS = int(self.l)
                    self.Text1.insert(tk.INSERT, "Days has been inputed""\n")
                    break
                else:
                    self.Text1.insert(tk.INSERT, "Invalid input ""\n")
                    break

        def enter(self):
            self.name = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE
            self.no_of_days = int(self.DAYS)

        def tor(self):

            if self.ch == 1: #small
                self.price = self.price + (150 * self.no_of_days)
                m[0] = 1
            elif self.ch == 2: #medium
                self.price = self.price + (200 * self.no_of_days)
                m[0] = 2
            elif self.ch == 3: #large
                self.price = self.price + (250 * self.no_of_days)
                m[0] = 3
            elif self.ch == 4: #x-tra large
                self.price = self.price + (300 * self.no_of_days)
                m[0] = 4

        def payment_option(self):
            op = self.p
            if op == 1: # By cash
                self.Text1.insert(tk.INSERT, "No discount""\n")
            elif op == 2:# By credit card
                self.price = self.price - ((self.price * 10) / 100)
                self.Text1.insert(tk.INSERT, "10%_discount""\n")

        def bill(self):

            if m[0] == 1:
                a = Small
            elif m[0] == 2:
                a = Medium
            elif m[0] == 3:
                a = Large
            elif m[0] == 4:
                a = ExtraLarge

            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)

                    k = s.room_no
                    G.append(k)
                    continue

            except EOFError:
                pass

            for r in a: #chk the room number if it's already use or not
                if r not in G:
                    self.room = r
                    break
                else:
                    continue
            self.room = r
            f2.close()

            details_list.append(self.name)
            details_list.append(self.address)
            details_list.append(self.mobile_no)
            details_list.append(self.room)
            details_list.append(self.price)




            file_save() #call function 



        def submit_clicked():
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and self.var4.get()==0 and self.var5.get()==1 and self.var6.get()==0:
                self.ch=1
                self.p=2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)


            elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 1
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 2
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() ==0 :
                self.ch = 2
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 3
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 3
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 4
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 4
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            else:
                self.Text1.insert(tk.INSERT, "Invalid choice please input a valid choice""\n")





        root = tk.Tk()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 15 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"


        root.geometry("1069x742")
        root.title("FIND MY LOCKER")
        root.configure(background="#FFD6AA") #BRICK ORANGE
        root.configure(highlightbackground="#FFD6AA")
        root.configure(highlightcolor="black")

        self.Text1 = tk.Text(root) #output at the bottom of gui
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font10)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=tk.WORD)

        self.Frame1 = tk.Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=tk.GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=tk.GROOVE)
        self.Frame1.configure(background="#FEF5D4") #LIGHT YELLOW
        self.Frame1.configure(highlightbackground="#FEF5D4")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=995)

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(background="#FEF5D4")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#FEF5D4")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''YOU CLICKED ON''')
        self.Message1.configure(width=496)

        self.Message2 = tk.Message(self.Frame1)
        self.Message2.place(relx=0.52, rely=0.19, relheight=0.74, relwidth=0.07)
        self.Message2.configure(background="#FEF5D4")
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#FEF5D4")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text=''':''')
        self.Message2.configure(width=66)

        self.Message3 = tk.Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)
        self.Message3.configure(background="#FEF5D4")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#FEF5D4")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''CHECK-IN''')
        self.Message3.configure(width=347)

        self.menubar = tk.Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame2 = tk.Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=tk.GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=tk.GROOVE)
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=995)

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03, height=47, width=289)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''ENTER YOUR NAME''')

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.045, rely=0.29, height=47, width=329)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''ENTER YOUR NUMBER''')



        self.Entry3 = tk.Entry(self.Frame2)
        self.name=tk.StringVar() #obtain value from string
        self.Entry3.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#bfbfbf")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#ffffff")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#e6e6e6")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(textvariable=self.name)


        self.Entry4 = tk.Entry(self.Frame2)
        self.mobile=tk.StringVar()
        self.Entry4.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#bfbfbf")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#ffffff")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#e6e6e6")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(textvariable=self.mobile)


        self.Entry5 = tk.Entry(self.Frame2)
        self.addr = tk.StringVar()
        self.Entry5.place(relx=0.47, rely=0.18,height=34, relwidth=0.43)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#bfbfbf")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#ffffff")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#e6e6e6")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(textvariable=self.addr)

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.045, rely=0.16, height=47, width=334)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''ENTER YOUR ADDRESS''')

        self.Label6 = tk.Label(self.Frame2)
        self.Label6.place(relx=0.32, rely=0.5, height=48, width=296)
        self.Label6.configure(activebackground="#ffffff")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#bfbfbf")
        self.Label6.configure(font=font13)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#ffffff")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''CHOOSE YOUR LOCKER''')

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.3, rely=0.79, height=48, width=300)
        self.Label7.configure(activebackground="#ffffff")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#bfbfbf")
        self.Label7.configure(font=font14)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#ffffff")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''CHOOSE PAYMENT METHOD''')

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.04, relheight=0.1, relwidth=0.05)
        self.Message4.configure(background="#ffffff")
        self.Message4.configure(font=font13)
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#ffffff")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text=''':''')
        self.Message4.configure(width=46)

        self.Message5 = tk.Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.17, relheight=0.12, relwidth=0.03)
        self.Message5.configure(background="#ffffff")
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#ffffff")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text=''':''')
        self.Message5.configure(width=26)

        self.Message6 = tk.Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)
        self.Message6.configure(background="#ffffff")
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#ffffff")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text=''':''')
        self.Message6.configure(width=36)

        self.Checkbutton1 = tk.Checkbutton(self.Frame2)
        self.var1 = tk.IntVar()
        self.Checkbutton1.place(relx=0.15, rely=0.58, relheight=0.17
                , relwidth=0.14)
        self.Checkbutton1.configure(activebackground="#ffffff")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(disabledforeground="#bfbfbf")
        self.Checkbutton1.configure(font=font14)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#ffffff")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=tk.LEFT)
        self.Checkbutton1.configure(text='''SMALL''')
        self.Checkbutton1.configure(variable=self.var1)





        self.Checkbutton2 = tk.Checkbutton(self.Frame2)
        self.var2 = tk.IntVar()
        self.Checkbutton2.place(relx=0.13, rely=0.72, relheight=0.11
                , relwidth=0.21)
        self.Checkbutton2.configure(activebackground="#ffffff")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#ffffff")
        self.Checkbutton2.configure(disabledforeground="#bfbfbf")
        self.Checkbutton2.configure(font=font13)
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#ffffff")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=tk.LEFT)
        self.Checkbutton2.configure(text='''MEDIUM''')
        self.Checkbutton2.configure(variable=self.var2)

        self.Checkbutton3 = tk.Checkbutton(self.Frame2)
        self.var3 = tk.IntVar()
        self.Checkbutton3.place(relx=0.5, rely=0.6, relheight=0.11
                , relwidth=0.16)
        self.Checkbutton3.configure(activebackground="#ffffff")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#ffffff")
        self.Checkbutton3.configure(disabledforeground="#bfbfbf")
        self.Checkbutton3.configure(font=font13)
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#ffffff")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify=tk.LEFT)
        self.Checkbutton3.configure(text='''LARGE''')
        self.Checkbutton3.configure(variable=self.var3)

        self.Checkbutton4 = tk.Checkbutton(self.Frame2)
        self.var4 = tk.IntVar()
        self.Checkbutton4.place(relx=0.52, rely=0.71, relheight=0.11
                , relwidth=0.12)
        self.Checkbutton4.configure(activebackground="#ffffff")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#ffffff")
        self.Checkbutton4.configure(disabledforeground="#bfbfbf")
        self.Checkbutton4.configure(font=font13)
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#ffffff")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify=tk.LEFT)
        self.Checkbutton4.configure(text='''X-TRA''')
        self.Checkbutton4.configure(variable=self.var4)

        self.Checkbutton5 = tk.Checkbutton(self.Frame2)
        self.var5 = tk.IntVar()
        self.Checkbutton5.place(relx=0.485, rely=0.89, relheight=0.1
                                , relwidth=0.4)
        self.Checkbutton5.configure(activebackground="#ffffff")
        self.Checkbutton5.configure(activeforeground="#000000")
        self.Checkbutton5.configure(background="#ffffff")
        self.Checkbutton5.configure(disabledforeground="#bfbfbf")
        self.Checkbutton5.configure(font=font16)
        self.Checkbutton5.configure(foreground="#000000")
        self.Checkbutton5.configure(highlightbackground="#ffffff")
        self.Checkbutton5.configure(highlightcolor="black")
        self.Checkbutton5.configure(justify=tk.LEFT)
        self.Checkbutton5.configure(text='''By credit/debit card 10%_Discount''')
        self.Checkbutton5.configure(variable=self.var5)

        self.Checkbutton6 = tk.Checkbutton(self.Frame2)
        self.var6 = tk.IntVar()
        self.Checkbutton6.place(relx=0.153, rely=0.89, relheight=0.1
                                , relwidth=0.15)
        self.Checkbutton6.configure(activebackground="#ffffff")
        self.Checkbutton6.configure(activeforeground="#000000")
        self.Checkbutton6.configure(background="#ffffff")
        self.Checkbutton6.configure(disabledforeground="#bfbfbf")
        self.Checkbutton6.configure(font=font16)
        self.Checkbutton6.configure(foreground="#000000")
        self.Checkbutton6.configure(highlightbackground="#ffffff")
        self.Checkbutton6.configure(highlightcolor="black")
        self.Checkbutton6.configure(justify=tk.LEFT)
        self.Checkbutton6.configure(text='''By cash''')
        self.Checkbutton6.configure(variable=self.var6)

        self.Message7 = tk.Message(self.Frame2)
        self.Message7.place(relx=0.28, rely=0.46, relheight=0.11, relwidth=0.04)
        self.Message7.configure(background="#ffffff")
        self.Message7.configure(font=font15)
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#ffffff")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(text='''-''')
        self.Message7.configure(width=41)

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground="#98AFC7")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#98AFC7")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=chk_name)

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground="#98AFC7")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#98AFC7")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#ffffff")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=chk_add)

        self.Button3 = tk.Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground="#98AFC7") #Blue Gray
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#98AFC7")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#ffffff")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''OK''')
        self.Button3.configure(command=chk_mo)

        self.Button4 = tk.Button(self.Frame2)
        self.Button4.place(relx=0.76, rely=0.66, height=83, width=156)
        self.Button4.configure(activebackground="#B87333") #Copper
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#B87333")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font16)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''SUBMIT''')
        self.Button4.configure(command=submit_clicked)

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.43, height=44, width=260)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''NUMBER OF DAYS''')


        self.Entry1 = tk.Entry(self.Frame2)
        self.days=tk.StringVar()
        self.Entry1.place(relx=0.47, rely=0.43, height=34, relwidth=0.43)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=424)
        self.Entry1.configure(textvariable=self.days)

        self.Message8 = tk.Message(self.Frame2)
        self.Message8.place(relx=0.42, rely=0.41, relheight=0.11, relwidth=0.03)
        self.Message8.configure(background="#ffffff")
        self.Message8.configure(font=font13)
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#ffffff")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(text=''':''')
        self.Message8.configure(width=26)

        self.Button5 = tk.Button(self.Frame2)
        self.Button5.place(relx=0.91, rely=0.43, height=33, width=43)
        self.Button5.configure(activebackground="#98AFC7")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#98AFC7")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#ffffff")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''OK''')
        self.Button5.configure(command=chk_day)


        root.mainloop()


if __name__ == '__main__':
    hotel=LOCKER_checkin()






