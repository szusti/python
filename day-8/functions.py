def greet():
    print("Hello")
    print("User")
    print("Your in")

def greet_with_name(name):
    print("Hello")
    print("User provided: ", name)
    print("Your in")

def greet_with(name, location):
    print("Hello")
    print("User provided: ", name)
    print("You are from: ", location)

# can also use def greet_with(name=name_a,location=location_a)
# this way does not matter order

# greet()
# greet_with_name(input("Provide your name\n"))
greet_with("Michaelllo", "Katowice")