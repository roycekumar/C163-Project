from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("Fever_Report")
root.geometry("600x630")
yes = ImageTk.PhotoImage(Image.open("yes.png"))
no=ImageTk.PhotoImage(Image.open("no.png"))
root.configure(background="#fa8071")
question1_radioButton=StringVar(value=0)

Question1=Label(root,text="Do you experience shortness of breath during routine activities?",background="#fa8071",fg="white")
Question1.pack()
question1_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes",image=yes,background="#fa8071")
question1_r1.pack()
question1_r2=Radiobutton(root,text="no",variable=question1_radioButton,value="no",image=no,background="#fa8071")
question1_r2.pack()

question2_radioButton=StringVar(value="0")
Question2=Label(root,text="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?",background="#fa8071",fg="white")
Question2.pack()
question2_r1=Radiobutton(root,text="yes",variable=question2_radioButton,value="yes",image=yes,background="#fa8071")
question2_r1.pack()
question2_r2=Radiobutton(root,text="no",variable=question2_radioButton,value="no",image=no,background="#fa8071")
question2_r2.pack()

question3_radioButton=StringVar(value="0")
Question3=Label(root,text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?s",background="#fa8071",fg="white")
Question3.pack()
question3_r1=Radiobutton(root,text="yes",variable=question3_radioButton,value="yes",image=yes,background="#fa8071")
question3_r1.pack()
question3_r2=Radiobutton(root,text="no",variable=question3_radioButton,value="no",image=no,background="#fa8071")
question3_r2.pack()
question4_radioButton=StringVar(value="0")
Question4=Label(root,text="Do you experience shortness of breath while at rest/lying down",background="#fa8071",fg="white")
Question4.pack()
question4_r1=Radiobutton(root,text="yes",variable=question4_radioButton,value="yes",image=yes,background="#fa8071")
question4_r1.pack()
question4_r2=Radiobutton(root,text="no",variable=question4_radioButton,value="no",image=no,background="#fa8071")
question4_r2.pack()
question5_radioButton=StringVar(value="0")
Question5=Label(root,text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",fg="white",background="#fa8071")
Question5.pack()
question5_r1=Radiobutton(root,text="yes",variable=question5_radioButton,value="yes",image=yes,background="#fa8071")
question5_r1.pack()
question5_r2=Radiobutton(root,text="no",variable=question5_radioButton,value="no",image=no,background="#fa8071")
question5_r2.pack()
def fever_score():
    score=0
    if question1_radioButton.get()=="yes":
        score+=10
        print(score)
    if question2_radioButton.get()=="yes":
        score+=10
        print(score)
    if question3_radioButton.get()=="yes":
        score+=10
        print(score)
    if question4_radioButton.get()=="yes":
        score+=10
        print(score)
    if question5_radioButton.get()=="yes":
        score+=10
        print(score)
    if score<=10:
        messagebox.showinfo("Report","You don't need to visit a doctor")
    elif score>10 and score<=30:
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else:
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
btn=Button(root,text="Click Me",command=fever_score)
btn.pack()
root.mainloop()
