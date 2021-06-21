# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 00:51:38 2021

@author: beluf
"""

from tkinter import *

import cv2
import random


def abrir_ventana_2():
    global win
    ventana.withdraw()
    win=Toplevel() 
    win.geometry('380x380+500+600')
    win.configure(background='dark turquoise')
    e3=Label(win,text="GANASTE!!!",bg="dark blue",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
    Imagenganaste=Label(win,image=imagen4).place(x=45,y=50)
    lscore24=Label(win,text="ESCORE").place(x=165,y=313)
    lscore2=Label(win,text=a).place(x=175,y=333)
    lscore3=Label(win,text="-").place(x=185,y=333)
    lscore4=Label(win,text=h).place(x=195,y=333)
    boton2=Button(win,text='ok',command=win.destroy).place(x=180,y=356)

def abrir_ventana_3():
    global win
    #ventana.withdraw()
    win=Toplevel() 
    win.geometry('380x380+500+600')
    win.configure(background='dark turquoise')
    e3=Label(win,text="PERDISTE!!!",bg="dark blue",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
    Imagenperdiste=Label(win,image=imagen5).place(x=80,y=40)
    lscore344=Label(win,text="ESCORE").place(x=165,y=313)
    lscore2=Label(win,text=score3).place(x=175,y=333)
    lscore3=Label(win,text="-").place(x=185,y=333)
    lscore4=Label(win,text=score2).place(x=195,y=333)
    boton2=Button(win,text='ok',command=win.destroy).place(x=180,y=356)

def piedra():
    global score,score2,score3
    if score ==3:
        score=0
        score2=0
        score3=0
    score=score+1
    score2=score2+1
    
    mensajesronda=Label(ventana,text=score).place(x=385,y=220)
    mensajescoreme1=Label(ventana,text="SCORE:").place(x=85,y=470)
    mensajescoreme2=Label(ventana,text=score3).place(x=135,y=470)
    mensajescorecom3=Label(ventana,text="SCORE:").place(x=535,y=470)
    mensajescorecom4=Label(ventana,text=score2).place(x=590,y=470)
    cap = cv2.VideoCapture(0)
    
    paper = cv2.CascadeClassifier('paper.xml')
    sc = cv2.CascadeClassifier('scissor.xml')
    rock = cv2.CascadeClassifier('rock.xml')
    z=110
    rt= []
    while z>0:
        z=z-1
        if z%10==0:
           print(z/10)
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        paper1 = paper.detectMultiScale(gray,
                                         scaleFactor = 6,
                                         minNeighbors = 120,
                                         minSize=(200,200))
        
        sc1 = sc.detectMultiScale(gray,
    	scaleFactor = 5 ,
    	minNeighbors = 94,
        minSize=(250,250))
    
        rock1 = rock.detectMultiScale(gray,
                                         scaleFactor = 6.8 ,
                                         minNeighbors = 180,
                                         minSize=(180,180))
     
        for (x,y,w,h) in paper1:
            #cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,'paper',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
            rt.append(1)
        for (x1,y1,w1,h1) in sc1:
            #cv2.rectangle(frame, (x1,y1),(x1+w1,y1+h1),(0,0,255),2)
            cv2.putText(frame,'sc',(x1,y1-10),2,0.7,(0,0,255),2,cv2.LINE_AA)
            rt.append(2)
        for (x2,y2,w2,h2) in rock1:
            #cv2.rectangle(frame, (x2,y2),(x2+w2,y2+h2),(255,0,0),2)
            cv2.putText(frame,'rock',(x2,y2-10),2,0.7,(255,0,0),2,cv2.LINE_AA)
            rt.append(3)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) == 27:
            break
    pp=0
    scss=0
    rck=0
    s=0
    det=0
    while s<len(rt):
        if rt[s]==1:
            pp=pp+1
        if rt[s]==2:
            scss=scss+1
        if rt[s]==3:
            rck=rck+1
        s=s+1
    print(rck)
    print(scss)
    print(pp)
    if pp>scss and pp>rck:
        print("papel")
        det=1
    if scss>pp and scss>rck:
        print("scissor")
        det=2
    if rck>scss and rck>pp:
        print("ROCK")
        det=3
    
    cap.release()
    cv2.destroyAllWindows()
    
    if det==1:
        Imagenpapel=Label(ventana,image=imagen2).place(x=50,y=120)
        Imagencompu2=Label(ventana,image=imagen3).place(x=500,y=120)
        Imagenscore4=Label(ventana,image=imagen8).place(x=260,y=382)
        #score=score-1
    if det==2:   
        Imagenpapel3=Label(ventana,image=imagen3).place(x=50,y=120)
        Imagencompu3=Label(ventana,image=imagen1).place(x=500,y=120)
        Imagenscore4=Label(ventana,image=imagen8).place(x=260,y=382)
        #score=score-1
        
    if det==3:
        Imagenpapel4=Label(ventana,image=imagen1).place(x=50,y=120)
        Imagencompu4=Label(ventana,image=imagen2).place(x=500,y=120)
        Imagenscore4=Label(ventana,image=imagen8).place(x=260,y=382)
        #score=score-1
    print(score)
    if score2==3:
        abrir_ventana_3()
    elif score3==3:
        abrir_ventana_2()
    return
 
global ventana
ventana=Tk()
ventana.geometry("800x590+0+0")
ventana.config(bg="blue")
fondo=PhotoImage(file="fondo.gif")
ventana.title("PIEDRA PAPEL O TIJERA")
fondo1=Label(ventana,image=fondo).place(x=0,y=0)
imagen1=PhotoImage(file="piedra.gif")
imagen2=PhotoImage(file="papel.gif")
imagen3=PhotoImage(file="tijera.gif")
imagen4=PhotoImage(file="titulo1.gif")
imagen5=PhotoImage(file="perdiste1.gif")
imagen8=PhotoImage(file="perdiste2.gif")
titulo=Label(ventana,image=imagen4).place(x=8,y=10)
mensajescoreme5=Label(ventana,text="PLAYER 1").place(x=85,y=415)
mensajescoreme5=Label(ventana,text="COMPUTER").place(x=535,y=415)
#mensajetime=Label(ventana,text="TIME").place(x=385,y=280)
global score, score2,score3,a,h
h=0
score=0
score2=0
score3=0
a=0
btn1 = Button(ventana, text = "RONDA", command = piedra,fg = "blue", bg = "cyan").place(x=365,y=170)

print(score)
ventana.mainloop()
#ardu.close()

#################################
