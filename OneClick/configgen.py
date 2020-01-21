from tkinter import *
import tkinter.ttk
from tkinter import filedialog
import os
import shutil
import configparser
from encrdecr import encr_passd

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()
        
        self.master.title('Config Generation')                
                
        choices = ['Yes','No']        
             
        self.naukrilbl = Label(master, text="Naukri.com")
        self.naukrilbl.grid(row=1, column=0)     
                
        self.npopupLabel = Label(master, text="Account Yes/No?")
        self.npopupLabel.grid(row=2, column=0)        
        
        self.npopupmenu = tkinter.ttk.Combobox(master,values=choices, width=17)
        self.npopupmenu.grid(row=2, column=1)
        self.npopupmenu.current(0)                

        self.nunameLabel = Label(master, text="User Name")
        self.nunameLabel.grid(row=3, column=0)

        self.nuname = StringVar()
        self.nunameEntry = Entry(master, textvariable=self.nuname)
        self.nunameEntry.grid(row=3, column=1)
                        
        self.npwdLabel = Label(master, text="Password")
        self.npwdLabel.grid(row=4, column=0)

        self.npwd = StringVar()
        self.npwdEntry = Entry(master, show='*', textvariable=self.npwd)
        self.npwdEntry.grid(row=4, column=1)


        tkinter.ttk.Separator(master, orient="horizontal").grid(row=5, column=0, columnspan=4, sticky='nsew')
        
        self.naukrigflbl = Label(master, text="NaukriGulf.com")
        self.naukrigflbl.grid(row=6, column=0)     
                
        self.ngpopupLabel = Label(master, text="Account Yes/No?")
        self.ngpopupLabel.grid(row=7, column=0)        
        
        self.ngpopupmenu = tkinter.ttk.Combobox(master,values=choices, width=17)
        self.ngpopupmenu.grid(row=7, column=1)
        self.ngpopupmenu.current(0)

        self.ngunameLabel = Label(master, text="User Name")
        self.ngunameLabel.grid(row=8, column=0)

        self.nguname = StringVar()
        self.ngunameEntry = Entry(master, textvariable=self.nguname)
        self.ngunameEntry.grid(row=8, column=1)
                        
        self.ngpwdLabel = Label(master, text="Password")
        self.ngpwdLabel.grid(row=9, column=0)

        self.ngpwd = StringVar()
        self.ngpwdEntry = Entry(master, show='*', textvariable=self.ngpwd)
        self.ngpwdEntry.grid(row=9, column=1)

        tkinter.ttk.Separator(master, orient="horizontal").grid(row=10, column=0, columnspan=4, sticky='nsew')
        
        self.monsterindlbl = Label(master, text="MonsterIndia.com")
        self.monsterindlbl.grid(row=11, column=0)     
                
        self.mipopupLabel = Label(master, text="Account Yes/No?")
        self.mipopupLabel.grid(row=12, column=0)        
        
        self.mipopupmenu = tkinter.ttk.Combobox(master,values=choices, width=17)
        self.mipopupmenu.grid(row=12, column=1)
        self.mipopupmenu.current(0)

        self.miunameLabel = Label(master, text="User Name")
        self.miunameLabel.grid(row=13, column=0)

        self.miuname = StringVar()
        self.miunameEntry = Entry(master, textvariable=self.miuname)
        self.miunameEntry.grid(row=13, column=1)
                        
        self.mipwdLabel = Label(master, text="Password")
        self.mipwdLabel.grid(row=14, column=0)

        self.mipwd = StringVar()
        self.mipwdEntry = Entry(master, show='*', textvariable=self.mipwd)
        self.mipwdEntry.grid(row=14, column=1)
        
        tkinter.ttk.Separator(master, orient="horizontal").grid(row=15, column=0, columnspan=4, sticky='nsew')
        
        self.monstergflbl = Label(master, text="MonsterGulf.com")
        self.monstergflbl.grid(row=16, column=0)     
                
        self.mgpopupLabel = Label(master, text="Account Yes/No?")
        self.mgpopupLabel.grid(row=17, column=0)        
        
        self.mgpopupmenu = tkinter.ttk.Combobox(master,values=choices, width=17)
        self.mgpopupmenu.grid(row=17, column=1)
        self.mgpopupmenu.current(0)

        self.mgunameLabel = Label(master, text="User Name")
        self.mgunameLabel.grid(row=18, column=0)

        self.mguname = StringVar()
        self.mgunameEntry = Entry(master, textvariable=self.mguname)
        self.mgunameEntry.grid(row=18, column=1)
                        
        self.mgpwdLabel = Label(master, text="Password")
        self.mgpwdLabel.grid(row=19, column=0)

        self.mgpwd = StringVar()
        self.mgpwdEntry = Entry(master, show='*', textvariable=self.mgpwd)
        self.mgpwdEntry.grid(row=19, column=1)        
        
        tkinter.ttk.Separator(master, orient="horizontal").grid(row=20, column=0, columnspan=4, sticky='nsew')
        
        self.resumeLabel = Label(master, text="Resume File")
        self.resumeLabel.grid(row=21, column=0)

        self.resume = StringVar()
        self.resumeEntry = Entry(master,textvariable=self.resume)
        self.resumeEntry.grid(row=21, column=1)    

        def fileDialog():
     
            self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
            (("pdf files","*.pdf"),("doc files","*.docx"),("doc files","*.doc"),("all files","*.*")) )
            self.resume.set(os.path.basename(self.filename))

        self.button = Button(master, text = "Browse A File",command = fileDialog)
        self.button.grid(column = 3, row = 21)            
        
        tkinter.ttk.Separator(master, orient="horizontal").grid(row=22, column=0, columnspan=2, sticky='nsew')                
        
        def buttonClick():
                                    
            shutil.copyfile(self.filename, os.path.join(os.getcwd(),os.path.basename(self.filename)))
            
            config = configparser.ConfigParser()
            cfgfile = open('config.ini', 'w')
            
            config.add_section('naukri')
            config.set('naukri', 'account', self.npopupmenu.get())
            config.set('naukri', 'username', self.nuname.get())
            config.set('naukri', 'password', encr_passd(self.npwd.get()))
            
            config.add_section('naukrigulf')
            config.set('naukrigulf', 'account', self.ngpopupmenu.get())
            config.set('naukrigulf', 'username', self.nguname.get())
            config.set('naukrigulf', 'password', encr_passd(self.ngpwd.get()))
            
            config.add_section('monsterindia')
            config.set('monsterindia', 'account', self.mipopupmenu.get())
            config.set('monsterindia', 'username', self.miuname.get())
            config.set('monsterindia', 'password', encr_passd(self.mipwd.get()))
            
            config.add_section('monstergulf')
            config.set('monstergulf', 'account', self.mgpopupmenu.get())
            config.set('monstergulf', 'username', self.mguname.get())
            config.set('monstergulf', 'password', encr_passd(self.mgpwd.get()))
            
            config.add_section('resume')
            config.set('resume', 'filename', os.path.basename(self.filename))
            
            config.write(cfgfile)
            cfgfile.close()
            
            self.master.destroy()

        self.submitButton = Button(master, text="Submit", command=buttonClick)
        self.submitButton.grid()

if __name__ == "__main__":
    guiFrame = GUI()    
    guiFrame.mainloop()