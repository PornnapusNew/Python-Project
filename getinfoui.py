import os
import pickle

details_list=[]
l2=[]
G = []
def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

import sys

import tkinter as tk


class Information:
    def __init__(self):
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            print(self.gettininfo)
            print("\n")
            if self.gettininfo.isdigit() == True and len(self.gettininfo) != 0:
                self.Text1.insert(tk.INSERT, " Valid locker number ""\n")
            else :
                self.Text1.insert(tk.INSERT,"Invalid locker number""\n")

            try:
                n = 0
                f2 = open("hotel.dat", "rb")
                while True:
                    s = pickle.load(f2)
                    a = str(s.room_no)
                    print (a)
                    if self.gettininfo == a:
                        n = 1
                        print("NAME-", "\t", "\t", s.name)
                        print("\n")
                        print("ADDRESS-", "\t", s.address)
                        print("\n")
                        print("MOBILE NO.-", "  ", s.mobile_no)
                        print("\n")
                        print("THE TOTAL BILL IS ", s.price)
                    elif EOFError:
                        if n == 0:
                            print("NO GUEST IN ROOM ", self.gettininfo)
                        else:
                            n = 0
                            continue
            except EOFError:
                pass
                f2.close()

        root = tk.Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        root.geometry("881x582+249+104")
        root.title("FIND MY LOCKER")
        root.configure(background="#e2b3a3")



        self.Frame1 = tk.Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=tk.GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=tk.GROOVE)
        self.Frame1.configure(background="#eecfbb")
        self.Frame1.configure(width=825)

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font="font10")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=764)
        self.Text1.configure(wrap=tk.WORD)



        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.15, height=48, width=377)
        self.Label1.configure(background="#eecfbb")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ENTER THE LOCKER NO. :''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.gather=tk.StringVar()
        self.Entry1.place(relx=0.65, rely=0.17,height=40, relwidth=0.1)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="font10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=84)
        self.Entry1.configure(textvariable=self.gather)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.39, rely=0.29, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#a3b6c5")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SUBMIT''')
        self.Button1.configure(width=197)
        self.Button1.configure(command=gotinfo)

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
        self.Message1.configure(background="#eecfbb")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''GET INFO HERE ...''')
        self.Message1.configure(width=460)
        root.mainloop()






if __name__ == '__main__':
    GETINFO=Information()
