import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S State game")
image = "C:/Users/USER/Documents/Python/day25/us_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state=[]

while len(guessed_state) < 50:
   ans_state=screen.textinput(title=f"{len(guessed_state)}/50 State guessed ", prompt="Enter the state name:").title()
   df =pd.read_csv('C:/Users/USER/Documents/Python/day25/us_game/50_states.csv')
   states_name=df['state'].to_list()
   if ans_state in states_name:
      t=turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = df[df.state == ans_state]
      t.goto(int((state_data.x)),int(state_data.y))
      t.write(ans_state)
      guessed_state.append(ans_state)
   
turtle.mainloop()