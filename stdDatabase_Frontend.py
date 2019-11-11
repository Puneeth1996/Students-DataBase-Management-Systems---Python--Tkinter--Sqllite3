from tkinter import *
import tkinter.messagebox
import stdDatabase_Backend

class Student:

     def __init__(self,root):
          self.root=root
          self.root.title("STUDENTS DATABASE MANAGEMENT SYSTEM")
          self.root.geometry("1350x750+0+0")
          self.root.config(bg="cadet blue")

          stdID=StringVar()
          FIRSTNAME=StringVar()
          SURNAME=StringVar()
          DOB=StringVar() 
          AGE=StringVar()
          GENDER=StringVar()
          MOBILE=StringVar()


          #*********************************************Function********************#

          def iExit():
               print('iExit')
               iExit=tkinter.messagebox.askyesno("STUDENTS DATABASE MANAGEMENT SYSTEM","confirm if you want to exit")
               if iExit > 0:
                    root.destroy()
                    return

          def clearData():
               print('clearData')
               self.txtstdID.delete(0,END)
               self.txtFna.delete(0,END)
               self.txtSna.delete(0,END)
               self.txtDoB.delete(0,END)
               self.txtAge.delete(0,END)
               self.txtGen.delete(0,END)
               self.txtMob.delete(0,END)

          def addData():
               print('addData')
               if(len(stdID.get())!=0):
                    stdDatabase_Backend.addStdRec(stdID.get(),FIRSTNAME.get(),SURNAME.get(),DOB.get(),AGE.get(),GENDER.get(),MOBILE.get())
                    print(stdID.get(),FIRSTNAME.get(),SURNAME.get(),DOB.get(),AGE.get(),GENDER.get(),MOBILE.get())
                    print(StudentRec)
                    studentlist.delete(0,END)
                    studentlist.insert(END,(stdID.get(),FIRSTNAME.get(),SURNAME.get(),DOB.get(),AGE.get(),GENDER.get(),MOBILE.get()))


          def DisplayData():
               print('DisplayData')
               print(StudentRec)
               studentlist.delete(0,END)
               for row in stdDatabase_Backend.viewData():
                    studentlist.insert(END,row,str(""))


          def StudentRec(event):
               print('StudentRec')
               global sd
               searchStd=studentlist.curselection()[0]
               sd=studentlist.get(searchStd )

               self.txtstdID.delete(0,END)
               self.txtstdID.insert(END,sd[1])
               self.txtFna.delete(0,END)
               self.txtFna.insert(END,sd[2])
               self.txtSna.delete(0,END)
               self.txtSna.insert(END,sd[3])
               self.txtDoB.delete(0,END)
               self.txtDoB.insert(END,sd[4])
               self.txtAge.delete(0,END)
               self.txtAge.insert(END,sd[5])
               self.txtGen.delete(0,END)
               self.txtGen.insert(END,sd[6])
               self.txtMob.delete(0,END)
               self.txtMob.insert(END,sd[7])

          def DeleteData():
               print(StudentRec)
               print('DeleteData')
               if(len(stdID.get())!=0):
                    print(len(stdID.get()))
                    stdDatabase_Backend.deleteRec(sd[0])
                    clearData()
                    DisplayData()

          def searchDatabase():
               print(StudentRec)
               print('searchDatabase')
               studentlist.delete(0,END)
               for row in stdDatabase_Backend.searchData(stdID.get(),FIRSTNAME.get(),SURNAME.get(),DOB.get(),AGE.get(),GENDER.get(),MOBILE.get()):
                    studentlist.insert(END,row,str(""))

          def update():
               print(StudentRec)
               print('update')
               if(len(stdID.get())!=0):
                    stdDatabase_Backend.deleteRec(sd[0])
               if(len(stdID.get())!=0):
                    stdDatabase_Backend.addStdRec(stdID.get(),FIRSTNAME.get(),SURNAME.get(),DOB.get(),AGE.get(),GENDER.get(),MOBILE.get())
                    studentlist.delete(0,END)
                    studentlist.insert(END,(stdID.get(),FIRSTNAME.get(),SURNAME.get(),DOB.get(),AGE.get(),GENDER.get(),MOBILE.get()))   
                    
                    
                    

          #*********************************************frame********************#
          MainFrame=Frame(self.root,bg="cadet blue")
          MainFrame.grid()

          TitFrame=Frame(MainFrame,bd=2,padx=54,pady=8,bg="ghost white",relief=RIDGE)
          TitFrame.pack(side=TOP)

          self.lblTit=Label(TitFrame,font=("arial",40,"bold"),text="STUDENT DATABASE MANAGEMENT SYSTEM",bg="ghost white")
          self.lblTit.grid()

          ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="ghost white",relief=RIDGE)
          ButtonFrame.pack(side=BOTTOM)

          DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,bg="cadet blue",relief=RIDGE)
          DataFrame.pack(side=BOTTOM)

          DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,bg="ghost white",relief=RIDGE,font=("arial",20,"bold"),text="student Info\n")
          DataFrameLEFT.pack(side=LEFT)

          DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=20,bg="ghost white",relief=RIDGE,font=("arial",20,"bold"),text="student Details\n")
          DataFrameRIGHT.pack(side=RIGHT)
          #---------------------------------------------lbels and entry widget---------------------------#

          self.lblstdID=Label(DataFrameLEFT,font=("arial",20,"bold"),text="STUDENT ID",padx=2,pady=2,bg="ghost white")
          self.lblstdID.grid(row=0,column=0,sticky=W)
          self.txtstdID=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=stdID,width=39)
          self.txtstdID.grid(row=0,column=1)
                              
          self.lblFna=Label(DataFrameLEFT,font=("arial",20,"bold"),text="FIRSTNAME",padx=2,pady=2,bg="ghost white")
          self.lblFna.grid(row=1,column=0,sticky=W)
          self.txtFna=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=FIRSTNAME,width=39)
          self.txtFna.grid(row=1,column=1)
                                                  
          self.lblSna=Label(DataFrameLEFT,font=("arial",20,"bold"),text="SURNAME",padx=2,pady=2,bg="ghost white")
          self.lblSna.grid(row=2,column=0,sticky=W)
          self.txtSna=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=SURNAME,width=39)
          self.txtSna.grid(row=2,column=1)

          self.lblDoB=Label(DataFrameLEFT,font=("arial",20,"bold"),text="DOB",padx=2,pady=2,bg="ghost white")
          self.lblDoB.grid(row=3,column=0,sticky=W)
          self.txtDoB=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=DOB,width=39)
          self.txtDoB.grid(row=3,column=1)

          self.lblAge=Label(DataFrameLEFT,font=("arial",20,"bold"),text="AGE",padx=2,pady=2,bg="ghost white")
          self.lblAge.grid(row=4,column=0,sticky=W)
          self.txtAge=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=AGE,width=39)
          self.txtAge.grid(row=4,column=1)

          self.lblGen=Label(DataFrameLEFT,font=("arial",20,"bold"),text="GENDER",padx=2,pady=2,bg="ghost white")
          self.lblGen.grid(row=5,column=0,sticky=W)
          self.txtGen=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=GENDER,width=39)
          self.txtGen.grid(row=5,column=1)

          self.lblMob=Label(DataFrameLEFT,font=("arial",20,"bold"),text="MOBILE",padx=2,pady=2,bg="ghost white")
          self.lblMob.grid(row=6,column=0,sticky=W)
          self.txtMob=Entry(DataFrameLEFT,font=("arial",20,"bold"),textvariable=MOBILE,width=39)
          self.txtMob.grid(row=6,column=1)

          #---------------------------------------------listbox and scrollbar widget---------------------------#

          scrollbar=Scrollbar(DataFrameRIGHT)
          scrollbar.grid(row=0,column=1,sticky="ns")

          studentlist=Listbox(DataFrameRIGHT,width=41,height=16,font=("arial",12,"bold"),yscrollcommand=scrollbar.set)
          studentlist.bind('<<ListboxSelect>>',StudentRec)
          studentlist.grid(row=0,column=0,padx=8)
          scrollbar.config(command=studentlist.yview)

          #---------------------------------------------Button widget---------------------------#
          
          self.btnAddData=Button(ButtonFrame,text="Add New",font=("arial",20,"bold"),height=1,width=10,bd=4,command=addData)
          self.btnAddData.grid(row=0,column=0)

          self.btnDisplayData=Button(ButtonFrame,text="Display",font=("arial",20,"bold"),height=1,width=10,bd=4,command=DisplayData)
          self.btnDisplayData.grid(row=0,column=1)

          self.btnClearData=Button(ButtonFrame,text="Clear",font=("arial",20,"bold"),height=1,width=10,bd=4,command=clearData)
          self.btnClearData.grid(row=0,column=2)

          self.btnDeleteData=Button(ButtonFrame,text="Delete",font=("arial",20,"bold"),height=1,width=10,bd=4,command=DeleteData)
          self.btnDeleteData.grid(row=0,column=3)

          self.btnSearchData=Button(ButtonFrame,text="Search",font=("arial",20,"bold"),height=1,width=10,bd=4,command=searchDatabase)
          self.btnSearchData.grid(row=0,column=4)

          self.btnUpdateData=Button(ButtonFrame,text="Update",font=("arial",20,"bold"),height=1,width=10,bd=4,command=update)
          self.btnUpdateData.grid(row=0,column=5)

          self.btnExitData=Button(ButtonFrame,text="Exit",font=("arial",20,"bold"),height=1,width=10,bd=4,command=iExit)
          self.btnExitData.grid(row=0,column=6)






if __name__=="__main__":
     root=Tk()
     application=Student(root)
     root.mainloop()          
