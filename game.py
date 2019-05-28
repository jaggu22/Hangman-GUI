import tkinter as tk
from random import randint
from time import sleep
#from PIL import Image,ImageTk

LARGE_FONT= ("Verdana", 12)
name=""
difficulty=""
#----------------derived class from base class tkinter---------------
class Base(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.geometry("480x480")
        
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, SelectorPage, GamePage):

            frame = F(container, self)
            frame.configure(background="Peru")
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont,n='',d='',c=''):
        if(len(n)):
         self.frames[cont].labeln.configure(text=n)
         self.frames[cont].name=n
        if(len(d)):
         self.frames[cont].labeld.configure(text=d)
         self.frames[cont].difficulty=d
        if(len(c)):
         d=self.frames[cont].fetchdata("/root/project150917/data.txt")
         self.frames[cont].d=d[d[0][c]]
         self.frames[cont].start_game()
        frame = self.frames[cont]
        frame.tkraise()


#--------------------home page-----------------------------       
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)  
        label = tk.Label(self, text="HANGMAN", font=('times',65),bg="Light Goldenrod Yellow")
        label.pack(pady=10,padx=10)
        label1=tk.Label(self,text="\n\n",bg="Peru")
        label1.pack()
        k=tk.Label(self,text="ENTER YOUR NAME",font=('times',15))
        k.pack()
        label1=tk.Label(self,text="\n",bg="Peru")
        label1.pack()
        e=tk.Entry(self)
        e.pack()
        label1=tk.Label(self,text="\n",bg="Peru")
        label1.pack()
        button = tk.Button(self, text="SUBMIT",
                            command=lambda: controller.show_frame(SelectorPage,e.get()))
        button.pack()
#-----------------------------------selector page-------------------------
class SelectorPage(tk.Frame):

    def __init__(self, parent, controller):
        self.name=""
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HANGMAN", font=('times',65),bg="Light Goldenrod Yellow")
        label.pack(pady=10,padx=10)
        self.labeln = tk.Label(self, text="NO NAME ENTERED", font=LARGE_FONT)
        self.labeln.pack(pady=10,padx=10)
        label1=tk.Label(self,text="\n",bg="Peru")
        label1.pack()
        a=tk.Label(self,text="Select the level :",font=LARGE_FONT)
        a.pack()
        variable = tk.StringVar(self)
        variable.set("MEDIUM") # default value
        label1=tk.Label(self,text="",bg="Peru")
        label1.pack()
        e1=tk.OptionMenu(self,variable,"EASY","MEDIUM","HARD")
        e1.place(x=303,y=205)
        label1=tk.Label(self,text="\n",bg="Peru")
        label1.pack()
        variable1 = tk.StringVar(self)
        variable1.set("STATES&CITIES") # default value
        label1=tk.Label(self,text="Select the categories",font=('times',10))
        label1.pack()
        cat=tk.OptionMenu(self,variable1,"STATES&CITIES","MOVIENAMES","ANIMALS")
        cat.pack()
        label1=tk.Label(self,text="\n\n\n",bg="Peru")
        label1.pack()
        button2 = tk.Button(self, text="START GAME",
                command=lambda: controller.show_frame(GamePage,self.name,variable.get(),variable1.get()))
        button2.pack(side="bottom")

