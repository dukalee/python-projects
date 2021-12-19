#!/usr/bin/env python3

import random
import tkinter as tk


class StroopTest():


    def __init__(self): 

        self.colors = ['Red','Blue','Green','Pink','White',
           'Yellow','Orange','Purple', 'Magenta', 'Cyan']
        self.colors = [i.upper() for i in self.colors]
        self.score = 0
        self.time  = 30 
        self.highscore = 0 


    def startgame(self, event): 

        if self.time == 30:
            self.countdown()
        elif self.time <= 0 :
            self.timeover()
        self.nextcolor()


    def main(self): 

        """
        main function
        """

        self.root = tk.Tk()
        self.root.title("Stroop Test")
        self.root.geometry("500x300")
        backgroundcolor = "#2A2A2A"
        fontcolor = 'white'
        FONT = 'Orbitron'
        self.root['bg'] = backgroundcolor

        instructions = tk.Label(self.root, 
            text = "GUESS THE COLOR OF THE WORD!",
            bg = backgroundcolor,
            fg = fontcolor,
            font = (FONT, 15))

        self.score_label = tk.Label(self.root, 
            text = "SCORE: {}".format(self.score),
            bg = backgroundcolor,
            fg = fontcolor,
            font = (FONT, 15))

        self.time_label = tk.Label(self.root, 
            text = "TIME LEFT: " + str(self.time),
            bg = backgroundcolor, 
            fg = fontcolor,
            font = (FONT, 15))
                
        self.label = tk.Label(self.root, 
            text = "PRESS ENTER",
            font = (FONT, 40),
            fg = "orange",
            bg = backgroundcolor)

        self.entry = tk.Entry(self.root, 
            width = 30,
            font = FONT,
            justify = 'center')

        self.root.bind('<Return>', self.startgame)
        instructions.pack(pady = (20,5))
        self.score_label.pack(pady = 5)
        self.label.pack(pady = (30,20))
        self.entry.pack(pady=10)
        self.time_label.pack(pady = (5,10))

        self.entry.focus_set()
        self.root.mainloop()


    def countdown(self): 

        if self.time > 0:
            self.time -= 1
        self.time_label.config(text = "TIME LEFT: " + str(self.time))
        if self.time < 5: 
            self.time_label.config(fg = 'red')
        self.time_label.after(1000, self.countdown)


    def nextcolor(self): 

        if self.time > 0:

            if self.entry.get().lower() == self.colors[1].lower():
                self.score += 1
     
            self.entry.delete(0, "end")
            random.shuffle(self.colors)
            self.label.config(fg = str(self.colors[1]), text = str(self.colors[0]))
            self.score_label.config(text = "SCORE: " + str(self.score))


    def timeover(self): 

        self.label.configure(text = 'GAME OVER')


if __name__ == "__main__":

    game = StroopTest()
    game.main()


