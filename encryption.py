import string
import math

# p and q are prime numbers
# n, phi(n), e, and d are defined here same way they are in the assignment

p = 17
q = 23
n = p*q
phi = (p-1)*(q-1)
e = 5
d = int((2 * phi +1)/e)

def encrypt():
    """
    Returns encrypted version of the user input
    
    Arguments: 
    none (user will be asked for input)
    
    Output:
    cipher: a list containing encrypted version of user input
    """
    ASCII = string.printable # string containing all ASCII characters
    characters = []
    characters[:0] = ASCII # list containing all ASCII characters
    # The following block of code creates a dictionary with keys being ASCII characters 
    # and values being an integer (unique to that ASCII character). 
    numberAssign = {} 
    for i in range(0,len(characters)):
        numberAssign[characters[i]] = i+1
    
    print("What would you like to encrypt?")
    message = input() # ask user for input
    # The following block of code takes each letter in string input and creates its encryped version based
    # on the algorithm provided in the assignment.
    cipher = []
    for s in message:
        translation = numberAssign[s]
        cipher.append((translation**e) % n)
    
    
    return cipher
    
message1 = encrypt()
print("This is your encrypted message:",message1)
