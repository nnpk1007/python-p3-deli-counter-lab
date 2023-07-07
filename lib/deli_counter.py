# Build the line() function that shows everyone their current place in the line. 
# If there is nobody in line, it should say "The line is currently empty.".

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        current_place = "The line is currently: " + " ".join(f"{katz_deli.index(name) + 1}. {name}" for name in katz_deli)
        print(current_place)

# Build a function that a new customer will use when entering the deli. 
# The take_a_number() function should accept two arguments, 
# the list for the current line of people (katz_deli), 
# and a string containing the name of the person joining the end of the line. 
# The function should call out (i.e., print) the person's name along with 
# their position in line.
# "Welcome, Ada. You are number 1 in line.\n"

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.", end="\n")

# Build the now_serving() function which should call out (print) the next person in line 
# and then remove them from the front. If there is nobody in line, 
# it should call out (print) that "There is nobody waiting to be served!".

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
