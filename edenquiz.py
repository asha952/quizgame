
total_right = 0


def result(one_or_zero):
    global total_right
    if one_or_zero == 1:
        total_right += 1
        print("you got that one right! good job \n")
    elif one_or_zero == 0:
        print("bzzzzzzt you got that one wrong \n")


def where_from():
    print("1. Where is EDEN from? Please enter a letter a-e")
    print("a. New York")
    print("b. California")
    print("c. Mexico")
    print("d. Ababwa")
    print("e. Dublin")
    if input() == 'e':
        return 1
    else:
        return 0


def what_song():
    print("1. what is his oldest song? Please enter a letter a-e")
    print("a. Wide Awake")
    print("b. falling in reverse")
    print("c. drugs")
    print("d. XO")
    print("e. Fumes")
    if input() == 'd':
        return 1
    else:
        return 0


print("Welcome to a quiz about the artist EDEN")
result(where_from())
result(what_song())
print(total_right)