from tkinter import *
import random
import tkinter


root = Tk()
root.title('Type Speed Test')

root.geometry('700x700')

root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


def resetWritingWidgets():
    randomTexts = [
        "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. "
        "Its high-level built in data structures, combined with dynamic typing and dynamic binding, "
        "make it very attractive for Rapid Application Development, "
        "as well as for use as a scripting or glue language to connect existing components together. "
        "Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. "
        "Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter "
        "and the extensive standard library are available in source or binary form without charge for all major platforms, "
        "and can be freely distributed."
    ]

    text = random.choice(randomTexts).lower()

    splitPoint = 0

    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    root.after(60000, stopTest)
    root.after(1000, addSecond)


def stopTest():
    global writeAble
    writeAble = False

    amountWords = len(labelLeft.cget('text').split(' '))

    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    ResultLabel.destroy()
    ResultButton.destroy()

    resetWritingWidgets()


def addSecond():
    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    if writeAble:
        root.after(1000, addSecond)

def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            # set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass



resetWritingWidgets()

root.mainloop()
