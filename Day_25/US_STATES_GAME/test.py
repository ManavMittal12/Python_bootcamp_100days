import pandas
us_states = pandas.read_csv("50_states.csv")
# print(us_states)
state = us_states[us_states.state == "California"]
print((state.x, state.y))
