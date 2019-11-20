One_or_Zero = 0
def result(One_or_Zero):
    if One_or_Zero == 1:
        print("you got that one right! good job")
    else:
        print()



def where_from():
    print("1. Where is EDEN from?")
    print("a. New York")
    print("b. California")
    print("c. Mexico")
    print("d. Ababwa")
    print("e. Dublin")
    if(input() == 'e'):
        print("you got that one right!")
    else:
        print("bzzt you got that one wrong")
    return