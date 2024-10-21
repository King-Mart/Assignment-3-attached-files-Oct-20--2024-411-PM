import math

def split_tester(N, d):
    """
    Returns True if for each substring of length d, the numbers are in increasing order
    """
    N = str(N)
    if len(N) % d != 0:
        return False
    else:
        substrings = [int(N[i:i+d]) for i in range(0, len(N), d)]
        return comparePairLst(substrings, is_smaller)
# you can add more function definitions here if you like       

def is_smaller(n1, n2):
    return n1 > n2

def comparePairLst(lst, function):
    const = function(lst[1], lst[0])
    for i in range(len(lst))[2:]:
        if not function(lst[i], lst[i-1]) == const :
            return False
    return True


            
# main
# Your code for the welcome message goes here, instead of name="Vida"
name = input("What is your name? : ")
print(f"Welcome {name} to the increasing split tester, nice to meet you!")

flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    #YOUR CODE GOES HERE. The next line should be elif or else.
    else:
        print("Ok, let's do it!")
        no_error = False
        while not no_error:
            try:
                d=int(input("What is the size of the split? "))
                N=int(input("What is the number you want to test? "))
                no_error = True
            except ValueError:
                print("That's not a number. Try again.")

        if split_tester(N, d):
            print(f"{N} admits an increasing split of size {d}")
        
        else:   
            print(f"{N} does not admit an increasing split of size {d}")
            


        
#finally your code goes here too.

