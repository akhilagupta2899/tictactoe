from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def checkWinner():

    if (button1['text'] == 'O' and  button2['text'] == 'O' and  button3['text'] == 'O' or
        button4['text'] == 'O' and button2['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' ):
        messagebox._show("winner is game ", 'player o is winner')
        exit()

    elif(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
         button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
         button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
         button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
         button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
         button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
         button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
         button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
         messagebox._show("winner is game ", 'player x is winner')
         exit()


    elif(button1['text'] != '' and button2['text'] != '' and button3['text'] != '' and
         button4['text'] != '' and button5['text'] != '' and button6['text'] != '' and
         button7['text'] != '' and button8['text'] != '' and button9['text'] != '' ):
          messagebox._show("no winner "," game is draw")
          exit()




root= Tk()

root.geometry('600x600')

button1=ttk.Button(root,text='',command= lambda:buttonPressed(1))
button1.grid(row=0,column=0,ipadx=50,ipady=50)
button2=ttk.Button(root,text='',command= lambda:buttonPressed(2))
button2.grid(row=0,column=1,ipadx=50,ipady=50)
button3=ttk.Button(root,text='',command= lambda:buttonPressed(3))
button3.grid(row=0,column=2,ipadx=50,ipady=50)
button4=ttk.Button(root,text='',command= lambda:buttonPressed(4))
button4.grid(row=1,column=0,ipadx=50,ipady=50)
button5=ttk.Button(root,text='',command= lambda:buttonPressed(5))
button5.grid(row=1,column=1,ipadx=50,ipady=50)
button6=ttk.Button(root,text='',command= lambda:buttonPressed(6))
button6.grid(row=1,column=2,ipadx=50,ipady=50)
button7=ttk.Button(root,text='',command= lambda:buttonPressed(7))
button7.grid(row=2,column=0,ipadx=50,ipady=50)
button8=ttk.Button(root,text='',command= lambda:buttonPressed(8))
button8.grid(row=2,column=1,ipadx=50,ipady=50)
button9=ttk.Button(root,text='',command= lambda:buttonPressed(9))
button9.grid(row=2,column=2,ipadx=50,ipady=50)


player = 1


def buttonPressed(buttonNumber):
    global player

    if buttonNumber == 1 and player == 1 and button1['text'] != 'O':
        button1.config(text="X")
        player = 2

    elif buttonNumber==1 and player== 2 and button1['text']!='X':
        button1.config(text="O")
        player = 1

    elif buttonNumber == 2 and player == 1 and button2['text']!='O':
        button2.config(text="X")
        player = 2

    elif buttonNumber == 2 and player == 2 and button2['text']!='X':
        button2.config(text="O")
        player = 1

    elif buttonNumber == 3 and player == 1 and button3['text'] != 'O':
        button3.config(text="X")
        player = 2

    elif buttonNumber == 3 and player == 2 and button3['text']!='X':
        button3.config(text="O")
        player = 1
    elif buttonNumber == 4 and player == 1 and button4['text'] != 'O':
        button4.config(text="X")
        player = 2

    elif buttonNumber == 4 and player == 2 and button4['text']!='X':
        button4.config(text="O")
        player = 1
    elif buttonNumber == 5 and player == 1 and button5['text'] != 'O':
        button5.config(text="X")
        player = 2

    elif buttonNumber == 5 and player == 2 and button5['text']!='X':
        button5.config(text="O")
        player = 1
    elif buttonNumber == 6 and player == 1 and button6['text'] != 'O':
        button6.config(text="X")
        player = 2

    elif buttonNumber == 6 and player == 2 and button6['text']!='X':
        button6.config(text="O")
        player = 1
    elif buttonNumber == 7 and player == 1 and button7['text'] != 'O':
        button7.config(text="X")
        player = 2

    elif buttonNumber == 7 and player == 2 and button7['text']!='X':
        button7.config(text="O")
        player = 1
    elif buttonNumber == 8 and player == 1 and button8['text'] != 'O':
        button8.config(text="X")
        player = 2

    elif buttonNumber == 8 and player == 2 and button8['text']!='X':
        button8.config(text="O")
        player = 1
    elif buttonNumber == 9 and player == 1 and button9['text'] != 'O':
        button9.config(text="X")
        player = 2

    elif buttonNumber == 9 and player == 2 and button9['text']!='X':
        button9.config(text="O")
        player = 1

    checkWinner()
root.mainloop()
