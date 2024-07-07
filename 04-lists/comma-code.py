

def comma_code(l: list):

    for i, x in enumerate(l):
        if i == len(l) - 1:
            print("and " + str(x))
            break
        print(str(x), end=", ")

        
comma_code([1, 2, 3, 4, 5])
