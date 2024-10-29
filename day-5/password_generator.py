import random
import password_generator_char

print("Welcoe to PyPasswordGenerator!")

nr_letters = int(input("How many letters\n"))
nr_symbols = int(input("How many symbols\n"))
nr_numbers = int(input("How many numbers\n"))

password_lenght = nr_letters+nr_numbers+nr_symbols

list_choosed_letters = []
list_choosed_symbols = []
list_choosed_numbers = []

# for char in range(0, nr_letters):
#     list_choosed_letters.append(password_generator_char.letters[random.randint(0,len(password_generator_char.letters)-1)])
# for char in range(0, nr_symbols):
#     list_choosed_symbols.append(password_generator_char.symbols[random.randint(0,len(password_generator_char.symbols)-1)])
# for char in range(0, nr_numbers):
#     list_choosed_numbers.append(password_generator_char.numbers[random.randint(0,len(password_generator_char.numbers)-1)])

for char in range(0, nr_letters):
     list_choosed_letters.append(random.choice(password_generator_char.letters))
for char in range(0, nr_symbols):
     list_choosed_symbols.append(random.choice(password_generator_char.symbols))
for char in range(0, nr_numbers):
     list_choosed_numbers.append(random.choice(password_generator_char.numbers))

list_choosed_char = [list_choosed_letters, list_choosed_symbols, list_choosed_numbers]
print(list_choosed_char)
nr_char_list = [nr_letters, nr_symbols, nr_numbers]

password = ""
amount_of_letter_added = 0
while amount_of_letter_added != password_lenght:
    type_char = random.randint(0,2)
    if nr_char_list[type_char] > 0:  
        what_char = random.randint(0,len(list_choosed_char[type_char])-1)
        if list_choosed_char[type_char][what_char] != "none":
            nr_char_list[type_char] -= 1
            password += list_choosed_char[type_char][what_char]
            list_choosed_char[type_char][what_char] = "none"
            amount_of_letter_added+=1

print("Your password is ",password)

# alternatively,  shuffle option instead manually randomize. It' much more clean and shorter
# Create one list if all selected char and use shuffle options. Example from udemy

# password_list = []
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")