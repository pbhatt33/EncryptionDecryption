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

def decrypt():
    """
    Returns decrypted version of the cipher given
    
    """
    ASCII = string.printable # string containing all ASCII characters
    characters = []
    characters[:0] = ASCII  # list containing all ASCII characters
    # The following block of code creates a dictionary with keys being integers and values being 
    # the ASCII character with that integer position.
    alphaAssign = {}
    for i in range(1,len(characters)+1):
        alphaAssign[i] = characters[i-1]
    
    print("What would you like to decrypt?")
    cipher = input() #ask user for input
    cipher = cipher.replace("[", "")
    cipher = cipher.replace("]", "")
    cipher = cipher.split(",")
    # The following block of code takes each integer in the cipher (provided in list format) and creates 
    # its decrypted version based on the algorithm provided in the assignment.
    message = []
    for c in cipher:
        c = int(c)
        translation = (c**d) % n
        message.append(alphaAssign[translation])
    message = "".join(message)
        
    
    return message

message2 = decrypt()
print("This is your decrypted message:",message2)