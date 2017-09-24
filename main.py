#!/usr/bin/python
# -*- coding:utf-8 -*-
import Tkinter
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import sys
import codecs
import webbrowser
import os

class PadHn(object):
    def __init__(self,Vin,*args,**kwargs):
        self.WI = Vin
        self.colF='#e9ebee'
        self.WI.title('Simple Visor De Fotos || Información')
        self.WI.geometry('435x165')
        self.WI.maxsize(width=435,height=165)
        self.WI.minsize(width=435,height=165)
        self.PhotoIco = PhotoImage(file='bin/images/favicon.gif',format='gif')
        self.WI.configure(bg=self.colF)
        self.WI.tk.call('wm','iconphoto',self.WI._w,self.PhotoIco)
        self.WI = Frame(Vin)
        self.WI.pack(side="top",fill="both",expand=True)
        self.WI.grid_rowconfigure(0,weight=1)
        self.WI.grid_columnconfigure(0,weight=1)
        self.text0=Label(self.WI,text='Simple Visor De Fotos Todos Los Derechos Reservados',bg=self.colF,fg='red',font=('Arial',13))
        self.text0.place(x=10,y=10)
        self.text1=Label(self.WI,text='Autor: Jhon Jair Contreras Salgado',bg=self.colF,fg='#066',font=('Arial',13))
        self.text1.place(x=10,y=30)
        self.text2=Label(self.WI,text='Email: maybetoca@gmail.com',bg=self.colF,fg='#066',font=('Arial',13))
        self.text2.place(x=10,y=50)
        self.text3=Label(self.WI,text='Versión: 1.0',bg=self.colF,fg='#066',font=('Arial',13))
        self.text3.place(x=10,y=70)
        self.text4=Label(self.WI,text='Licencia: GPL',bg=self.colF,fg='#066',font=('Arial',13))
        self.text4.place(x=10,y=90)
        self.text5=Label(self.WI,text='Copyright: © 2017',bg=self.colF,fg='#066',font=('Arial',13))
        self.text5.place(x=10,y=110)
        self.text6=Label(self.WI,text='Name: Simple Visor De Fotos',bg=self.colF,fg='#066',font=('Arial',13))
        self.text6.place(x=10,y=133)
        self.WI.mainloop()

