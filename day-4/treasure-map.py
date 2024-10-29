line1 = ["o","o","o"]
line2 = ["o","o","o"]
line3 = ["o","o","o"]
print ("Hiding your treasure! X Makrs the spot")
position = input ("where do you want to put the treasure \n").lower()

map = [line1, line2, line3]

#different way for column
# abc = ["a", "b", "c"]
# column_number = abc.index(position[0])
column = position[0]
column_number = 0


if column == "a":
    column_number = 0
elif column_number == "b":
    column_number = 1
else: 
    column_number = 2

row = int(position[1]) - 1

map[column_number][row] = "x"



print(f"{line1}\n{line2}\n{line3}")
