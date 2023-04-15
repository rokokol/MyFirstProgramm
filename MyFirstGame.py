from tkinter import *
import random
import time
import os
import sys

class Ball:
    def __init__(self, canvas, paddle, color):
        starts = [-6,-4,-2,2,4,6]
        random.shuffle(starts)
        self.score =score
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id,245,100)
        self.x=starts[0]
        self.y=-6
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom= False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        q = score.score/1000
        if pos[1] <=0:
            self.y=6+q
        if pos[3] >= self.canvas_height:
            self.y=-6-q
        if pos[0] <= 0:
            self.x =6+q
        if pos[2] >= self.canvas_width:
            self.x =-6-q
        if self.hit_paddle(pos):
            self.y=-8-q
            if paddle.x >= 0:
                self.x = self.x+3+q
            else:
                self.x = self.x-3-q
        if pos[3] >= self.canvas_height:
            self.hit_bottom =True

class Score:
    def __init__(self, canvas):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(400, 20, text='''Your score is %s'''% self.score, font=('Courier',10))

    def hit(self):
        self.score += 200
        self.canvas.itemconfig(self.id, text='''Your score is %s'''% self.score)
            
class Paddle:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.started = False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('A', self.turn_left)
        self.canvas.bind_all('D', self.turn_right)
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.restart)
        self.canvas.bind_all('<Return>', self.start_game)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw (self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.x=0
        elif pos[2] >= self.canvas_width:
            self.x=0

    def turn_left(self, evt):
        q = score.score/1000
        self.x=-5-q

    def turn_right(self, evt):
        q = score.score/1000
        self.x=5+q

    def start_game(self, evt):
        self.started = True

    def restart(self, evt):
        os.execv(sys.executable, [sys.executable] + sys.argv)

score = 0
tk = Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle=Paddle(canvas, '#401a00')
ball = Ball(canvas, paddle, '#fba71c')
text= canvas.create_text(250, 150, text='''Press enter for start''', fill='blue', font=('Courier', 22,))
score = Score(canvas)
end= ['охуевающая', 'промордоблядскойстрахобиздище.', 'Грихомордоблядское', 'пиздоуебищевосьмипиздоебнытый', 'пятихуй.', 'Недоёбыш', 'членоротый', 'LOSHARA', 'ЛОШАРА!!!!!!1111!!1', 'петушара', 'осёл', 'даже бомж лучше играет']

while 'amogus':     
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(text, text='')
    elif ball.hit_bottom == True:
        time.sleep(0.5)
        canvas.itemconfig(text, fill = 'red', text='''      Game Over
press space for restart''')
        random.shuffle(end)
        print(end[0])
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)

