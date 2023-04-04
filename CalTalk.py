from tkinter import *
import speech_recognition as sr
import re
from fractions import Fraction  
import math
from pint import*
import tkinter as tk




def help():
    root.withdraw()
    top=Toplevel()
    top.title("Help")
    top.geometry("320x410+350+100")
    top.minsize(width=320, height=410)
    top.maxsize(width=320, height=410)
    top.lift()
    top.attributes("-topmost",True)
    global val
    val=StringVar()
    
    
    help_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
    help_text.pack()
    help_text.insert(INSERT,"How to use:\n"
                     "Step 1. Click on Tap to Speak.\n"
                     "Step 2. Instructions to use.\n"

                    "\nTo calculate addition(+) speak plus.\n"
                    "like to do 8+1, say: eight plus one.\n"

                     
                    "\nTo calculate  subtraction(-) speak minus.\n"
                     "like to do 8-1, say: eight minus one.\n"
                     
                     "\nTo calculate multiplication(*) speak multiplied by.\n"
                     "like to say: six multiplied by three.\n"
                     
                     "\nTo calculate division(/) speak divided by.\n"
                     
                     "like to do 7/3 say: seven divided by three.\n"
                     
                     "\nStep 4. Tap on speaker to hear the result.\n"

                      "For better result use microphone."


                     )
    help_text.config(state=DISABLED)





def about():
    top=Toplevel()
    top.title("About")
    top.geometry("320x410+350+100")
    top.minsize(width=320, height=410)
    top.maxsize(width=320, height=410)
    top.lift()
    top.attributes("-topmost",True)
    global val
    val=StringVar()
    
    
    abt_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
    abt_text.pack()
    abt_text.insert(INSERT,

                       "Voice Calculator is very amusing desktop applications and voice activated calculator is most running applications.\n"
                        "\nCalculator is basic need of life most probably for working people, for students of engineering,teachers, for clerical work and for other such purposes like carpenteron shops markets fast calculation is done on daily basis.\n\n"
                        "So for all calculator users, this best voice calculator free is a finest fast calculator.\n"
                        "Now you just have to speak and voice online calculator will automatically calculate what you say"
                        "You can perform simple as well as complicated calculation by just speaking and talking calculator."
                        )
    
    abt_text.config(state=DISABLED)
    
    


    

            
    
