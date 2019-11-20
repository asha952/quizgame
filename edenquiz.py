

def result(one_or_zero):
    if one_or_zero == 1:
        print("you got that one right! good job")
    elif one_or_zero == 0:
        print("bzzzzzzt you got that one wrong")


def where_from():
    print("1. Where is EDEN from?")
    print("a. New York")
    print("b. California")
    print("c. Mexico")
    print("d. Ababwa")
    print("e. Dublin")
    if input() == 'e':
        return 1
    else:
        return 0


print("Welcome to a quiz about the artist EDEN")
result(where_from())
