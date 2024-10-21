def sum_odd_divisors(n):
    '''
    '''
    if n == 0:
        return None
    n = abs(n)
    sum = 1 + n if n % 2 == 1 else 1
    for i in range(2, int(n**0.5+1)+1):
            sum += (i + n//i if (n/i) % 2 == 1 else i) if n % i == 0 and i % 2 == 1 else 0 
    return sum
print(sum_odd_divisors(-2001))

def series_sum():
    sum = 1000
    for i in range(1, int(input("Please enter a non negative integer : \n")) + 1):

        sum += 1/(i**2)
    return sum





def pell(n):
    '''
    '''
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache = {0 : 0
             , 1 : 1}
    sum = 0
    for i in range(2, n + 1):
        sum = 2 * cache[i - 1] + cache[i - 2]
        cache[i] = sum
    return sum
def pell_recursive(n, cache={0: 0, 1: 1}):
    '''
    Faster but python sets a recursive limit at 999 so unuasble for some tests
    '''
    if n < 0:
        return None
    if n in cache:
        return cache[n]
    cache[n] = 2 * pell(n - 1, cache) + pell(n - 2, cache)
    return cache[n]

import time

start_time = time.time()
print(pell(1743))
print("Time taken by pell:", time.time() - start_time, "seconds")

def valid_char(char):
    return 101 <= ord(char) <= 106 or 70 <= ord(char) <= 88 or 50 <= ord(char) <= 54 or char == "\\" or char == "," or char == "!"



def countMmbers(phrase):
    sum = 0
    for char in phrase:
        if valid_char(char):
            sum += 1
    return sum

def casual_number(s):
    '''
    Returns the first number found in the string. If a number is found, it is returned as an integer. If no number is found, None is returned. My understanding of this question is that it is a number if there are no consecutive non integer characters

    :param s: A string containing what might look like a number
    :return: the found number, None if none are found
    '''
    if len(s) == 0:
        # If the string is empty, return None
        return None
    found_number = ""
    previous_is_digit = True
    if s[0].isdigit():
        # If the first character is a digit, add it to the number
        found_number += s[0]
    elif s[0] == "-":
        # If the first character is a negative sign, add it to the number
        found_number += s[0]
        previous_is_digit = False
    else:
        # If the first character is not a digit, mark it as not a digit
        previous_is_digit = False
        
    for char in s[1:]:
        if char.isdigit():
            # If the character is a digit, add it to the number
            found_number += char
            previous_is_digit = True
        else:
            if not previous_is_digit:
                # If the character is not a digit, and the previous character was not a digit, return None
                return None
            previous_is_digit = False


    # Return the found number as an integer
    return int(found_number)

def alienNumbers(s):
    '''
    A function that takes a string of characters and returns the decimal equivalent using the following mapping:
    T = 1024, y = 598, ! = 121, a = 42, N = 6, U = 1

    '''
    # The one line challenge i only possible thanks to the assumptions we make which are Type safety
    # The function assumes that the input string will only contain the characters T, y, !, a, N, U
    # The function will return None if the input string contains any other characters
    return sum({"T" : 1024, "y" : 598, "!" : 121, "a" : 42, "N" : 6, "U" : 1}[x]  for x in s if x in "Ty!aNU")

def alienNumbersAgain(s):
    '''
    A function that takes a string of characters and returns the decimal equivalent using the following mapping:
    T = 1024, y = 598, ! = 121, a = 42, N = 6, U = 1

    '''
    # TNothing changes here since I didn't use any string functions at first
    return sum({"T" : 1024, "y" : 598, "!" : 121, "a" : 42, "N" : 6, "U" : 1}[x]  for x in s if x in "Ty!aNU")

def encrypt(s):
    '''
    '''
    return "".join(y+x for x, y in zip(s[:len(s)//2], s[:((len(s)+1)//2)-1:-1])) + s[(len(s))//2:(len(s)+1)//2]




print(encrypt("Hello, world"))

def oPify(s : str):
    if not s:
        return ""
    output = s[0]
    for i in range(len(s))[1:]:
        if s[i-1].isalpha() and s[i].isalpha():
            output += "O" if s[i-1].isupper() else "o"
            output += "P" if s[i].isupper() else "p"
        output += s[i]
    return output

def nonrepetitive(s):
    '''I will use a simple implementation of the Trie datastructure to solve this assigmnent. Here there is no root and the tree might loop, which will help us determine if a duplicate is found
    '''
    if not s:
        return ""
    
    #saving the previously encountered character
    previous_char = s[0]

    #characters we need to lookout for
    watchlist = []

    #characters that would prove the string to be repetitive
    target = ""
    #If we are suspicious of a repeated pattern
    alertMode = False

    #Trie
    word_map = {s[0] : []}

    for index, char in enumerate(s[1:]):
        #If we are not in alert mode (lookout)
        if not alertMode:
            #If we have a character that is not in the watchlist we add it to our pattern tracker
            word_map[previous_char].append(char)
        else:

            #Loop the remaining letters to see if we find the same pattern TODO: keep track of multiple targets to avoid looping the same elements over and over again
            for char in s[index+1:]:

                #If we loop back to the same character, we can conclude it does repeat
                if char in word_map:
   
                        if word_map[char][0] == target:
                            return False
                else:
                    alertMode = False
                    break
                #If we have a character that is in the watchlist we keep the alert mode until we loop back to one of the same
                if char in watchlist:
                    watchlist = word_map[char]
                    previous_char = char
                else:
                    alertMode = False
                    break

                
            
        
        #keep looking
        if char not in word_map:
            word_map[char] = []
        
        #If we find the word then we trigger alert mode and look to see if we will come across the word again
        else:
            alertMode = True
            watchlist =word_map[char]
            target = char

        previous_char = char

    return True
    



print(oPify("aBCdef22x"))

print(nonrepetitive("borborygmus"))
