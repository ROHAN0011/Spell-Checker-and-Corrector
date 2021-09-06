from textblob import TextBlob
from tkinter import *


def Auto_correct():
    Output_text.delete(1.0, END)
    corrected_words = []
    text = Input_text.get(1.0, END).split(" ")
    for i in text:
        corrected_words.append(TextBlob(i))

    for i in corrected_words:

        Output_text.insert(END, i.correct()+" ")


root = Tk()
root.geometry('1200x520')
root.resizable(0, 0)
root.title("Project--  Auto Spelling Correction   - Rohan Kasabe")
root.config(bg='blue')


# heading
Label(root, text="AUTO SPELLING CORRECTION ",
      font="arial 20 bold", pady=5, bg='white smoke').pack()
# footer
Label(root, text="Developed By Rohan Kasabe", font='arial 20 bold',
      pady=5, bg='white smoke', width='25').pack(side='bottom')

# INPUT AND OUTPUT TEXT WIDGET
Label(root, text="Enter Text", font='arial 18 bold',
      bg='white smoke').place(x=250, y=90)
Input_text = Text(root, font='arial 13', bg='black', fg='white', height=11,
                  wrap=WORD, padx=5, pady=5, width=60, insertbackground='white')
Input_text.place(x=30, y=130)

Label(root, text="Output", font='arial 18 bold',
      bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 13', bg='black', fg='white', height=11,
                   wrap=WORD, padx=5, pady=5, width=60, insertbackground='white')
Output_text.place(x=600, y=130)


##########  Correction Button ########
auto_correct_btn = Button(root, text='Auto Correct', bg='green',
                          font='arial 18 bold', pady=5, command=Auto_correct)
auto_correct_btn.place(x=510, y=360)

root.mainloop()