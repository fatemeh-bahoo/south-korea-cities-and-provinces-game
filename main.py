import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=467, height=700)
screen.title("South Korea Cities and Provinces Game")
image = "South_Korea_blank.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("kr.csv")
all_cities_provinces = data.Cities_and_Provinces.to_list()
user_guessed = []

while len(user_guessed) < 17:
    user_answer = screen.textinput(title=f"{len(user_guessed)}/17 The Cities and Provinces Correct", prompt="What's another city name?\nType 'exit' if you want to stop playing").title()
    if user_answer == "Exit":
        missing_data = [city for city in all_cities_provinces if city not in user_guessed]
        #We can use the line above or write the following 4 lines, the result is the same
        # missing_data = []
        # for city in all_cities_provinces:
        #     if city not in user_guessed:
        #         missing_data.append(city)
        data = pandas.DataFrame(missing_data)
        data.to_csv("missing_data.csv")
        break

    if user_answer in all_cities_provinces:
        user_guessed.append(user_answer)
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        data_check = data[data.Cities_and_Provinces == user_answer]
        pointer.goto(int(data_check.x), int(data_check.y))
        pointer.write(user_answer)
