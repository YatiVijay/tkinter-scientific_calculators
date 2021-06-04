from tkinter import Tk
from tkinter import StringVar,Entry,Button
from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor,sqrt


class calculator:
    def __init__(self):
        window=Tk()
        window.title('Scientific Calculator - YATI')
        window.configure(background="#000000")
        self.string=StringVar()
        window.minsize(435,486)
        window.maxsize(435,486)
        
        entry=Entry(window,fg="#DCDCDC",textvariable=self.string,bd=9,width="66")
        entry.grid(row=0,column=0,columnspan=7,padx=2,pady=15,ipady=14)
        entry.configure(background="#696969")
        entry.focus()
        

        values = ["7","8","9","/","%","del","AC",
                  "4","5","6","*","=",
                  "1","2","3","-","(",")","sqrt",
                  "+/-","0",".","+","min","max","pow",
                  "sin","cos","tan","abs","floor","ceil","pi",
                  "asin","acos","degree","radian","log10","log","e"
                  ]

        text=1
        i=0
        row=1
        col=0
        for t in values:
            padx=10
            pady=10
            if (i%7==0):
                row=(i//7)+1
                col=0
            if t=="+/-":
                btn=Button(window,height=2,width=4,bd=4,padx=padx,pady=pady, text=t ,command=lambda txt=t:self.interchange())
                btn.grid(row=row,column=col,padx=2,pady=1)
                btn.configure(background="#C0C0C0")
            if t=="=":
                btn=Button(window,height=2,width=4,bd=4,padx=70,pady=pady,text=t,command=lambda txt=t:self.equals())
                btn.grid(row=row,column=col,columnspan=3,padx=2,pady=2)
                btn.configure(background="#808080")
                i=i+2
            elif(t=='del'):
                btn=Button(window,height=2,width=4,bd=4,padx=padx,pady=pady, text=t ,command=lambda txt=t:self.delete())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="#F4A460")
            elif(t=='AC'):
                btn=Button(window,height=2,width=4,bd=4,padx=padx,pady=pady,text=t,command=lambda txt=t:self.clearall())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="#D2691E")
            else:
                if t!="+/-":
                    btn=Button(window,height=2,width=4,bd=4,padx=padx,pady=pady,text=t ,command=lambda txt=t:self.addChar(txt))
                    btn.grid(row=row,column=col,padx=1,pady=1)
                    if t in "1234567890.":
                        btn.configure(background="#C0C0C0")
                    else:
                        btn.configure(background="#A9A9A9")

            col=col+1
            i=i+1
        window.mainloop()
    def interchange(self):
        w=self.string.get()
        s=''
        c=0
        if w[-1] in '1234567890':
            for j in w[::-1]:
                if j in '0123456789.':
                    s=j+s
                    c=c+1
                else:
                    break
            w=w[:len(w)-c]
            if s[0]=='0':
                s=s[1:]
            if len(s)==0 and len(w)==0:
                self.string.set('-')
            else:
                self.string.set(w+'(-'+s+')')
        else:
            self.string.set("INVALID INPUT")
        

    def clearall(self):
        self.string.set("")

    def equals(self):
        result=""
        try:
            result=eval(self.string.get())
            self.string.set(result)
        except:
            result="INVALID INPUT"
        self.string.set(result)
        
    def addChar(self,char):
        self.string.set(self.string.get()+(str(char)))
        
    def delete(self):
        self.string.set(self.string.get()[0:-1])
            
calculator()


