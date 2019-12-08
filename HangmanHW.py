from tkinter import *
from PIL import Image, ImageTk
import os

class Hangman:
    DIR = False
    def __init__(self, word="word"):
        self.window = Tk()
        self.window.title("Hangman Game")

        self.path = os.path.dirname(os.path.realpath(__file__))
        self.WORD = word.lower()
        self.WRONG = 0
        self.FOUND = ""
        self.change_image()
        self.entry = Entry(master=self.window, text="Your input here:")
        self.entry.grid(row=4, column=0)
        self.submit = Button(master=self.window, text="Submit", command=self.check)
        self.submit.grid(row=4, column=0)

        self.update_word()
        self.window.mainloop()

    def reveal(self):
        reveal = ""
        for i in self.WORD:
            if i in self.FOUND:
                reveal += i
            else:
                reveal += " _ "
        return reveal

    def change_image(self):
        if Hangman.DIR:
            directionImg = "{}/img/{}.gif".format(self.path, self.WRONG)
        else:
            directionImg = "img/{}.gif".format(self.WRONG)

        image = ImageTk.PhotoImage(Image.open(directionImg))
        img = Label(master=self.window, image=image)
        img.image = image
        img.grid(row=0, column=0)

    def check(self):
        Letter = self.entry.get[0].lower()
        print(Letter)
        if Letter not in self.WORD:
            self.WRONG += 1
        self.FOUND += Letter
        self.update_word()

        if self.WRONG == 7:
            self.submit.grid(row=0, column=0)
            self.entry.grid(row=0, column=0)
            self.updateword(self.WORD)

        self.FOUND += Letter
        self.change_image()
        self.check()

    def update_word(self, word=""):
        if not word:
            word = self.check()
        lb = Label(master=self.window, text=word)
        lb.grid(row=3, column=0)
