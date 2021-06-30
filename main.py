from tkinter import *
import difflib
from timeit import default_timer
import random

root=Tk()
root.title('Typing test')
root.geometry("600x400")
 
header = Label(root, font = ('arial', 30, 'bold'), text = "Typing Test",bg="gold")
header.place(x = 200,y = 0)
 
words=['Life is a game play it','I like watching sports', 'We are going out', 'Lets play in the garden','I prefer coffee', 'Ram is faster than Paul', 'This is an amazing man', 'I prefer Marvel over DC', 'Lets check the scores', 'we are waiting for the results' ]
word=random.choice(words)

entered=StringVar()

def enter():
    global word
    global start
    global entered  
 
    label2=Label(root, font = ('arial', 15), text = "Type here:",bg="gold")
    label2.place(x= 100, y=150)
 
    entered=StringVar() 
    enter=Entry(root,textvariable=entered,font =('arial', 15),width=20)
    enter.place(x=200,y=150)
 
    btn2 = Button(root, text = "Test",command=test,bg="blue",fg="white", font = ('arial', 10))
    btn2.place(x=200,y=200)
    
def test():
    global entered
    global word
    global start
 
    string=f"{entered.get()}"
    end=  default_timer()
    time= round(end-start,3)
    wpm=round(len(word.split())*60/time,2)
 
    if string==word:
        d1 ="Time= " + str(time) + ' sec'
        d2="Accuracy= 100% "
        d3= "wpm= " + str(wpm) + 'wpm' 
    
    elif string=='':
        d1 ="Time= " + str(time) + ' sec'
        d2="Accuracy= 0% "
        d3= "wpm= 0%"         
        
    else:
        accuracy=difflib.SequenceMatcher(None,word,string).ratio()
        accuracy=str(round(accuracy*100,2))
        d1 ="Time= "+ str(time) + ' sec'
        d2="Accuracy= " + accuracy + '%'
        d3= "wpm= " + str(wpm) + ' wpm'
 
    
    label1=Label(root, font = ('arial', 15, 'italic'), text = d1,bg="gold")
    label1.place(x= 200,y= 250)
 
    label1=Label(root, font = ('arial', 15, 'italic'), text = d2,bg="gold")
    label1.place(x= 200,y= 300)
 
    label1=Label(root, font = ('arial', 15, 'italic'), text = d3,bg="gold")
    label1.place(x= 200,y= 350)

label=Label(root, font = ('arial', 20, 'bold'), text = word,fg="red",bg="gold")
label.place(x=150,y=50)
 
btn = Button(root, text = "Click to Enter",command=enter,bg="blue",fg="white", font = ('arial', 10))
btn.place(x=200,y=100)
start= default_timer()
 
mainloop()
