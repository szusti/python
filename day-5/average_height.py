#Average height

heigh = input("Provide list of students heights").split()

# alternative loop
# for i in range(0,len(heigh)):
#     heigh_number[i] = int(heigh[i])

# print("Lista", heigh)

sum_heigh = 0
number_of_students = 0
for i in heigh:
    number_of_students += 1
    sum_heigh += int(i)

average_height = round(sum_heigh / number_of_students)
print("Average heights is ", average_height)





