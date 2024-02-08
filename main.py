import turtle as tr
import pandas as pd
screen  =tr.Screen()
screen.title("India States Game")
statesImg = "intermediate_python/day25/IndiaStateNameGuessingGame/blank_states_img.gif"
screen.addshape(statesImg)
# screen.setup(width=1000,height=1000)
screen.setup(width = 1.0, height = 1.0)
screen.screensize(bg="black")
# tr.shape(statesImg)
usMap = tr.Turtle()
usMap.shape(statesImg)



stateData = pd.read_csv("J:/Development/Python_courses/Angela_100_days_of_code/intermediate_python/day25/IndiaStateNameGuessingGame/indianStates.csv")
# print(stateData)
numOfStates = len(stateData)
isGameON = True
guessedStates=[]
while isGameON and numOfStates>len(guessedStates):
  guessedValue =screen.textinput(title=f"{len(guessedStates)}/{numOfStates} states correct:",prompt="What's another state in India?")
  # handling canedl button
  if(guessedValue):
    guessedValue = guessedValue.lower()
  else:
    isGameON = False
  
  # checking for exit command in textinput
  if(guessedValue=="exit"):
    isGameON = False
  else:
    # user enetered a valid text
    # now check if that text is actully a Indian state or not
    if(guessedValue) in stateData["state"].str.lower().to_list():
      # check if already guessed
      if guessedValue in guessedStates:
        print("you already guessed this state earlier!!")
      else:
        print("congo you guessed a state")
        stateName = " ".join(s.capitalize() for s in guessedValue.split())
        # print(f"printing {stateName} on its respective location")
        newState = tr.Turtle()
        newState.hideturtle()
        newState.penup()
        # print(f"x value is : {type(stateData.loc[(stateData["state"].str.lower() == guessedValue),"x"].item())}")
        coords = stateData.loc[(stateData["state"].str.lower() == guessedValue),["x","y"]]
        # print(coords)
        # print(type(coords))
        newState.goto(coords["x"].item(),coords["y"].item())
        newState.write(stateName,font=("Arial",8,"normal"))
        guessedStates.append(guessedValue)
    else:
      print("guessed name is incorrect try again!!")
    # print(guessedValue)
if(isGameON == False):
  print(f"game finished, you pressed exit. Your score is : {len(guessedStates)}/{numOfStates}")
elif len(guessedStates) == numOfStates:
  print("You guessed all states, congo")

# create a csv file here:
learnStates=[
  state
  for state in stateData["state"]
  if state.lower() not in guessedStates
  ]
pd.DataFrame({
  "states to learn":learnStates
}).to_csv("J:/Development/Python_courses/Angela_100_days_of_code/intermediate_python/day25/IndiaStateNameGuessingGame/statesToLearn.csv",index=False)
# print(learnStates)


# def getCoord(x,y):
#   print(x,y)
# tr.onscreenclick(getCoord  ) # this fn works with module turtle, not a object of turtle class
screen.mainloop()


# Jammu & Kashmir,-168.0, 445.0
# its a UT not state

# tr.goto(-200,-200)


# print(f"ts is : ",tr)
# print(f"type of tr is: ",type(tr))
# print(f"type of screen is : ",type(screen))
# screen.exitonclick()



 #  or use
      # from string import capwords
      # string = capwords(string) # capitalize characters after each separator.
      # see the doc: string.capwords(s, sep=None), separator defaults to space