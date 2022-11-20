from tkinter import *
root = Tk()
root.configure(bg='blue')
root.geometry('1000x900')
root.title("Course Recommender")
s = "Click 1 if Science Student,Click 2 if Commerce Student,Click 3 if Art Student"
et = Label(root,text = s.upper()).grid(row = 1,column = 5)
global phys
global maths
global bios
#button 1 entry
def get_entry1():
   
    lst = list(sci.get().split())
    phys = int(lst[0])
    maths = int(lst[1])
    bios = int(lst[2])
    chems = int(lst[3])
    yr = int(lst[4])
    root1 = Tk()
    root1.geometry('1000x900')
    root1.configure(bg='white')
    root1.title("SCIENCE")
    
    if phys>50 and chems>50 and maths>50 and yr== 4:
        a= 7
        statements = ['Do you like coding?Are you curious on knowing how apps work? Do you like working on data? If yes enter 1','Do you like electrical circuits?Are you curious about power grids? Do you like learning about electromagnetism? If yes enter 2',"Do you like designing electronic circuits?Are you curious on knowing about integrated circuits and embedded systems?If yes enter 3","Do you like designing and constructing structural components?Do you want to contribute to infrastructure around you?If yes enter 4","Do you like to design and manafacture mechanical systems?Did topics like fluid mechanics and thermodynamics fascinate you? If yes enter 5","Do you like working with genes?Are you curious about biochemistry? If yes enter 6","Do you like to make pharmaceutical products?Are you curious about constituents of medicine?If yes enter 7"]
        for i in statements:
            l = Label(root1,text = i).grid(row = a,column = 5 )
            a+=1
       
        def click1(x):
            if x == '1':
                l = Label(root1,text ="Opt for Computer Science Engineering.Wish You Loads Of Luck!",fg = 'red').grid(row =15,column=5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1 
            elif x =='2':
                l = Label(root1,text ="Opt for Electrical Engineering.Wish You Loads Of Luck!",fg = 'red').grid(row = 16,column =5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1  
            elif x == '3':
                l = Label(root1,text ="Opt for Electronic Engineering.Wish You Loads Of Luck!",fg = 'red').grid(row = 17,column =5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1 
            elif x == '4':
                l = Label(root1,text ="Opt for Civil Engineering.Wish You Loads Of Luck!",fg = 'red').grid(row = 18,column=5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1 
            elif x == '5':
                l = Label(root1,text ="Opt for Mechanical Engineering.Wish You Loads Of Luck!",fg = 'red').grid(row =19,column =5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1  
            elif x == '6':
                l = Label(root1,text ="Opt for Biotechnology Engineering.Wish You Loads Of Luck!",fg = 'red').grid(row = 20,column =5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1  
            elif x == '7':
                l = Label(root1,text ="Opt for B.Pharma Degree.Wish you Loads of Luck!",fg = 'red').grid(row = 21,column =5)
                for i in statements:
                  l = Label(root1,text = i,fg='white',bg='white').grid(row = a,column = 5 )
                  a+=1                 
            
                
        button1 = Button(root1,text = '1',command = lambda : click1('1')).grid(row = 22,column = 2)
        button2 = Button(root1,text = '2',command = lambda : click1('2')).grid(row = 22,column = 5)
        button3 = Button(root1,text = '3',command = lambda : click1('3')).grid(row = 22,column = 7)
        button4 = Button(root1,text = '4',command = lambda : click1('4')).grid(row = 23,column = 2)
        button5 = Button(root1,text = '5',command = lambda : click1('5')).grid(row = 23,column = 5)
        button6 = Button(root1,text = '6',command = lambda : click1('6')).grid(row = 23,column = 7)
        button7 = Button(root1,text = '7',command = lambda : click1('7')).grid(row = 24,column = 2)
    elif phys>50 and chems>50 and bios>50 and yr>=5:
        
        a= 7
        #statements = [ou like learning about ? If yes enter 2',"Do you like designing electronic circuits?Are you curious on knowing about integrated circuits and embedded systems?If yes enter 3","Do you like designing and constructing structural components?Do you want to contribute to infrastructure around you?If yes enter 4","Do you like to design and manafacture mechanical systems?Did topics like fluid mechanics and thermodynamics fascinate you? If yes enter 5","Do you like working with genes?Are you curious about biochemistry? If yes enter 6","Do you like to make pharmaceutical products?Are you curious about constituents of medicine?If yes enter 7"]
        statements = ["Do you aspire to be a doctor?Are you interested in knowing more about human physiology?If yes enter 1","Do you aspire to be a dentist?Are you interested in knowing more about dental histology? If yes enter 2","Are you interested in learning in depth about homeopathic medicine?If yes enter 3","Do you like nuturing animals?Have you wondered about animal physiology?If yes enter 4","Do you feel Ayurveda is fascinating?If yes enter 5","Do you like healing people's pain points?Are you curious about kinesiology?If yes enter 6"]
        for i in statements:
            l = Label(root1,text = i).grid(row = a,column = 5 )
            a+=1
       
        def click1(x):
            if x == '1':
                l = Label(root1,text ="Opt for MBBS course.Wish You Loads Of Luck!",fg = 'red' ).grid(row =15,column=5)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            elif x =='2':
                l = Label(root1,text ="Opt for MDS degree.Wish You Loads Of Luck!",fg = 'red').grid(row = 16,column =5)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1
            elif x == '3':
                l = Label(root1,text ="Opt for BHMS.Wish You Loads Of Luck!",fg = 'red').grid(row = 17,column =5)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            elif x == '4':
                l = Label(root1,text ="Opt for  BAMS course.Wish You Loads Of Luck!",fg = 'red').grid(row = 18,column=5)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            elif x == '5':
                l = Label(root1,text ="Opt for Vetinary sciences.Wish You Loads Of Luck!",fg = 'red').grid(row =19,column =5)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            elif x == '6':
                l = Label(root1,text ="Opt for Physiotherapy.Wish You Loads Of Luck!",fg = 'red').grid(row = 20,column =5)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            
            
                
        button1 = Button(root1,text = '1',command = lambda : click1('1')).grid(row = 22,column = 2)
        button2 = Button(root1,text = '2',command = lambda : click1('2')).grid(row = 22,column = 5)
        button3 = Button(root1,text = '3',command = lambda : click1('3')).grid(row = 22,column = 7)
        button4 = Button(root1,text = '4',command = lambda : click1('4')).grid(row = 23,column = 2)
        button5 = Button(root1,text = '5',command = lambda : click1('5')).grid(row = 23,column = 5)
        button6 = Button(root1,text = '6',command = lambda : click1('6')).grid(row = 23,column = 7)
        #button7 = Button(root,text = '7',command = lambda : click1('7')).grid(row = 24,column = 2)
        
    elif yr == 3:
        t1 = Text(root1, height=5, width=30)
        label= Label(root1,text="Select the desired Option",bg="white")
        label.grid(row=0,column=1)
        choices=["Do you aspire to pursue a career related to science?If yes enter 1","Do you want to learn about computer and its applications?If yes enter 2","Do you to aspire to join the naval and air forces of our country?If yes enter 3","Do you want to pursue law?If yes enter 4"]
        a=8
        for i in choices:
            lbl = Label(root1,text=i)
            lbl.grid(row=a,column=1)
            a+=1
        def click(choice):
            if choice == "1":
                
                lbl = Label(root1, text="Opt for a B.Sc Degree.Wish You Loads Of Luck!",fg = 'red')
                lbl.grid(row=7,column=1)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            elif choice == "2":
                lbl = Label(root1, text="Opt for BCA Degree.Wish You Loads Of Luck!",fg = 'red')
                lbl.grid(row=7, column=1)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1  
            elif choice == "3":
                lbl = Label(root1, text="Join NDA.Wish You Loads Of Luck!",fg = 'red')
                lbl.grid(row=7, column=1)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1 
            elif choice == "4":
                lbl = Label(root1, text="Opt for LLB Course.Wish You Loads Of Luck!",fg = 'red')
                lbl.grid(row=7, column=1)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1  

            else:
                lbl = Label(root1,text="Enter one of the options given")
                lbl.grid(row=7, column=1)
                for i in statements:
                 l = Label(root1,text = i,bg='white',fg='white').grid(row = a,column = 5 )
                 a+=1  


        # define buttons
        bt1 = Button(root1, text="1", padx=40, pady=20, command=lambda: click("1"))  # callback
        bt2 = Button(root1, text="2", padx=40, pady=20, command=lambda: click("2"))  # callback
        bt3 = Button(root1, text="3", padx=40, pady=20, command=lambda: click("3"))  # callback
        bt4 = Button(root1, text="4", padx=40, pady=20, command=lambda: click("4"))  # callback



        bt1.grid(row=2, column=0)
        bt2.grid(row=2, column=1)
        bt3.grid(row=2, column=2)
        bt4.grid(row=3, column=0)


def commerce():
    root2 = Tk()
    root2.geometry('1000x900')
    root2.configure(bg='white')
    root2.title("COMMERCE")
    t1 = Text(root2, height=5, width=30)
    label= Label(root2,text="Select the desired Option",bg="white")
    label.grid(row=0,column=1)
    choices=["Do you want to pursue a career in commerce, accounting, finance, banking and insurance?,If yes enter 1","Do you want to become a Chartered Accountant,If yes enter 2","Do you want to become a Cost and Management Accountant ,If yes enter 3","Do you want to learn about business adminstration,If yes enter 4","Do you want to become a Company Secretary,If yes enter 5","Do you want to learn about Economics?If yes enter 6","Do you want to become a Certified Financial Planner (CFP),If yes enter 7"]
    a=8
    for i in choices:
        lbl = Label(root2,text=i)
        lbl.grid(row=a,column=1)
        a+=1
    def click(choice):
        if choice == "1":

            lbl = Label(root2, text="Opt for B.Com Degree.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7,column=1)
            a=8
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1           
            
        elif choice == "2":
            lbl = Label(root2, text="Opt for CA foundation course.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1           
        elif choice == "3":
            lbl = Label(root2, text="Opt for CMA Foundation Course.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1            
        elif choice == "4":
            lbl = Label(root2, text="Opt for BBA Degree.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1            
        elif choice == "5":
            lbl = Label(root2, text="Opt for CS Foundation Course.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1            
        elif choice == "6":
            lbl = Label(root2, text="Opt for Bachelor of Economics Degree.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1           
        elif choice == "7":
            lbl = Label(root2, text="Register for CFP through Regular Pathway.Wish You Loads Of Luck!",fg = 'red')
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1            
        else:
            lbl = Label(root2, text="Enter one of the options given")
            lbl.grid(row=7, column=1)
            for i in choices:
                lbl = Label(root2,text=i,bg="white",fg='white')
                lbl.grid(row=a,column=1)
                a+=1            


    # define buttons
    bt1 = Button(root2, text="1", padx=40, pady=20, command=lambda: click("1"))  # callback
    bt2 = Button(root2, text="2", padx=40, pady=20, command=lambda: click("2"))  # callback
    bt3 = Button(root2, text="3", padx=40, pady=20, command=lambda: click("3"))  # callback
    bt4 = Button(root2, text="4", padx=40, pady=20, command=lambda: click("4"))  # callback
    bt5 = Button(root2, text="5", padx=40, pady=20, command=lambda: click("5"))  # callback
    bt6 = Button(root2, text="6", padx=40, pady=20, command=lambda: click("6"))  # callback
    bt7 = Button(root2, text="7", padx=40, pady=20, command=lambda: click("7"))  # callback


    bt1.grid(row=2, column=0)
    bt2.grid(row=2, column=1)
    bt3.grid(row=2, column=2)

    bt4.grid(row=3, column=0)
    bt5.grid(row=3, column=1)
    bt6.grid(row=3, column=2)

    bt7.grid(row=4, column=0)
    
def arts():
    root3 = Tk()
    root3.title("ARTS")
    root3.geometry('1000x900')
    root3.configure(bg='white')
    t1 = Text(root3, height=5, width=30)
    label= Label(root3,text="Select the desired Option",bg="white")
    label.grid(row=0,column=1)
    choices=["Are you interested in Sales, Marketing, Finance?If yes enter 1","Do you want to make wonders in Film Making, Music, Dance, Painting & Sculpting, Pottery & Ceramics, Creative Writing, Animation,If yes enter 2","Do you want to shake the country by thrilling and exciting news,If yes then enter 3","If you are interested about conceiving the idea of an event, planning it, promoting the event,then enter 4","If you are good and interested at interpersonal skills, communication skills, negotiation skills, and customer service skills,then enter 5","Do you want to rock in humanities, social sciences, and liberal arts ,then enter 6"]
    a=7
    for i in choices:
        lbl = Label(root3,text=i)
        lbl.grid(row=a,column=1)
        a+=1
    def click(choice):
        if choice == "1":
            
            lbl = Label(root3, text="opt for Bachelor of Business Administration (B.B.A.) course. Best of luck!",fg = 'red')
            lbl.grid(row=15,column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1 
        elif choice == "2":
            lbl = Label(root3, text="opt for Bachelor of Fine Arts(B.F.A) course.All the Best!",fg = 'red')
            lbl.grid(row=15, column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1
        elif choice == "3":
            lbl = Label(root3, text="opt for Journalism and Mass Communication course.Best of Luck",fg = 'red')
            lbl.grid(row=15, column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1 
        elif choice == "4":
            lbl = Label(root3, text="opt for Event Management course. Best of Luck",fg = 'red')
            lbl.grid(row=15, column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1 
        elif choice == "5":
            lbl = Label(root3, text="opt for Bachelor of Hotel Management(B.H.M) course.Best of luck!",fg = 'red')
            lbl.grid(row=15, column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1
        elif choice == "6":
            lbl = Label(root3, text="opt for Bachelor of Arts (B.A.) course.All the Best!",fg = 'red')
            lbl.grid(row=15, column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1

        else:
            lbl = Label(root3, text="Enter one of the options given")
            lbl.grid(row=15, column=1)
            for i in choices:
              lbl = Label(root3,text=i,fg='white',bg='white')
              lbl.grid(row=a,column=1)
              a+=1


# define buttons
    bt1 = Button(root3, text="1", padx=40, pady=20, command=lambda: click("1"))  # callback
    bt2 = Button(root3, text="2", padx=40, pady=20, command=lambda: click("2"))  # callback
    bt3 = Button(root3, text="3", padx=40, pady=20, command=lambda: click("3"))  # callback
    bt4 = Button(root3, text="4", padx=40, pady=20, command=lambda: click("4"))  # callback
    bt5 = Button(root3, text="5", padx=40, pady=20, command=lambda: click("5"))  # callback
    bt6 = Button(root3, text="6", padx=40, pady=20, command=lambda: click("6"))  # callback



    bt1.grid(row=2, column=0)
    bt2.grid(row=2, column=1)
    bt3.grid(row=2, column=2)

    bt4.grid(row=3, column=0)
    bt5.grid(row=3, column=1)
    bt6.grid(row=3, column=2)

    
def bt1():
    
    global sci
    lab = Label(root,text = 'Enter PCMB marks and years willing to study seperated by space').grid(row = 3,column = 5)
    sci = Entry(root,width = 100)
    sci.grid(row=10,column = 5)
    ent = Button(root,text = 'Enter',command = get_entry1).grid(row = 4,column = 5)

def bt2():
    global sci
    #lab = Label(root,text = 'Enter PCMB marks and years willing to study seperated by space').grid(row = 3,column = 5)
    #sci = Entry(root,width = 100)
    #sci.grid(row=10,column = 5)
    #ent = Button(root,text = 'Enter',command = get_entry1).grid(row =4,column = 5)
    
def bt3():
    global sci
    #lab = Label(root,text = 'EnterPCMB marks and years willing to study seperated by space').grid(row = 3,column = 5)
    #sci = Entry(root,width = 100)
    #sci.grid(row=10,column = 5)
    #ent = Button(root,text = 'Enter',command = get_entry).grid(row = 4,column = 5)
    
bt1 = Button(root,text = '1',command = bt1).grid(row = 5,column = 2,columnspan = 1)
bt2 = Button(root,text = '2',command = commerce).grid(row = 5,column = 5,columnspan = 1)
bt3 = Button(root,text = '3',command = arts).grid(row = 5,column = 9,columnspan = 1)

root.mainloop()