#-----------------------game page------------------------------------------------------
class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        self.name=""
        self.level=1
        self.d={}
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HANGMAN", font=('times',65),bg="Light Goldenrod Yellow")
        label.pack(pady=10,padx=10)
        self.labeln = tk.Label(self, text="NO NAME ENTERED", font=('times',10))
        self.labeln.pack(anchor="nw",padx=10)
        self.labeld = tk.Label(self, text="", font=('times',10))
        self.labeld.place(x=200,y=131)
        score=tk.Label(self,text="SCORE",font=('times',10))
        score.place(x=10,y=160)
        self.s1=tk.Label(self,text="")
        self.s1.place(x=55,y=160)
        labelx=tk.Label(self,text="LEVEL",font=('times',10))
        labelx.place(x=350,y=131)
        self.level_lab=tk.Label(self,text="1")
        self.level_lab.place(x=397,y=131)
        label1=tk.Label(self,text="\n",bg="Peru")
        label1.pack()
        k=tk.Label(self,text="  ENTER GUESS  ",font=('times',10))
        k.pack(anchor="center")
        #label1=tk.Label(self,text="\n",bg="Peru")
        #label1.pack()
        e2=tk.Entry(self)
        e2.place(x=157,y=220)
        #label1=tk.Label(self,text="\n",bg="Peru")
        #label1.pack()
        k1=tk.Button(self,text="SUBMIT",font=('times',10),command=lambda :self.check(e2.get()))
        k1.place(x=320,y=220)
        k1.config(width=5)
        word=tk.Label(self,text="  WORD  : ",font=('times',10))
        word.place(x=157,y=300)
        self.w1=tk.Label(self,text="")
        self.w1.place(x=207,y=300)
        self.s=tk.Label(self,text="TRIALS REMAINING:",font=('times',10))
        self.s.place(x=157,y=350)
        self.j=tk.Label(self,text="",font=('times',20),bg="Peru")
        self.j.place(x=1,y=400)
        #al=tk.Label(self)
        #al.place(x=290,y=350)
        hint=tk.Label(self,text=" HINT :",font=('times',10))
        hint.place(y=245)
        self.k2=tk.Label(self,text="",font=('times',10))
        self.k2.place(x=1,y=245)


       # button2 = tk.Button(self, text="Page One",
                        #    command=lambda: controller.show_frame(SelectorPage))
       # button2.pack()
        
        button1 = tk.Button(self, text="QUIT",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(side="bottom")
        
    def fetchdata(self,fo):
        """RETURNS A LIST WITH DICTINORIES OF NAMES AND HINTS
           ZEROTH DICT SERVES AS INDEX TO OTHER DICTS"""
        l=[{}]
        j=0
        f=open(fo,"r")
        for i in f:
            if(i[0]=='@'):
                j+=1
                k=i[1:-1]
                l[0][k]=j
                l.append({})
            elif(i[0]=='~'):
                key=i[1:-1]
                l[j][key]=[]
            else:
                l[j][key].append(i[0:-1])
        for i in l[0]:
            for j in l[l[0][i]]:
                l[l[0][i]][j].reverse()
        f.close()
        return(l)
#-------------------------------------------fetching data-----------------------

    def start_game(self):
        level=self.level
        self.word=list(self.d.keys())
        self.word=self.word[randint(0,len(self.word)-1)]
        self.n=len(self.word)
        self.w1.configure(text='_ '*self.n)
        self.n=round(self.n/level)+2
        self.a=self.n
        self.hints=self.d[self.word]
        self.guessed=""
        self.s.configure(text="Trials Remaining: "+str(self.a-1))
        score=round(len(self.word)**2*self.a/self.n)      
        self.s1.configure(text=str(score))
        self.k2.configure(text="")


    def check(self,entry):
        a=self.a
        word=self.word
        if(a<7 and a!=self.n and a!=2):
            self.k2.configure(text=self.hints.pop())
        entry=entry[:len(word)]
        self.a=a-1
        a-=1
        score=round(len(word)**2*a/self.n)      
        self.s1.configure(text=str(score))
        if(a==1 or entry==word):
            if(entry!=word):
                score=0
            if(score):
             self.j.configure(text="YOU WON.lET`S GO TO NEXT LEVEL")
             self.level+=1
            else:
             self.j.configure(text="YOU LOST.LET`S TRY AGAIN")
            self.judge(score)
            self.start_game()
            self.level_lab.configure(text=str(self.level))
            return 0
        d=False
        for i in entry:
            if(i in word and i not in self.guessed):
                self.guessed+=i
                d=True
        w1=""
        for i in word:
            if(i in self.guessed):
                w1+=i
            else: 
                w1+='_ '
        self.s.configure(text="Trials Remaining: "+str(a-1))
        self.w1.configure(text=w1)

#-------------------------------main----------------------------------------------
app = Base()
app.mainloop()
