from tkinter import *
import textSummarizer
    
output = ''

def clicked():
    output = textSummarizer.compute(input_text_field.get("1.0","end"))
    output_text_field.delete('1.0', 'end')
    output_text_field.insert(INSERT, output)

def clear():
    input_text_field.delete('1.0', 'end')
    
window = Tk()
window.title("Text Summarizer")

label = Label(window, text="Enter your text:")
label.grid(column=0,row=0)

input_text_field = Text(window,  height=20, width= 80)
input_text_field.grid(column=1,row=0)

label = Label(window, text="")
label.grid(column=0,row=1)

bt = Button(window,bg="green",text="Get Synopsis", command=clicked)
bt.grid(column=1,row=2)

bt = Button(window,bg="red",text="Clear Input Field", command=clear)
bt.grid(column=0, row=2)

label = Label(window, text="")
label.grid(column=0,row=3)

label = Label(window, text="Synopsis:")
label.grid(column=0,row=4)

output_text_field = Text(window, height=20, width= 80)
output_text_field.grid(column=1,row=4)

#window.geometry('600x600')
window.mainloop()

    