class HanV(object):
    def InsertF(self):
        self.name= askopenfilename(**self.opts)
        if (self.name)!='':
            if(self.NumbL)==0:
                self.For1=self.name
                self.For1a=PhotoImage(file=self.For1,format='gif')
                self.For1a = self.For1a.zoom(10)
                self.For1a = self.For1a.subsample(22)
                self.NumbL = self.NumbL+1
                self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                self.LaIm1=Label(bg='#066',width=385,height=375,image=self.For1a)
                self.LaIm1.place(x=80,y=20)
            elif(self.NumbL)==1:
                self.For2=self.name
                self.For2a=PhotoImage(file=self.For2,format='gif')
                self.For2a = self.For2a.zoom(3)
                self.For2a = self.For2a.subsample(15)
                self.NumbL = self.NumbL+1
                self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                self.LaIm2=Label(bg='#066',width=140,height=150,image=self.For2a)
                self.LaIm2.place(x=45,y=430)
            else:
                if(self.NumbL)==2:
                    self.For3=self.name
                    self.For3a=PhotoImage(file=self.For3,format='gif')
                    self.For3a = self.For3a.zoom(3)
                    self.For3a = self.For3a.subsample(15)
                    self.NumbL = self.NumbL+1
                    self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                    self.LaIm3=Label(bg='#066',width=140,height=150,image=self.For3a)
                    self.LaIm3.place(x=205,y=430)
                else:
                    if(self.NumbL)==3:
                        self.For4=self.name
                        self.For4a=PhotoImage(file=self.For4,format='gif')
                        self.For4a = self.For4a.zoom(3)
                        self.For4a = self.For4a.subsample(15)
                        self.NumbL = 0
                        self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                        self.LaIm4=Label(bg='#066',width=140,height=150,image=self.For4a)
                        self.LaIm4.place(x=365,y=430)
        else:
            self.MensErroD = tkMessageBox.showerror('Simple Visor De Fotos','Por Favor Selecciona Una Foto')
            return self.MensErroD

    def NextI(self):
        if((self.For1)and(self.For2)and(self.For3)and(self.For4))== '':
            self.Ms = tkMessageBox.showerror('Simple Visor De Fotos','Por Favor Insertar Las 4 Fotos')
            return self.Ms
        else:
            if(self.Op)==1:
                self.let1=self.For2
                self.lt1=PhotoImage(file=self.let1,format='gif')
                self.lt1 = self.lt1.zoom(10)
                self.lt1 = self.lt1.subsample(22)
                self.Op=self.Op+1
                self.LaIm1=Label(bg='#066',width=385,height=375,image=self.lt1).place(x=80,y=20)
                
            elif(self.Op)==2:
                self.let2=self.For3
                self.lt2=PhotoImage(file=self.let2,format='gif')
                self.lt2 = self.lt2.zoom(10)
                self.lt2 = self.lt2.subsample(22)
                self.Op=self.Op+1
                self.LaIm1=Label(bg='#066',width=385,height=375,image=self.lt2).place(x=80,y=20)
            else:
                if(self.Op)==3:
                    self.let3=self.For4
                    self.lt3=PhotoImage(file=self.let3,format='gif')
                    self.lt3 = self.lt3.zoom(10)
                    self.lt3 = self.lt3.subsample(22)
                    self.Op=self.Op+1
                    self.LaIm1=Label(bg='#066',width=385,height=375,image=self.lt3).place(x=80,y=20)
                else:
                    if(self.Op)==4:
                        self.let4=self.For1
                        self.lt4=PhotoImage(file=self.let4,format='gif')
                        self.lt4 = self.lt4.zoom(10)
                        self.lt4 = self.lt4.subsample(22)
                        self.Op=1
                        self.LaIm1=Label(bg='#066',width=385,height=375,image=self.lt4).place(x=80,y=20)
        
    def prev(self):
        if((self.For1)and(self.For2)and(self.For3)and(self.For4))== '':
            self.Ms = tkMessageBox.showerror('Simple Visor De Fotos','Por Favor Insertar Las 4 Fotos')
            return self.Ms
        else:
            if(self.Op)==1:
                self.letr1=self.For4
                self.ltr1=PhotoImage(file=self.letr1,format='gif')
                self.ltr1 = self.ltr1.zoom(10)
                self.ltr1 = self.ltr1.subsample(22)
                self.Op=4
                self.LaIm1=Label(bg='#066',width=385,height=375,image=self.ltr1).place(x=80,y=20)
                
            elif(self.Op)==4:
                self.letr2=self.For3
                self.ltr2=PhotoImage(file=self.letr2,format='gif')
                self.ltr2 = self.ltr2.zoom(10)
                self.ltr2 = self.ltr2.subsample(22)
                self.Op=3
                self.LaIm1=Label(bg='#066',width=385,height=375,image=self.ltr2).place(x=80,y=20)
            else:
                if(self.Op)==3:
                    self.letr3=self.For2
                    self.ltr3=PhotoImage(file=self.letr3,format='gif')
                    self.ltr3 = self.ltr3.zoom(10)
                    self.ltr3 = self.ltr3.subsample(22)
                    self.Op=2
                    self.LaIm1=Label(bg='#066',width=385,height=375,image=self.ltr3).place(x=80,y=20)
                else:
                    if(self.Op)==2:
                        self.letr4=self.For1
                        self.ltr4=PhotoImage(file=self.letr4,format='gif')
                        self.ltr4 = self.ltr4.zoom(10)
                        self.ltr4 = self.ltr4.subsample(22)
                        self.Op=1
                        self.LaIm1=Label(bg='#066',width=385,height=375,image=self.ltr4).place(x=80,y=20)

    def DelF(self):
        if((self.For1)and(self.For2)and(self.For3)and(self.For4))== '':
            self.Ms1 = tkMessageBox.showerror('Simple Visor De Fotos','Por Favor Insertar Las 4 Fotos')
            return self.Ms1
        else:
            if(self.Op)==1:
                if tkMessageBox.askyesno('Simple Visor De Fotos','¿Esta Seguro Que Quiere Eliminar La Foto1 ?'):
                    self.Ers=os.remove(self.For1)
                    self.Msu=tkMessageBox.showinfo('Simple Visor De Fotos','Foto Eliminada Correctamente')
                    self.LaIm1=Label(bg='#066',width=55,height=25).place(x=80,y=20)
                    self.NumbL=0
                    self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                    return self.Ers,self.Msu
                else:
                    return
            elif(self.Op)==2:
                if tkMessageBox.askyesno('Simple Visor De Fotos','¿Esta Seguro Que Quiere Eliminar La Foto2 ?'):
                    self.Ers1=os.remove(self.For2)
                    self.Msu1=tkMessageBox.showinfo('Simple Visor De Fotos','Foto Eliminada Correctamente')
                    self.LaIm2=Label(bg='#066',width=20,height=10).place(x=45,y=430)
                    self.NumbL=1
                    self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                    return self.Ers1,self.Msu1
                else:
                    return
            else:
                if(self.Op)==3:
                    if tkMessageBox.askyesno('Simple Visor De Fotos','¿Esta Seguro Que Quiere Eliminar La Foto3 ?'):
                        self.Ers2=os.remove(self.For3)
                        self.Msu2=tkMessageBox.showinfo('Simple Visor De Fotos','Foto Eliminada Correctamente')
                        self.LaIm3=Label(bg='#066',width=20,height=10).place(x=205,y=430)
                        self.NumbL=2
                        self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                        return self.Ers2,self.Msu2
                    else:
                        return
                else:
                    if(self.Op)==4:
                        if tkMessageBox.askyesno('Simple Visor De Fotos','¿Esta Seguro Que Quiere Eliminar La Foto4 ?'):
                            self.Ers3=os.remove(self.For4)
                            self.Msu3=tkMessageBox.showinfo('Simple Visor De Fotos','Foto Eliminada Correctamente')
                            self.LaIm4=Label(bg='#066',width=20,height=10).place(x=365,y=430)
                            self.NumbL=3
                            self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
                            return self.Ers3,self.Msu3
                    else:
                        return
    def Facebook(self):
        self.FaceC=webbrowser.open('https://www.facebook.com/PeicelGroup',new=0,autoraise=True)
        return self.FaceC
    
    def Twitter(self):
        self.Twit=webbrowser.open('https://twitter.com/peicel_group',new=0,autoraise=True)
        return self.Twit
    
    def Youtube(self):
        self.Yout=webbrowser.open('https://www.youtube.com/channel/UC8dMEuqS4TCcI8SgayqAbdg',new=0,autoraise=True)
        return self.Yout

    def InfoToolOperandi(self,*args,**kwargs):
        self.b=Toplevel()
        self.b=PadHn(self.b)
    
    def ExcAyu(self):
        if tkMessageBox.askyesno('Simple Visor De Fotos','Para Ver Instrucciones Online Debes Visitar peicelgroup.byethost15.com, ¿ DESEAS VISITAR EL SITIO WEB ?'):
            self.webR=webbrowser.open('http:/www.peicelgroup.byethost15.com/',new=0,autoraise=True)
            return self.webR
        else:
            return 
            
    def __init__(self,VisorV,*args,**kwargs):
        self.Ventana = VisorV
        self.wid=554
        self.hei=640
        self.colF='#e9ebee'
        self.Ventana.title('Simple Visor De Fotos')
        self.Ventana.geometry('554x640')
        self.Ventana.maxsize(width=self.wid,height=self.hei)
        self.Ventana.minsize(width=554,height=640)
        self.PhotoIco = PhotoImage(file='bin/images/favicon.gif',format='gif')
        self.ImageBot=PhotoImage(file='bin/images/Uplo.gif',format='gif')
        self.Fa=PhotoImage(file='bin/images/Facebook.gif',format='gif')
        self.Tw=PhotoImage(file='bin/images/Twitter.gif',format='gif')
        self.You=PhotoImage(file='bin/images/Youtube.gif',format='gif')
        self.BoN=PhotoImage(file='bin/images/Next.gif',format='gif')
        self.BoP=PhotoImage(file='bin/images/Previus.gif',format='gif')
        self.ImF=PhotoImage(file='bin/images/info.gif',format='gif')
        self.ImA=PhotoImage(file='bin/images/ayuda.gif',format='gif')
        self.ImC=PhotoImage(file='bin/images/Close.gif',format='gif')
        self.ImageDel=PhotoImage(file='bin/images/Erase.gif',format='gif')
        self.NumbL=0
        self.Op=1
        self.For1=''
        self.For2=''
        self.For3=''
        self.For4=''
        self.opts = {}
        self.opts['title']='Abrir Foto || Simple Visor De Fotos '
        self.opts['filetypes'] = [('GIF files','.gif')]

        #BarraMenu
        self.BarrM=Menu(self.Ventana)
        self.MenuF=Menu(self.BarrM,tearoff=0)
        self.MenuF.add_command(label='Información',image=self.ImF,compound=LEFT,command=self.InfoToolOperandi,foreground='#066',background='#e9ebee')
        self.MenuF.add_separator()
        self.MenuF.add_command(label='Ayuda',foreground='#066',image=self.ImA,command=self.ExcAyu,compound=LEFT,background='#e9ebee')
        self.MenuF.add_command(label='Salir',image=self.ImC,compound=LEFT,command=self.Ventana.destroy,foreground='#066',background='#e9ebee')
        self.BarrM.add_cascade(label='File',menu=self.MenuF,underline=0)

        #Config
        self.Ventana.configure(bg=self.colF)
        self.Ventana.config(menu=self.BarrM)
        self.Ventana.tk.call('wm','iconphoto',self.Ventana._w,self.PhotoIco)
        self.Ventana = Frame(VisorV)
        self.Ventana.pack(side="top",fill="both",expand=True)
        self.Ventana.grid_rowconfigure(0,weight=1)
        self.Ventana.grid_columnconfigure(0,weight=1)
        
        # Menu Frame
        self.LaIm1=Label(bg='#066',width=55,height=25).place(x=80,y=20)
        self.LaIm2=Label(bg='#066',width=20,height=10).place(x=45,y=430)
        self.LaIm3=Label(bg='#066',width=20,height=10).place(x=205,y=430)
        self.LaIm4=Label(bg='#066',width=20,height=10).place(x=365,y=430)
        self.NumLi=Label(self.Ventana,text=self.NumbL,fg='#066',font=('Arial',18)).place(x=60,y=600)
        self.BotIns=Button(self.Ventana,text='Insertar Foto',image=self.ImageBot,command=self.InsertF,compound=LEFT,bg='#066',width=130,fg='#fff',font=('Arial',12),relief='ridge',underline=3,activebackground='#066',activeforeground='#fff')
        self.BotIns.place(x=105,y=600)
        self.ButF=Button(image=self.Fa,bg='#e9ebee',command=self.Facebook,activebackground='#e9ebee',underline=0,relief=FLAT).place(x=450,y=605)
        self.ButT=Button(image=self.Tw,bg='#e9ebee',command=self.Twitter,activebackground='#e9ebee',underline=0,relief=FLAT).place(x=473,y=605)
        self.ButY=Button(image=self.You,bg='#e9ebee',command=self.Youtube,activebackground='#e9ebee',underline=0,relief=FLAT).place(x=496,y=605)
        self.ButN=Button(self.Ventana,text='Next',image=self.BoN,compound=TOP,command=self.NextI,font=('Arial',13),fg='#066',activeforeground='#066',cursor='hand1',width=50,bg='#e9ebee',activebackground='#e9ebee',relief=FLAT).place(x=484,y=170)
        self.ButN=Button(self.Ventana,text='Prev',image=self.BoP,compound=TOP,command=self.prev,font=('Arial',13),fg='#066',activeforeground='#066',cursor='hand1',width=50,bg='#e9ebee',activebackground='#e9ebee',relief=FLAT).place(x=10,y=170)
        self.BotDe=Button(self.Ventana,text='Eliminar Foto',command=self.DelF,image=self.ImageDel,compound=LEFT,bg='#066',width=130,fg='#fff',font=('Arial',12),relief='ridge',underline=6,activebackground='#066',activeforeground='#fff')
        self.BotDe.place(x=275,y=600)
        self.Ventana.mainloop()

    
def main():
    ZonaV = Tk()
    b=HanV(ZonaV)
    
if __name__=='__main__':
    main()