def yes(*args):
    #code for Voice calculator
    #start->
      
    def voicecal():
        
        
        root.withdraw()
        def cal():
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_thresold=1
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=5)
                print('speak')
                audio=r.listen(source)
                try:
                    text=r.recognize_google(audio)
                    try:
                       x = re.sub('addition', "+", text)
                       x1 = re.sub('substraction', "-", x)
                       x2 = re.sub('into', "*", x1)
                       
                       x3 = re.sub('divide', "/", x2)
                       print (x3)
                       x4=eval(x3)
                       print (x4)
                       #from gtts import gTTS

                       val1.set(x3)
                       val2.set(str(x4))
                      # from playsound import playsound
                       #import random
                       #import os

                        #creating a super random named file

                       #r1 = random.randint(1,10000000)
                       #r2 = random.randint(1,10000000)

                       #randfile = str(r2)+"randomtext"+str(r1) +".mp3"

                       #tts = gTTS(str(x4), lang='en', slow=True)
                       #tts.save(randfile)
                       #playsound(randfile)

                       #print(randfile)
                       #os.remove(randfile)
                                               
                       
                       
                       

                       
                       

                       
                       
                    except ValueError:
                        val1.set("ValueError")
                        print("ValueError")
                    except Exception as e:
                        val1.set("SomeError")
                        print(e)
                         
                except Exception as e:
                    val1.set("SayAgain")
                    print(e)
                    

        global vc            
        vc=Toplevel()
        vc.title('Voice Calculator')
        vc.geometry("320x410+350+100")
        vc.minsize(width=320, height=410)
        vc.maxsize(width=320, height=410)
        vc.attributes("-topmost",True)
        def key1():
            
            vc.withdraw()
            yes()

        frame1=Frame(vc,width=320,height=200,bd=3,relief="raise",bg="silver")
        frame1.pack(side=TOP)
        frame2=Frame(vc,width=280,height=350,bd=3,relief="raise")
        frame2.pack(side=TOP)
        
        
        
        l=Label(frame1, text=" CalTalk! ",font=('arial',45,'bold'))
        l.grid(row=0,column=0)
        val1=StringVar()
        l=Label(frame2, text=" Input ",font=('arial',15,'bold'),width=15,height=1)
        l.place(x=30,y=0)

        entry11=Entry(frame2,font=('arial',15,'bold'),bd=3, width=24,textvariable=val1)
        entry11.place(x=2,y=30)
        #,relief='groove',bd=4,width=12,height=4,padx=10,pady=10,
        l=Label(frame2, text=" Output ",font=('arial',15,'bold'),width=15,height=1)
        l.place(x=30,y=60)
        val2=StringVar()
        entry2=Entry(frame2,font=('arial',15,'bold'),bd=3, width=24,textvariable=val2)
        entry2.place(x=2,y=90)
        helpp=Button(frame2,text="About",font=('arial',10,'bold'),relief='groove',bd=5, width=11
                     ,height=3,padx=10,pady=10)
        helpp.place(x=10,y=220)
        helpp1=Button(frame2,text="Back",font=('arial',10,'bold'),relief='groove',bd=5, width=11,height=3,padx=10,pady=10,command=key1)
        helpp1.place(x=145,y=220)   
        
        btn_voicecal=Button(frame2,text="Speak!",font=('arial',10,'bold'),width=20,height=2,relief='raise',command=cal,bd=5)
        btn_voicecal.place(x=40,y=150)


    
    h.withdraw()
    root=Tk()
    root.title("CalTalk!")
    root.geometry("320x410+350+100")
    root.minsize(width=320, height=410)
    root.maxsize(width=320, height=410)
    root.attributes("-topmost",True)

    def about():
        root.withdraw()
        top=Toplevel()
        top.title("About")
        top.geometry("320x410+350+100")
        top.minsize(width=320, height=410)
        top.maxsize(width=320, height=410)
        top.lift()
        top.attributes("-topmost",True)
        global val
        val=StringVar()
        
        
        abt_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
        abt_text.pack()
        abt_text.insert(INSERT,

                           "Voice Calculator is very amusing desktop applications and voice activated calculator is most running applications.\n"
                            "\nCalculator is basic need of life most probably for working people, for students of engineering,teachers, for clerical work and for other such purposes like carpenteron shops markets fast calculation is done on daily basis.\n\n"
                            "So for all calculator users, this best voice calculator free is a finest fast calculator.\n"
                            "Now you just have to speak and voice online calculator will automatically calculate what you say"
                            "You can perform simple as well as complicated calculation by just speaking and talking calculator."
                            )
        
        abt_text.config(state=DISABLED)
    



    def help1():
       r=Tk()
       r.title('Help')
       
       r.geometry("320x410+350+100")
       r.minsize(width=320, height=410)
       r.maxsize(width=320, height=410)
       r.attributes("-topmost",True)
       he=Label(r,text='Thanks for using CalTalk!',font=('comic sense',12,'bold'))
       he.grid(row=0,column=0)
       he1=Label(r,text='Administrative Team',font=('comic sense',12),width=30,height=4)
       he1.grid(row=1,column=0)
       
       but=Button(r,text="ok",height=2,width=10,relief='groove')
       but.grid(row=4,column=1)
    def unitconverter():
       root.withdraw()
       def temp1():
               ns.withdraw()
               
               
               x=UnitRegistry()


               p=Tk()
               
               p.attributes("-topmost",True)




               #voice input
               
               def cal():
                   vall.set("")
                   sr.Microphone(device_index=1)
                   
                   r=sr.Recognizer()

                   r.energy_thresold=1000
                   with sr.Microphone() as source:
                       
                       r.adjust_for_ambient_noise(source, duration=5)
                       print("speak")
                       vall.set("Speak")
                       print("Bol")
                       audio=r.listen(source)
                       
                       try:
                           
                           text=r.recognize_google(audio)
                           
                           try:
                               text=int(text)
                               if(type(text)==int):    
                                   print(text)
                                   vall.set(text)
                           except ValueError:
                              vall.set("enter valid")
                           except:
                              vall.set(" some error")           
                       except:
                           vall.set('say again')

               #voice button

               vocal=Button(p,text="Speak!",font=('arial',10,'bold'),width=10,height=1,command=cal)
               vocal.place(x=200,y=150)

               #all funtion
               def clear():
                    vall.set("")
                    val.set("")

               def fun1():
                   pass


               def change10(*args):
                   try:
                
               #For meterc
                       if(var.get()=='Celsius'and var2.get()=='Fahrenheit'):
                           a=int(vall.get())
                           
                           f = (a * 9 / 5) + 32
                           val.set(str(f))
                           
                       if(var.get()=='Celsius'and var2.get()=='Kelvin'):
                           a=int(vall.get())
                           k = float(a + 273.15)
                           val.set(str(k))
                       if(var.get()=='Celcious'and var2.get()=='Celsius'):
                           a=(vall.get())
                           val.set(a)
                       if(var.get()=='Fahrenheit'and var2.get()=='Celsius'):
                           a=int(vall.get())
                           c = float((a - 32) * 5 / 9)
                           val.set(str(c))
                       if(var.get()=='Fahrenheit'and var2.get()=='Kelvin'):
                           a=int(vall.get())
                           k = a + 273
                           val.set(str(k))
                   #For Centimeter
                       if(var.get()=='Fahrenheit'and var2.get()=='Fahrenheit'):
                           a=(vall.get())
                           val.set(a)
                       if(var.get()=='Kelvin'and var2.get()=='Celsius'):
                           a=int(vall.get())
                           c = float(a - 273.15)
                   
                           val.set(str(c))
                       if(var.get()=='Kelvin'and var2.get()=='Fahrenheit'):
                           a=int(vall.get())
                           f = float((a - 273.15) * 1.8000 + 32.00)
                           val.set(str(f))
                       if(var.get()=='Kelvin'and var2.get()=='Kelvin'):
                           a=(vall.get())
                           val.set(a)
                   except ValueError:
                       val.set("Enter Valid Number")
                       vall.set("")
                       
               def click(key):
                   global memory
                   if key == '=':
                       # avoid division by integer
                       if '/' in entry.get() and '.' not in entry.get():
                           entry.insert(tk.END, ".0")
                       # guard against the bad guys abusing eval()
                       str1 = "-+0123456789."
                       if entry.get()[0] not in str1:
                           entry.set(END, "first char not in " + str1)
                       # here comes the calculation part
                       try:
                           result = eval(entry.get())
                           entry.insert(END, " = " + str(result))
                       except:
                           entry.insert(END, "--> Error!")
                   elif key == 'C':
                       entry.delete(0, END)  # clear entry
                   elif key == '->M':
                       memory = entry.get()
                       # extract the result
                       if '=' in memory:
                           ix = memory.find('=')
                           memory = memory[ix+2:]
                       root.title('M=' + memory)
                   elif key == 'M->':
                       entry.insert(END, memory)
                   elif key == 'neg':
                       if '=' in entry.get():
                           entry.delete(0, END)
                       try:
                           if entry.get()[0] == '-':
                               entry.delete(0)
                           else:
                               entry.insert(0, '-')
                       except IndexError:
                           pass
                   else:
                       # previous calculation has been done, clear entry
                       if '=' in entry.get():
                           entry.delete(0, END)
                       entry.insert(END, key)
                   






               p.geometry("320x410+350+100")
               p.title("Temprature Converter")
               p.minsize(width=320, height=410)
               p.maxsize(width=320, height=410)
               vall=StringVar(p)

               val=StringVar(p)
               entry = Entry(p, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=vall)
               entry.place(x=14,y=0)
               entry1 = Entry(p, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=val)
               entry1.place(x=14,y=70)
               OPTIONS={"Celsius", "Fahrenheit", "Kelvin"}
               var=StringVar(p)
               var.set("Celsius")
               var2=StringVar(p)
               var2.set("Celsius")

               btn_list = [
               '7',  '8',  '9',  
               '4',  '5',  '6',  
               '1',  '2',  '3', 
               '0',  '.',   ]
               # create all buttons with a loop
               r = 18
               c = 190
               for b in btn_list:
                   rel = 'ridge'
                   cmd = lambda x=b: click(x)
                   Button(p,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                   r += 93
                   if r >=279:
                       r = 18
                       c =c+50




               def bck():
                   p.withdraw()
                   unitconverter()
                   


               menu=OptionMenu(p,var,*OPTIONS)
               menu.place(x=114,y=35)
               menu1=OptionMenu(p,var2,*OPTIONS)
               menu1.place(x=114,y=110)
               cal=Button(p,text="Calculate",font=('arial',10,'bold'),width=10,height=1,command=change10)
               cal.place(x=107,y=150)

               back=Button(p,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=bck)
               back.place(x=203,y=340)  

               clear=Button(p,text="Clear",font=('arial',10,'bold'),width=10,height=1,command=clear)
               clear.place(x=14,y=150)
               p.mainloop()
               
   

           
       def confun():
           ns.withdraw()
           yes()

       global ns
       ns=Tk()
       ns.title("Converters")


       def about():
                     ns.withdraw()
                     top=Toplevel()
                     top.title("About")
                     top.geometry("320x410+350+100")
                     top.minsize(width=320, height=410)
                     top.maxsize(width=320, height=410)
                     top.lift()
                     top.attributes("-topmost",True)
                     global val
                     val=StringVar()
                    
                    
                     abt_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
                     abt_text.pack()
                     abt_text.insert(INSERT,

                                       "Voice Calculator is very amusing desktop applications and voice activated calculator is most running applications.\n"
                                        "\nCalculator is basic need of life most probably for working people, for students of engineering,teachers, for clerical work and for other such purposes like carpenteron shops markets fast calculation is done on daily basis.\n\n"
                                        "So for all calculator users, this best voice calculator free is a finest fast calculator.\n"
                                        "Now you just have to speak and voice online calculator will automatically calculate what you say"
                                        "You can perform simple as well as complicated calculation by just speaking and talking calculator."
                                        )
                    
                     abt_text.config(state=DISABLED)
            
            


         
       ns.geometry("320x410+350+100")
       ns.minsize(width=320, height=410)
       ns.maxsize(width=320, height=410)
       ns.attributes("-topmost",True)
       frame1=Frame(ns,width=307,height=140,bd=1,relief="solid")
       frame1.pack(side=TOP)
       l=Label(frame1, text="Converters",fg="black",bd=2,font=('arial',25,'bold'))
       l.place(x=25,y=40)
       binary=Button(ns,text="Temprature",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10, command=temp1)
       binary.place(x=7,y=150)
       octal=Button(ns,text="Length",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=ucl)
       octal.place(x=163,y=150)
         
       hexa=Button(ns,text="Currency",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10)
       hexa.place(x=7,y=235)
       decimal=Button(ns,text="Weight",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10)
       decimal.place(x=163,y=235)


       
       helpp=Button(ns,text="About",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=about)
       helpp.place(x=7,y=320)
       helpp1=Button(ns,text="Back",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=confun)
       helpp1.place(x=163,y=320)
            
    def ucl():
       ns.withdraw()
       
       
       x=UnitRegistry()


       p=Tk()
       p.attributes("-topmost",True)




       #voice input
       def cal():
           vall.set("")
           sr.Microphone(device_index=1)
           
           r=sr.Recognizer()

           r.energy_thresold=1000
           with sr.Microphone() as source:
               
               r.adjust_for_ambient_noise(source, duration=5)
               print("speak")
               vall.set("Speak")
               print("Bol")
               audio=r.listen(source)
               
               try:
                   
                   text=r.recognize_google(audio)
                   
                   try:
                       text=int(text)
                       if(type(text)==int):    
                           print(text)
                           vall.set(text)
                   except ValueError:
                      vall.set("enter valid")
                   except:
                      vall.set(" some error")           
               except:
                   vall.set('say again')

       #voice button

       vocal=Button(p,text="Speak!",font=('arial',10,'bold'),width=10,height=1,command=cal)
       vocal.place(x=200,y=150)

       #all funtion
       def clear():
            vall.set("")
            val.set("")

       def fun1():
           pass


       def change0(*args):
           try:
        
       #For meter
               if(var.get()=='Meter'and var2.get()=='Centimeter'):
                   a=int(vall.get())
                   b=a*x.meter
                   c=str(b.to(x.centimeter))
                   val.set(c)
               if(var.get()=='Meter'and var2.get()=='Inch'):
                   a=int(vall.get())
                   b=a*x.meter
                   c=str(b.to(x.inch))
                   val.set(c)
               if(var.get()=='Meter'and var2.get()=='Milimeter'):
                   a=int(vall.get())
                   b=a*x.meter
                   c=str(b.to(x.mm))
                   val.set(c)
               if(var.get()=='Meter'and var2.get()=='Micrometer'):
                   a=int(vall.get())
                   b=a*x.meter
                   c=str(b.to(x.micrometer))
                   val.set(c)
               if(var.get()=='Meter'and var2.get()=='Nanometer'):
                   a=int(vall.get())
                   b=a*x.meter
                   c=str(b.to(x.nanometer))
                   val.set(c)
           #For Centimeter
               if(var.get()=='Centimeter'and var2.get()=='Meter'):
                   a=int(vall.get())
                   b=a*x.cm
                   c=str(b.to(x.meter))
                   val.set(c)
               if(var.get()=='Centimeter'and var2.get()=='Inch'):
                   a=int(vall.get())
                   b=a*x.cm
                   c=str(b.to(x.inch))
                   val.set(c)
               if(var.get()=='Centimeter'and var2.get()=='Milimeter'):
                   a=int(vall.get())
                   b=a*x.cm
                   c=str(b.to(x.mm))
                   val.set(c)
               if(var.get()=='Centimeter'and var2.get()=='Micrometer'):
                   a=int(vall.get())
                   b=a*x.cm
                   c=str(b.to(x.micrometer))
                   val.set(c)
               if(var.get()=='Centimeter'and var2.get()=='Nanometer'):
                   a=int(vall.get())
                   b=a*x.cm
                   c=str(b.to(x.nanometer))
                   val.set(c)
           #for Inch
               if(var.get()=='Inch'and var2.get()=='Meter'):
                   a=int(vall.get())
                   b=a*x.inch
                   c=str(b.to(x.meter))
                   val.set(c)
               if(var.get()=='Inch'and var2.get()=='Centimeter'):
                   a=int(vall.get())
                   b=a*x.inch
                   c=str(b.to(x.cm))
                   val.set(c)
               if(var.get()=='Inch'and var2.get()=='Milimeter'):
                   a=int(vall.get())
                   b=a*x.inch
                   c=str(b.to(x.mm))
                   val.set(c)
               if(var.get()=='Inch'and var2.get()=='Micrometer'):
                   a=int(vall.get())
                   b=a*x.inch
                   c=str(b.to(x.micrometer))
                   val.set(c)
               if(var.get()=='Inch'and var2.get()=='Nanometer'):
                   a=int(vall.get())
                   b=a*x.inch
                   c=str(b.to(x.nanometer))
                   val.set(c)
           #for mili
               if(var.get()=='Milimeter'and var2.get()=='Meter'):
                   a=int(vall.get())
                   b=a*x.mm
                   c=str(b.to(x.meter))
                   val.set(c)
               if(var.get()=='Milimeter'and var2.get()=='Centieter'):
                   a=int(vall.get())
                   b=a*x.mm
                   c=str(b.to(x.cm))
                   val.set(c)
               if(var.get()=='Milimeter'and var2.get()=='Microeter'):
                   a=int(vall.get())
                   b=a*x.mm
                   c=str(b.to(x.micrometer))
                   val.set(c)
               if(var.get()=='Milimeter'and var2.get()=='Nanometer'):
                   a=int(vall.get())
                   b=a*x.mm
                   c=str(b.to(x.nanometer))
                   val.set(c)
               if(var.get()=='Milimeter'and var2.get()=='Inch'):
                   a=int(vall.get())
                   b=a*x.mm
                   c=str(b.to(x.inch))
                   val.set(c)
           #Micrometer
               if(var.get()=='Micrometer'and var2.get()=='Meter'):
                   a=int(vall.get())
                   b=a*x.micrometer
                   c=str(b.to(x.meter))
                   val.set(c)
               if(var.get()=='Micrometer'and var2.get()=='Centimeter'):
                   a=int(vall.get())
                   b=a*x.micrometer
                   c=str(b.to(x.cm))
                   val.set(c)
               if(var.get()=='Micrometer'and var2.get()=='Inch'):
                   a=int(vall.get())
                   b=a*x.micrometer
                   c=str(b.to(x.inch))
                   val.set(c)
               if(var.get()=='Micrometer'and var2.get()=='Milimeter'):
                   a=int(vall.get())
                   b=a*x.micrometer
                   c=str(b.to(x.mm))
                   val.set(c)
               if(var.get()=='Micrometer'and var2.get()=='Nanometer'):
                   a=int(vall.get())
                   b=a*x.micrometer
                   c=str(b.to(x.nanometer))
                   val.set(c)
           #nanometer
               if(var.get()=='Nanometer'and var2.get()=='Meter'):
                   a=int(vall.get())
                   b=a*x.nanometer
                   c=str(b.to(x.meter))
                   val.set(c)
               if(var.get()=='Nanometer'and var2.get()=='Centimeter'):
                   a=int(vall.get())
                   b=a*x.nanometer
                   c=str(b.to(x.cm))
                   val.set(c)
               if(var.get()=='Nanometer'and var2.get()=='Inch'):
                   a=int(vall.get())
                   b=a*x.nanometer
                   c=str(b.to(x.inch))
                   val.set(c)
               if(var.get()=='Nanometer'and var2.get()=='Milimeter'):
                   a=int(vall.get())
                   b=a*x.nanometer
                   c=str(b.to(x.mm))
                   val.set(c)
               if(var.get()=='Nanometer'and var2.get()=='Micrometer'):
                   a=int(vall.get())
                   b=a*x.nanometer
                   c=str(b.to(x.micrometer))
                   val.set(c)
           except ValueError:
               val.set("Enter Valid Number")
               vall.set("")
               
       def click(key):
           global memory
           if key == '=':
               # avoid division by integer
               if '/' in entry.get() and '.' not in entry.get():
                   entry.insert(tk.END, ".0")
               # guard against the bad guys abusing eval()
               str1 = "-+0123456789."
               if entry.get()[0] not in str1:
                   entry.set(END, "first char not in " + str1)
               # here comes the calculation part
               try:
                   result = eval(entry.get())
                   entry.insert(END, " = " + str(result))
               except:
                   entry.insert(END, "--> Error!")
           elif key == 'C':
               entry.delete(0, END)  # clear entry
           elif key == '->M':
               memory = entry.get()
               # extract the result
               if '=' in memory:
                   ix = memory.find('=')
                   memory = memory[ix+2:]
               root.title('M=' + memory)
           elif key == 'M->':
               entry.insert(END, memory)
           elif key == 'neg':
               if '=' in entry.get():
                   entry.delete(0, END)
               try:
                   if entry.get()[0] == '-':
                       entry.delete(0)
                   else:
                       entry.insert(0, '-')
               except IndexError:
                   pass
           else:
               # previous calculation has been done, clear entry
               if '=' in entry.get():
                   entry.delete(0, END)
               entry.insert(END, key)
           






       p.geometry("320x410+350+100")
       p.title("Unit Converter")
       p.minsize(width=320, height=410)
       p.maxsize(width=320, height=410)
       vall=StringVar(p)

       val=StringVar(p)
       entry = Entry(p, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=vall)
       entry.place(x=14,y=0)
       entry1 = Entry(p, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=val)
       entry1.place(x=14,y=70)
       OPTIONS={'Meter','Centimeter','Inch','Milimeter','Micrometer','Nanometer'}
       var=StringVar(p)
       var.set('Meter')
       var2=StringVar(p)
       var2.set('Meter')

       btn_list = [
       '7',  '8',  '9',  
       '4',  '5',  '6',  
       '1',  '2',  '3', 
       '0',  '.',   ]
       # create all buttons with a loop
       r = 18
       c = 190
       for b in btn_list:
           rel = 'ridge'
           cmd = lambda x=b: click(x)
           Button(p,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
           r += 93
           if r >=279:
               r = 18
               c =c+50




       def bck():
           p.withdraw()
           unitconverter()
           


       menu=OptionMenu(p,var,*OPTIONS)
       menu.place(x=114,y=35)
       menu1=OptionMenu(p,var2,*OPTIONS)
       menu1.place(x=114,y=110)
       cal=Button(p,text="Calculate",font=('arial',10,'bold'),width=10,height=1,command=change0)
       cal.place(x=107,y=150)

       back=Button(p,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=bck)
       back.place(x=203,y=340)  

       clear=Button(p,text="Clear",font=('arial',10,'bold'),width=10,height=1,command=clear)
       clear.place(x=14,y=150)
       p.mainloop()
       




    # These  functions  perform all operation  which are related to numbersystem.
    #start->




    #end

    def calprofit():
        if (v.get()==1):
          s,p=input1.get().split()
          val1.set(s)
          val2.set(p)
          temp=(int(s)*int (p))/100
          input1.set(str(temp))
          
        elif(v.get()==2):
          s,p=input1.get().split()
          val1.set(s)
          val2.set(p)
          temp=(int(s)*int (p))/100
          s=int (s)-temp
          input1.set(str(s))
      
   
        
        
            
          



    def calgst():
         if (v.get()==1):
          s,p=input1.get().split()
          val1.set(s)
          val2.set(p)
          temp=(int(s)*int(p))/100
          s=int (s)
          s+=temp
          input1.set(str(s))
      
      
         elif(v.get()==2):
             s,p=input1.get().split()
             val1.set(s)
             val2.set(p)
             temp=(int(s)*int (p))/100
             s=int (s)
             s-=temp
             input1.set(str(s))

    def calsi():
        try:
            p,r,t=input1.get().split()
            val1.set(p)
            val2.set(r)
            val3.set(t)
            si=(int (p)*int(r)*int (t))/100
            input1.set(str(si))
        except:
          input1.set("SomeError")
        
        
        
            
          
          

    # code for scientific calculator 
    #start->

    def other():
       root.withdraw()
       
    
       import math
       
       class Calc():
           def __init__(self):
               self.total = 0
               self.current = ""
               self.new_num = True
               self.op_pending = False
               self.op = ""
               self.eq = False

           def num_press(self, num):
               self.eq = False
               temp = text_box.get()
               temp2 = str(num)
               if self.new_num:
                   self.current = temp2
                   self.new_num = False
               else:
                   if temp2 == '.':
                       if temp2 in temp:
                           return
                   self.current = temp + temp2
               self.display(self.current)


           def calc_total(self):
               self.eq = True
               self.current = float(self.current)
               if self.op_pending == True:
                   self.do_sum()
               else:
                   self.total = float(text_box.get())

           def display(self, value):
               text_box.delete(0, END)
               text_box.insert(0, value)

           def do_sum(self):
               if self.op == "add":
                   self.total += self.current
               if self.op == "minus":
                   self.total -= self.current
               if self.op == "times":
                   self.total *= self.current
               if self.op == "divide":
                   self.total /= self.current
               if self.op == "raise":
                   self.total = self.total ** self.current
               if self.op == "rootof":
                   self.total = self.total ** (1/self.current)
               if self.op == "fact":
                   self.total=int(text_box.get())
                   self.total=math.factorial(self.total)
               if self.op == "ln":
                   self.total = log(self.total)
               if self.op == "log":
                   self.total=log(self.total,10)
               if self.op == "sine":
                   self.total=math.sin(self.total)
               if self.op == "cosine":
                   self.total = math.cos(self.total)
               if self.op == "tangent":
                   self.total = math.tan(self.total)
               if self.op == "exp":
                   self.total = math.exp(self.total)
               if self.op == "inv":
                   self.total = 1/self.total
               self.new_num = True
               self.op_pending = False
               self.display(self.total)

           def operation(self, op):
               self.current = float(self.current)
               if self.op_pending:
                   self.do_sum()
               elif not self.eq:
                   self.total = self.current
               self.new_num = True
               self.op_pending = True
               self.op = op
               self.eq = False

           def clear(self):
               self.eq = False
               self.current = "0"
               self.display(0)
               self.new_num = True

           def all_clear(self):
               self.clear()
               self.total = 0

           def sign(self):
               self.eq = False
               self.current = -(float(text_box.get()))
               self.display(self.current)

       sum1 = Calc()
       sm = Tk()
       sm.geometry("+350+100")
       calc = Frame(sm)
       calc.grid()
       
       
       sm.title("Calculator")
       sm.attributes("-topmost",True)
       text_box = Entry(calc, justify=RIGHT,width=30,font="Times 16 bold")
       text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
       text_box.insert(0, "0")
       #text_box.focus()

       numbers = "789456123"
       i = 0
       bttn = []
       for j in range(1,4):
           for k in range(3):
               bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
               bttn[i]["bg"]= "orange"
               bttn[i].grid(row = j, column = k,padx=1,pady=1)
               bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
               i += 1

       bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="orange")
       bttn_0["command"] = lambda: sum1.num_press(0)
       bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

       div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="steel blue")
       div["command"] = lambda: sum1.operation("divide")
       div.grid(row = 1, column = 3, padx=1, pady = 1)

       mult = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="steel blue")
       mult["command"] = lambda: sum1.operation("times")
       mult.grid(row = 2, column = 3,  padx=1, pady = 1)

       minus = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="steel blue")
       minus["command"] = lambda: sum1.operation("minus")
       minus.grid(row = 3, column = 3, padx=1, pady = 1)

       add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="steel blue")
       add["command"] = lambda: sum1.operation("add")
       add.grid(row = 4, column = 3,  padx=1, pady = 1)

       power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="green")
       power["command"] = lambda: sum1.operation("raise")
       power.grid(row=2,column = 4,padx=1,pady=1)

       rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "green")
       rootof["command"] = lambda: sum1.operation("rootof")
       rootof.grid(row=2, column=5, padx=1, pady=1)

       fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!",bg="green")
       fact["command"] = lambda: sum1.operation("fact")
       fact.grid(row=3,column=4, padx=1, pady=1)

       loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln",bg="green")
       loge["command"] = lambda: sum1.operation("ln")
       loge.grid(row=3, column=5, padx=1, pady=1)

       log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="green")
       log10["command"]= lambda: sum1.operation("log")
       log10.grid(row=4, column=4, padx=1 , pady=1)

       sine = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "green")
       sine["command"]=lambda: sum1.operation("sine")
       sine.grid(row=5,column=0,padx=1,pady=1)


       cosine = Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "green")
       cosine["command"]=lambda: sum1.operation("cosine")
       cosine.grid(row=5,column=1,padx=1,pady=1)

       tangent = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "green")
       tangent["command"]=lambda: sum1.operation("tangent")
       tangent.grid(row=5,column=2,padx=1,pady=1)

       exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="green")
       exponent["command"]=lambda: sum1.operation("exp")
       exponent.grid(row=5,column=3,padx=1,pady=1)

       inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
       inv["command"] = lambda: sum1.operation("inv")
       inv.grid(row=5,column=4,padx=1,pady=1)

       point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
       point["command"] = lambda: sum1.num_press(".")
       point.grid(row = 4, column = 1, padx=1, pady = 1)

       neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
       neg["command"] = sum1.sign
       neg.grid(row = 4, column = 2,  padx=1, pady = 1)


       clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
       clear["command"] = sum1.clear
       clear.grid(row = 1, column = 4,  padx=1, pady = 1)

       all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
       all_clear["command"] = sum1.all_clear
       all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

       equals = Button(calc,height =6,width=4,padx=10, pady = 10, text = "=",bg="green")
       equals["command"] = sum1.calc_total
       equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)

       sm.mainloop()

    #end
       













    def  fun5():
            global top9
            top9=Toplevel()
            top9.geometry("320x410+350+100")
            top9.minsize(width=320, height=410)
            top9.maxsize(width=320, height=410)
            top9.attributes("-topmost",True)
        
            global input1
            input1=StringVar()
            entry = Entry(top9, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=10,y=5)
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top9,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50



        
        
    # Unit Converter  calculator
    # Code->



         
       
         
 
 
    #END 


    #CODE FOR NUMBERSYSTEM
    # START ->
    #FUNCTION FOR SPEAK BUTTON   OCTAL TO ALL

    def speekoctal():
        import tkinter as tk
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source, duration=5)
           print('speak')
           audio=r.listen(source)
           try:
                binary=r.recognize_google(audio)
                try:  
                     def dec_to_all(binary1):
                         dec = str(int(binary1, 8)); # convert into decimal
                         decm = int(dec)
                         temp=bin(decm)
                         res2=dec
                         res1=hex(decm)
                         val1.set(temp)
                         val2.set(res2)
                         val3.set(res1)
                         
                     dec_to_all(binary)
                except ValueError:
                    val1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    val1.set(e)
                    print(e)
           except:
                val1.set("SayAgain")
                print('say again')
    ##FUNCTION FOR  CALCULATE  BUTTON
    # OCTAL TO ALL

    def caloctal():
           try:
                binary1=input1.get()
                try:  
                     def dec_to_all(binary1):
                         dec = str(int(binary1, 8)); # convert into decimal
                         decm = int(dec)
                         temp=bin(decm)
                         res2=dec
                         res1=hex(decm)
                         val1.set(temp)
                         val2.set(res2)
                         val3.set(res1)
                         
                     dec_to_all(binary1)
                except ValueError:
                    input1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    input1.set(e)
                    print(e)
           except:
               input1.set("SayAgain")
               print('say again')



    #END OCTAL

    ##FUNCTION FOR SPEAK BUTTON   DECIMAL TO ALL
    #START


    def speekdecimal():
        import tkinter as tk
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source, duration=5)
           print('speak')
           audio=r.listen(source)
           try:
                binary=r.recognize_google(audio)
                try:  
                     def dec_to_all(binary1):
                         input1.set(binary)
                         decm = int(binary1) # convert into decimal     
                         temp = bin(decm)
                         res1=hex(decm)
                         res2=oct(decm)
                         val1.set(temp)
                         val2.set(res2)
                         val3.set(res1)
                         
                     dec_to_all(binary)
                except ValueError:
                    val1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    val1.set(e)
                    print(e)
           except:
               val1.set("SayAgain")
               print('say again')


    ##FUNCTION FOR  CALCULATE  BUTTON   DECIMAL TO ALL
               
    def caldecimal():
           try:
                binary=input1.get()
                try:  
                     def dec_to_all(binary1):
                         decm = int(binary1) # convert into decimal     
                         temp = bin(decm)
                         res1=hex(decm)
                         res2=oct(decm)
                         val1.set(temp)
                         val2.set(res2)
                         val3.set(res1)
                         
                     dec_to_all(binary)
                except ValueError:
                    input1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    input1.set(e)
                    print(e)
           except:
               input1.set("SayAgain")
               print('say again')

    #END
               

    def speekhexa():
        import tkinter as tk
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source, duration=5)
           print('speak')
           audio=r.listen(source)
           try:
                binary=r.recognize_google(audio)
                try:
                    input1.set(binary)
                    def hexa_to_all(binary1):
                          dec = int(binary1, 16)
                          res2=bin(dec)
                          res1=oct(dec)
                          val1.set(dec)
                          val2.set(res1)
                          val3.set(res2)
                          
                          
                    hexa_to_all(binary)
                except ValueError:
                   print("ValueError")
                except Exception as e:
                    print(e)
           except:
                print('say again')





    def calhexa():
           try:
                binary=input1.get()
                try:
                    binary=input1.get()
            
                    def hexa_to_all(binary1):
                          dec = int(binary1, 16)
                          res2=bin(dec)
                          res1=oct(dec)
                          val1.set(dec)
                          val2.set(res1)
                          val3.set(res2)
                          
                          
                    hexa_to_all(binary)
                
                except ValueError:
                    input1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    input1.set(e)
                    print(e)
           except:
               input1.set("SayAgain")
               print('say again')
                
        

    def speekbinary():
        
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source, duration=5)
           print('speak')
           audio=r.listen(source)
           try:
                binary=r.recognize_google(audio)
                try:  
                     def bin_to_all(binary1):
                         input1.set(binary)
                         temp = int(binary1, 2)   
                         res1=hex(temp)
                         res2=oct(temp)
                         val1.set(temp)
                         val2.set(res2)
                         val3.set(res1)

       
                     bin_to_all(binary)
                except ValueError:
                   print("ValueError")
                except Exception as e:
                    print(e)
           except:
                print('say again')










    def calbinary():
           try:
                binary=input1.get()
                try:
                    def bin_to_all(binary1):
                         temp = int(binary1, 2)   
                         res1=hex(temp)
                         res2=oct(temp)
                         val1.set(temp)
                         val2.set(res2)
                         val3.set(res1)

                         
                    bin_to_all(binary)
                
                    
                         
             
                except ValueError:
                    input1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    input1.set(e)
                    print(e)
           except:
               input1.set("SayAgain")
               print('say again')

    def speekfraction():
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print('speak')
            audio=r.listen(source)
            try:
                 text=r.recognize_google(audio)
                 try:
                    print (text)
                    input1.set(text)
                    res=Fraction(text)
                    print (res)
                    input2.set("Num="+str(res))
                    
                 except ValueError:
                   print("ValueError")
                 except Exception as e:
                    print(e)
            except:
                print('say again')


    def calfraction():
        try:
                 text=input1.get()
                 try:
                    res=Fraction(text)
                    input2.set("Num="+str(res))
                    
                 except ValueError:
                   print("ValueError")
                   input2.set("ValueError")
                 except Exception as e:
                    input2.set(e)

        except:
                input2.set("TryAgain")
        


        

    def speekfact():
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print('speak')
            audio=r.listen(source)
            try:
                 
                 text=r.recognize_google(audio)
                 try:
                    input1.set(text)
                    f=int(text)
                    r=math.factorial(f)
                    input2.set(str(r))
                 except ValueError:
                   print("ValueError")
                 except Exception as e:
                    print(e)
            except:
                print('say again')


    def calfact():
           try:
                text=input1.get()
                try:
                    f=int(text)
                    r=math.factorial(f)
                    input2.set(str(r))
                     
                except ValueError:
                    input1.set("ValueError")
                    print("ValueError")
                except Exception as e:
                    input1.set(e)
                    print(e)
           except:
               input1.set("SayAgain")
               print('say again')



    def speekprime():
        sr.Microphone(device_index=1)
        r=sr.Recognizer()
        r.energy_thresold=1
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print('speak')
            audio=r.listen(source)
            try:
                
                 
                 text=r.recognize_google(audio)
                 try:
                    f=int(text)
                    num = f
                    if num > 1:
                       for i in range(2,num):
                           if (num % i) == 0:
                               print(num,"is not a prime number")
                               val1.set(str(num)+"=is not a prime number")
                               break
                       else:
                           print(num,"is a prime number")
                           val1.set(str(num)+"=is a prime number")
                           
                    else:
                       val1.set(str(num)+"is not a prime number")
                       print(num,"=is not a prime number")

                 except ValueError:
                   print("ValueError")
                 except Exception as e:
                    print(e)
            except:
                print('say again')




    def calprime():
            try:
                 text=input1.get()
                 try:
                    f=int(text)
                    num = f
                    if num > 1:
                       for i in range(2,num):
                           if (num % i) == 0:
                               print(num,"is not a prime number")
                               input2.set(str(num)+"=is not a prime number")
                               break
                       else:
                           print(num,"is a prime number")
                           input2.set(str(num)+"=is a prime number")
                           
                    else:
                       input2.set(str(num)+"is not a prime number")
                       print(num,"=is not a prime number")

                 except ValueError:
                   print("ValueError")
                 except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        

        
            
        

        
         
         


    def clear1():
            input1.set(" ")
            val1.set("")
            val2.set("")
            val3.set("")


    def clear2():
            input1.set(" ")
            input2.set(" ")
            
            


            
    def  finance():
         ac.withdraw()
         top=Toplevel()
         top.title("Finance")
         top.geometry("320x410+350+100")
         top.minsize(width=320, height=410)
         top.maxsize(width=320, height=410)
         top.attributes("-topmost",True)
         
         def profit():
             top.withdraw()
             pt=Toplevel()
             pt.geometry("320x410+350+100")
             pt.minsize(width=320, height=410)
             pt.maxsize(width=320, height=410)
             pt.attributes("-topmost",True)
        
             global input1
             input1=StringVar()
             entry = Entry(pt, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
             entry.place(x=10,y=5)
            
             def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


             btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
             r = 18
             c = 190
             for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(pt,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50


            
             l1=Label(pt,text="Amount",font=('arial',10,'bold'))
             l1.place(x=10,y=50)

             l2=Label(pt,text="Rate Of  %",font=('arial',10,'bold'))
             l2.place(x=10,y=85)

             global val1
             val1=StringVar()
             entry1=Entry(pt,font=('arial',10,'bold'),bd=4,textvariable=val1)
             entry1.place(x=150,y=50)
            
             def numb():
                pt.withdraw()
                finance()
                
                
                

             entry1=Entry(pt,font=('arial',10,'bold'),bd=4,textvariable=val1)
             entry1.place(x=150,y=50)
            
             global val2
             val2=StringVar()
            
             entry2=Entry(pt,font=('arial',10,'bold'),bd=4,textvariable=val2)
             entry2.place(x=150,y=85)
            
             global val3
             val3=StringVar()
             global v
            
             v = IntVar()
             r1=Radiobutton(pt,text="Profit",padx = 20, variable=v, value=1)
             r1.place(x=10,y=120)

             r1=Radiobutton(pt,text="Loss",padx = 20, variable=v, value=2)
             r1.place(x=150,y=120)

             speak=Button(pt,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1)
             speak.place(x=17,y=160)

             cal=Button(pt,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calprofit)
             cal.place(x=112,y=160)

            
             clear=Button(pt,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
             clear.place(x=203,y=160)
            
             back=Button(pt,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
             back.place(x=203,y=340)

          

         def simple():
             
            top.withdraw()
            si=Toplevel()
            si.geometry("320x410+350+100")
            si.minsize(width=320, height=410)
            si.maxsize(width=320, height=410)
            si.attributes("-topmost",True)


            global input1
            input1=StringVar()
            entry = Entry(si, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=10,y=5)
            
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(si,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50



                    

                    
                    
                    

            l1=Label(si,text="Principal",font=('arial',10,'bold'))
            l1.place(x=10,y=50)
            
            l2=Label(si,text="Rate Of Intrest",font=('arial',10,'bold'))
            l2.place(x=10,y=85)
            
            
            l4=Label(si,text="Time ",font=('arial',10,'bold'))
            l4.place(x=10,y=120)
            
            def numb():
                top.withdraw()
                numbersystem()

        
            global val1
            val1=StringVar()
            
            entry1=Entry(si,font=('arial',10,'bold'),bd=4,textvariable=val1)
            entry1.place(x=150,y=50)
            
            global val2
            val2=StringVar()
            
            entry2=Entry(si,font=('arial',10,'bold'),bd=4,textvariable=val2)
            entry2.place(x=150,y=85)
            
            global val3
            val3=StringVar()
            
            entry3=Entry(si,font=('arial',10,'bold'),bd=4,textvariable=val3)
            entry3.place(x=150,y=120)
            
            speak=Button(si,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1)
            speak.place(x=17,y=160)

            cal=Button(si,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calsi)
            cal.place(x=112,y=160)

            
            clear=Button(si,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
            clear.place(x=203,y=160)
            def siback():
                si.withdraw()
                finance()
            
            back=Button(si,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=siback)
            back.place(x=203,y=340)
     
         
         def gst():
            top.withdraw()
            gt=Toplevel()
            gt.geometry("320x410+350+100")
            gt.minsize(width=320, height=410)
            gt.maxsize(width=320, height=410)
            gt.attributes("-topmost",True)
        
            global input1
            input1=StringVar()
            entry = Entry(gt, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=10,y=5)
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(gt,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50
            
            
            l1=Label(gt,text="Amount",font=('arial',10,'bold'))
            l1.place(x=10,y=50)

            l2=Label(gt,text="Rate Of  %",font=('arial',10,'bold'))
            l2.place(x=10,y=85)

            global val1
            val1=StringVar()
            entry1=Entry(gt,font=('arial',10,'bold'),bd=4,textvariable=val1)
            entry1.place(x=150,y=50)
            
            def numb():
                gt.withdraw()
                finance()

            entry1=Entry(gt,font=('arial',10,'bold'),bd=4,textvariable=val1)
            entry1.place(x=150,y=50)
            
            global val2
            val2=StringVar()
            
            entry2=Entry(gt,font=('arial',10,'bold'),bd=4,textvariable=val2)
            entry2.place(x=150,y=85)
            
            global val3
            val3=StringVar()
            global v
            
            v = IntVar()
            
            r1=Radiobutton(gt,text="+Gst",padx = 20, value=1,variable=v)
            r1.place(x=10,y=120)

            r1=Radiobutton(gt,text="-Gst",padx = 20, value=2,variable=v)
            r1.place(x=150,y=120)

            speak=Button(gt,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1)
            speak.place(x=17,y=160)

            cal=Button(gt,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calgst)
            cal.place(x=112,y=160)

            
            clear=Button(gt,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
            clear.place(x=203,y=160)
            
            back=Button(gt,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
            back.place(x=203,y=340)
         
                 
            

             

        
         frame1=Frame(top,width=307,height=140,bd=1,relief="solid")
         frame1.pack(side=TOP)
         l=Label(frame1, text="Finance",fg="black",bd=2,font=('arial',40,'bold'))
         l.place(x=40,y=40)
         
         binary=Button(top,text="SimpleIntrest",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=simple)
         binary.place(x=7,y=150)
         

         
         octal=Button(top,text="Percentage ",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=profit)
         octal.place(x=163,y=150)
         

         
         hexa=Button(top,text="Loss",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10)
         hexa.place(x=7,y=235)


         def about():
                     top.withdraw()
                     
                     top1=Toplevel()
                     top1.title("About")
                     top1.geometry("320x410+350+100")
                     top1.minsize(width=320, height=410)
                     top1.maxsize(width=320, height=410)
                     top1.lift()
                     top1.attributes("-topmost",True)
                     global val
                     val=StringVar()
                    
                    
                     abt_text=Text(top1,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
                     abt_text.pack()
                     abt_text.insert(INSERT,

                                       "Voice Calculator is very amusing desktop applications and voice activated calculator is most running applications.\n"
                                        "\nCalculator is basic need of life most probably for working people, for students of engineering,teachers, for clerical work and for other such purposes like carpenteron shops markets fast calculation is done on daily basis.\n\n"
                                        "So for all calculator users, this best voice calculator free is a finest fast calculator.\n"
                                        "Now you just have to speak and voice online calculator will automatically calculate what you say"
                                        "You can perform simple as well as complicated calculation by just speaking and talking calculator."
                                        )
                    
                     abt_text.config(state=DISABLED)
    
    



         
         decimal=Button(top,text="GST",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10, command=gst)
         decimal.place(x=163,y=235)
         helpp=Button(top,text="About",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=about)
         helpp.place(x=7,y=320)

         def  finback():
             top.withdraw()
             algebra()
         helpp1=Button(top,text="Back",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=finback)
         helpp1.place(x=163,y=320) 
         root.quit()
         

        
         
          
            

            
            

            
             


            

       


    def help():
        root.withdraw()
        top=Toplevel()
        top.title("Help")
        top.geometry("320x410+350+100")
        top.minsize(width=320, height=410)
        top.maxsize(width=320, height=410)
        top.lift()
        top.attributes("-topmost",True)
        global val
        val=StringVar()
        
        
        help_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
        help_text.pack()
        help_text.insert(INSERT,"How to use:\n"
                         "Step 1. Click on Tap to Speak.\n"
                         "Step 2. Instructions to use.\n"

                        "\nTo calculate addition(+) speak plus.\n"
                        "like to do 8+1, say: eight plus one.\n"

                         
                        "\nTo calculate  subtraction(-) speak minus.\n"
                         "like to do 8-1, say: eight minus one.\n"
                         
                         "\nTo calculate multiplication(*) speak multiplied by.\n"
                         "like to say: six multiplied by three.\n"
                         
                         "\nTo calculate division(/) speak divided by.\n"
                         
                         "like to do 7/3 say: seven divided by three.\n"
                         
                         "\nStep 4. Tap on speaker to hear the result.\n"

                          "For better result use microphone."


                         )
        help_text.config(state=DISABLED)


      

    def numbersystem():
        
         root.withdraw()
         ns=Toplevel()
         ns.title("Number System")
         ns.geometry("320x410+350+100")
         ns.minsize(width=320, height=410)
         ns.maxsize(width=320, height=410)
         ns.attributes("-topmost",True)

         def about():
             ns.withdraw()
             top=Toplevel()
             top.title("About")
             top.geometry("320x410+350+100")
             top.minsize(width=320, height=410)
             top.maxsize(width=320, height=410)
             top.lift()
             top.attributes("-topmost",True)
             global val
             val=StringVar()
            
            
             abt_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
             abt_text.pack()
             abt_text.insert(INSERT,

                               "Voice Calculator is very amusing desktop applications and voice activated calculator is most running applications.\n"
                                "\nCalculator is basic need of life most probably for working people, for students of engineering,teachers, for clerical work and for other such purposes like carpenteron shops markets fast calculation is done on daily basis.\n\n"
                                "So for all calculator users, this best voice calculator free is a finest fast calculator.\n"
                                "Now you just have to speak and voice online calculator will automatically calculate what you say"
                                "You can perform simple as well as complicated calculation by just speaking and talking calculator."
                                )
            
             abt_text.config(state=DISABLED)
    
    


    



         def key2():
             ns.withdraw()
             yes()


         def hexafun():
            ns.withdraw()
             
            top=Toplevel()
            top.title("HexaToAll")
            top.geometry("320x410+300+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.attributes("-topmost",True)

            global input1
            input1=StringVar()
            
            entry = Entry(top, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1   )
            entry.place(x=10,y=5)
           # but=Button(top,text='BUt',command=numbersystem)
           # but.place(x=100,y=100)
            

            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50


            l1=Label(top,text="Hexa To Decimal",font=('arial',10,'bold'))
            l1.place(x=10,y=50)
            
            l2=Label(top,text="Hexa To Octal )",font=('arial',10,'bold'))
            l2.place(x=10,y=85)
            
            l4=Label(top,text="Hexa To Binary ",font=('arial',10,'bold'))
            l4.place(x=10,y=120)
            
            def numb():
                top.withdraw()
                numbersystem()

        
            global val1
            val1=StringVar()
            
            entry1=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val1,state=DISABLED)
            entry1.place(x=150,y=50)
            
            global val2
            val2=StringVar()
            
            entry2=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val2,state=DISABLED)
            entry2.place(x=150,y=85)
            
            global val3
            val3=StringVar()
            
            entry3=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val3,state=DISABLED)
            entry3.place(x=150,y=120)
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekhexa)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=caloctal)
            cal.place(x=112,y=160)

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
            clear.place(x=203,y=160)
            
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
            back.place(x=203,y=340)
              






            
        




         def decimalfun():
            ns.withdraw()
             
            top=Toplevel()
            top.title("Decimal To All")
            top.geometry("320x410+350+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.attributes("-topmost",True)

            global input1
            input1=StringVar()
            
            entry = Entry(top, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=10,y=5)
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50


            l1=Label(top,text="Decimal To Binary",font=('arial',10,'bold'))
            l1.place(x=10,y=50)
            
            l2=Label(top,text="Decimal To Octal",font=('arial',10,'bold'))
            l2.place(x=10,y=85)
            
            
            l4=Label(top,text="Decimal To  Hexa ",font=('arial',10,'bold'))
            l4.place(x=10,y=120)
            
            def numb():
                top.withdraw()
                numbersystem()

        
            global val1
            val1=StringVar()
            
            entry1=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val1)
            entry1.place(x=150,y=50)
            
            global val2
            val2=StringVar()
            
            entry2=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val2)
            entry2.place(x=150,y=85)
            
            global val3
            val3=StringVar()
            
            entry3=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val3)
            entry3.place(x=150,y=120)
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekdecimal)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=caldecimal)
            cal.place(x=112,y=160)

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
            clear.place(x=203,y=160)
            
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
            back.place(x=203,y=340)
              

          
         def octalfun():
            ns.withdraw()
             
            top=Toplevel()
            top.title("OctalToAll")
            top.geometry("320x410+350+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.attributes("-topmost",True)

            global input1
            input1=StringVar()
            
            entry = Entry(top, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=10,y=5)
           # but=Button(top,text='BUt',command=numbersystem)
           # but.place(x=100,y=100)
            

            
            def click(key):
                import tkiter as tk
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                import tkinter as tk
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50


            l1=Label(top,text="Octal To Binary",font=('arial',10,'bold'))
            l1.place(x=10,y=50)
            
            l2=Label(top,text="Octal To Decimal",font=('arial',10,'bold'))
            l2.place(x=10,y=85)
            
            
            l4=Label(top,text="Octal To  Hexa ",font=('arial',10,'bold'))
            l4.place(x=10,y=120)
            
            def numb():
                top.withdraw()
                numbersystem()

        
            global val1
            val1=StringVar()
            
            entry1=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val1)
            entry1.place(x=150,y=50)
            
            global val2
            val2=StringVar()
            
            entry2=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val2)
            entry2.place(x=150,y=85)
            
            global val3
            val3=StringVar()
            
            entry3=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val3)
            entry3.place(x=150,y=120)
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekoctal)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=caloctal)
            cal.place(x=112,y=160)

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
            clear.place(x=203,y=160)
            
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
            back.place(x=203,y=340)
            





             
            
         def binaryfun():
            ns.withdraw()
            top=Toplevel()
            top.geometry("320x410+350+100")
            top.title("BinaryToAll")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.attributes("-topmost",True)

            global input1
            input1=StringVar()
            
            entry = Entry(top, width=26,font=('arial',15),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=10,y=5)
           # but=Button(top,text='BUt',command=numbersystem)
           # but.place(x=100,y=100)
            

            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                import tkinter as tk
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50


            l1=Label(top,text="Binary To Decimal",font=('arial',10,'bold'))
            l1.place(x=10,y=50)
            
            l2=Label(top,text="Binary To Octal",font=('arial',10,'bold'))
            l2.place(x=10,y=85)
            
            
            l4=Label(top,text="Binary To Hexa",font=('arial',10,'bold'))
            l4.place(x=10,y=120)
            
            def numb():
                top.withdraw()
                numbersystem()

        
            global val1
            val1=StringVar()
            
            entry1=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val1)
            entry1.place(x=150,y=50)
            
            global val2
            val2=StringVar()
            
            entry2=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val2)
            entry2.place(x=150,y=85)
            
            global val3
            val3=StringVar()
            
            entry3=Entry(top,font=('arial',10,'bold'),bd=4,textvariable=val3)
            entry3.place(x=150,y=120)
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekbinary)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calbinary)
            cal.place(x=112,y=160)

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear1)
            clear.place(x=203,y=160)
            
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
            back.place(x=203,y=340)
     







            
         frame1=Frame(ns,width=307,height=140,bd=1,relief="solid")
         frame1.pack(side=TOP)
         


        
         
         binary=Button(ns,text="BinaryToAll",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10, command=binaryfun)
         binary.place(x=7,y=150)
         l=Label(frame1, text="Number System",fg="black",bd=2,font=('arial',25,'bold'))
         l.place(x=25,y=40)
            
         octal=Button(ns,text="OctalToALL",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=octalfun)
         octal.place(x=163,y=150)
         
       
         hexa=Button(ns,text="HexaToALL",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=hexafun)
         hexa.place(x=7,y=235)
         

         decimal=Button(ns,text="DecimalToALL",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=decimalfun)
         decimal.place(x=163,y=235)
         helpp=Button(ns,text="About",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=about)
         helpp.place(x=7,y=320)
         helpp1=Button(ns,text="Back",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=key2)
         helpp1.place(x=163,y=320)     
         root.quit()


         
         

    def algebra():
         root.withdraw()

         global ac
        
         ac=Toplevel()
         ac.title("Others")
         ac.geometry("320x410+350+100")
         ac.minsize(width=320, height=410)
         ac.maxsize(width=320, height=410)
         ac.attributes("-topmost",True)

         def about():
                     ac.withdraw()
                     top=Toplevel()
                     top.title("About")
                     top.geometry("320x410+350+100")
                     top.minsize(width=320, height=410)
                     top.maxsize(width=320, height=410)
                     top.lift()
                     top.attributes("-topmost",True)
                     global val
                     val=StringVar()
                    
                    
                     abt_text=Text(top,width=300,height=400,wrap=WORD,padx=10,pady=10,bd=4,selectbackground="red" ,fg="black")
                     abt_text.pack()
                     abt_text.insert(INSERT,

                                       "Voice Calculator is very amusing desktop applications and voice activated calculator is most running applications.\n"
                                        "\nCalculator is basic need of life most probably for working people, for students of engineering,teachers, for clerical work and for other such purposes like carpenteron shops markets fast calculation is done on daily basis.\n\n"
                                        "So for all calculator users, this best voice calculator free is a finest fast calculator.\n"
                                        "Now you just have to speak and voice online calculator will automatically calculate what you say"
                                        "You can perform simple as well as complicated calculation by just speaking and talking calculator."
                                        )
                    
                     abt_text.config(state=DISABLED)
    
    



         def key3():
             
             ac.withdraw()
             yes()

         
         def prime():
            ac.withdraw()
            top=Toplevel()
            top.title("Prime")
            top.geometry("320x410+350+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.lift()
            top.attributes("-topmost",True)

            global input1
            input1=StringVar()

            l1=Label(top,text=" Enter Value For PrimeNumber",font=('arial',15,'bold') ,width=26,height=2)
            l1.place(x=10,y=0)
            
            entry = Entry(top, width=26,font=('arial',14),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=20,y=50)


            global input2
            input2=StringVar()
            
            entry2 = Entry(top, width=26,font=('arial',14),bd=5,bg="white",selectforeground='red',textvariable=input2)
            entry2.place(x=20,y=100)
            
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50
            
            def numb():
                top.withdraw()
                algebra()
                
                
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekprime)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calprime)
            cal.place(x=112,y=160)

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear2)
            clear.place(x=203,y=160)
            
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=numb)
            back.place(x=203,y=340)
            
          
         def fact():
            ac.withdraw()
             
            top=Toplevel()
            top.title("Factorial")
            top.geometry("320x410+350+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.lift()
            top.attributes("-topmost",True)


            global input1
            input1=StringVar()

            l1=Label(top,text=" Enter Value For  Factorial ",font=('arial',15,'bold') ,width=26,height=2)
            l1.place(x=15,y=0)
            
            entry = Entry(top, width=26,font=('arial',14),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=20,y=50)


            global input2
            input2=StringVar()
            
            entry2 = Entry(top, width=26,font=('arial',14),bd=5,bg="white",selectforeground='red',textvariable=input2)
            entry2.place(x=20,y=100)
            
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry
                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50
            
            def numb():
                ac.withdraw
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekfact)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calfact)
            cal.place(x=112,y=160)

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear2)
            clear.place(x=203,y=160)
            def bc():
                top.withdraw()
                algebra()
            
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=bc)
            back.place(x=203,y=340)


            
          
         def fraction():
            ac.withdraw()
            top=Toplevel()
            top.title('Fraction')
            top.geometry("320x410+350+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.attributes("-topmost",True)


            global input1
            input1=StringVar()

            l1=Label(top,text=" Enter Value For FractionNumber",font=('arial',15,'bold') ,width=26,height=2)
            l1.place(x=5,y=0)
            
            entry = Entry(top, width=26,font=('arial',14),bd=5,bg="white",selectforeground='red',textvariable=input1)
            entry.place(x=20,y=50)


            global input2
            input2=StringVar()
            
            entry2 = Entry(top, width=26,font=('arial',14),bd=5,bg="white",selectforeground='red',textvariable=input2)
            entry2.place(x=20,y=100)
            
            
            def click(key):
                global memory
                if key == '=':
                    # avoid division by integer
                    if '/' in entry.get() and '.' not in entry.get():
                        entry.insert(tk.END, ".0")
                    # guard against the bad guys abusing eval()
                    str1 = "-+0123456789."
                    if entry.get()[0] not in str1:
                        entry.set(tk.END, "first char not in " + str1)
                    # here comes the calculation part
                    try:
                        result = eval(entry.get())
                        entry.insert(tk.END, " = " + str(result))
                    except:
                        entry.insert(tk.END, "--> Error!")
                elif key == 'C':
                    entry.delete(0, tk.END)  # clear entry













                elif key == '->M':
                    memory = entry.get()
                    # extract the result
                    if '=' in memory:
                        ix = memory.find('=')
                        memory = memory[ix+2:]
                    root.title('M=' + memory)
                elif key == 'M->':
                    entry.insert(tk.END, memory)
                elif key == 'neg':
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    try:
                        if entry.get()[0] == '-':
                            entry.delete(0)
                        else:
                            entry.insert(0, '-')
                    except IndexError:
                        pass
                else:
                    # previous calculation has been done, clear entry
                    if '=' in entry.get():
                        entry.delete(0, tk.END)
                    entry.insert(tk.END, key)


            btn_list = [
            '7',  '8',  '9',  
            '4',  '5',  '6',  
            '1',  '2',  '3', 
            '0',  '.',   ]
            # create all buttons with a loop
            r = 18
            c = 190
            for b in btn_list:
                rel = 'ridge'
                cmd = lambda x=b: click(x)
                tk.Button(top,text=b,width=9,font=('arial',10,'bold'),relief='raise',height=2,command=cmd).place(x=r,y=c)
                r += 93
                if r >=279:
                    r = 18
                    c =c+50
            
            def numb():
                top.withdraw()
            
            speak=Button(top,text="Speak",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=speekfraction)
            speak.place(x=17,y=160)

            cal=Button(top,text="Calculate",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=calfraction)
            cal.place(x=112,y=160)
            

            
            clear=Button(top,text="Clear",font=('arial',10,'bold'),relief='raise',width=9,height=1,command=clear2)
            clear.place(x=203,y=160)
            def bc():
                top.withdraw()
                algebra()
            back=Button(top,text="Back",font=('arial',10,'bold'),relief='raise',width=9,height=2,command=bc)
            back.place(x=203,y=340)  
                
         def algebra1():
            top=Toplevel()
            top.title("Algebra")
            top.geometry("320x410+350+100")
            top.minsize(width=320, height=410)
            top.maxsize(width=320, height=410)
            top.lift()
            top.attributes("-topmost",True)
            l1=Label(top,text=" Fraction",font=('arial',10,'bold'))
            l1.grid(row=0,column=0)
            
            l2=Label(top,text="Factorial",font=('arial',10,'bold'))
            l2.grid(row=1,column=0)
            
            
            entry1=Entry(top,font=('arial',8,'bold'),bd=4)
            entry1.grid(row=0, column=1)

            entry2=Entry(top,font=('arial',8,'bold'),bd=4)
            entry2.grid(row=1, column=1)

         frame1=Frame(ac,width=307,height=140,bd=1,relief="solid")
         frame1.pack(side=TOP)
         
         l=Label(frame1, text="Algebra",fg="black",bd=2,font=('arial',40,'bold'))
         l.place(x=44,y=35)
         
         fraction=Button(ac,text="Fraction",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=fraction)
         fraction.place(x=7,y=150)

         
         factorial=Button(ac,text="Factorial",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=fact)
         factorial.place(x=163,y=150)


         prime=Button(ac,text="Prime",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=prime)
         prime.place(x=7,y=235)

         
         prime=Button(ac,text="Finance",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=finance)
         prime.place(x=163,y=235)
         helpp=Button(ac,text="About",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=about)
         helpp.place(x=7,y=320)

         def bc():
                top.withdraw()
                algebra()
         helpp1=Button(ac,text="Back",font=('arial',10,'bold'),relief='groove',bd=5,width=15,height=3,padx=10,pady=10,command=key3)
         helpp1.place(x=163,y=320)  


    frame1=Frame(root,width=320,height=60,bd=3,relief="raise",bg="silver")
    frame1.pack(side=TOP)

    frame2=Frame(root,width=308,height=110,bd=2,relief="solid")
    frame2.pack(side=TOP)

    frame3=Frame(root,width=320,height=130,bd=2,relief="solid")
    frame3.pack(side=TOP)

    btn1=Button(frame1,text="Numbers",font=('arial',10,'bold'),width=10,height=1,command= numbersystem)
    btn1.grid(row=0,column=0)

    btn2=Button(frame1,text="Converters",font=('arial',10,'bold'),width=12,height=1, command=unitconverter)
    btn2.grid(row=0,column=1)

    btn3=Button(frame1,text="Others",font=('arial',10,'bold'),width=12,height=1,command=  algebra)
    btn3.grid(row=0,column=2)

    l=Label(frame2, text=" CalTalk! ",fg="black",font=('arial',50,'bold'))
    l.place(x=0,y=0)

    l=Label(frame2, text="(Voice Input Based Calculator)",fg="grey",font=('arial',15,'bold'))
    l.place(x=8,y=66)

    l=Label(frame3, text="",fg="green",font=('arial',45,'bold'))
    l.grid(row=0,column=0)

    btn1=Button(frame3,text=" Voice Calculator",font=('arial',14,'bold'),relief='groove',bd=4,width=12,height=4,padx=10,pady=10,command=voicecal)
    btn1.grid(row=0,column=0)


    btn1=Button(frame3,text=" About ",font=('arial',14,'bold'),width=8,relief='groove',bd=4,height=4,padx=10,pady=10,command=about)
    btn1.grid(row=0,column=1)
    btn1=Button(frame3,text=" Simple Calculator",font=('arial',14,'bold'),relief='groove',bd=4,width=12,height=4,padx=10,pady=10,command=other)
    btn1.grid(row=3,column=0)

    btn1=Button(frame3,text=" Help ",font=('arial',14,'bold'),width=8,relief='groove',bd=4,height=4,padx=10,pady=10,command=help)
    btn1.grid(row=3,column=1)

    root.mainloop()
h=Tk()
h.geometry("320x410+350+100")
h.title('Please Wait')
h.attributes("-topmost",True)
#f1=Frame(h,width=320,height=410,bd=2,relief="solid")
#f1.pack(side=TOP)
#f2=Frame(f1,width=308,height=130,bd=2,relief="solid")
#f2.place(x=5,y=100)
l2=Label(h,text='',font=('arial',15,'bold'),height=3,width=25)
l2.grid(row=0,column=0)
l3=Label(h,text='',font=('arial',15,'bold'),height=3,width=25)
l3.grid(row=1,column=0)
l1=Label(h,text='Loading...',font=('arial',15,'bold'),height=5,width=27)
l1.grid(row=8,column=0)
h.minsize(width=320, height=410)
h.maxsize(width=320, height=410)
b1=Button(h,text='click',height=2,width=10,command=yes)
b1.after(1500,yes)
h.mainloop()
