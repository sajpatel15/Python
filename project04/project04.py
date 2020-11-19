''' Module Project03.py'''
''' Author: Saj Patel
    Purose: To write a program that can cipher a text ''' 
import string

def cypher_alphabet(text):
    # creates a list with all lowercase alphabets
    plain_text = list(string.ascii_lowercase)

    # creates a list from the string passed and checks to see if any letter is repeated if so, the repeated letter would not be added
    cipher_text = []
    for elem in text:
        if elem not in cipher_text:
            cipher_text.append(elem.lower())

    # checks the plain_text list for remaining elements and adds it to the cipher list.
    for elem in plain_text:
        if not elem in cipher_text:
            cipher_text.append(elem)
    cipher = "".join([str(elem)for elem in cipher_text])

    # returns a string of letters with the cipher
    return cipher

def encrypt(text, cypher_alphabet):
    # creating a list of the string that is seperated by each letter
    text_list = [char for char in text]
    
    # storing the cypher alphabets in a list
    cypher = [char for char in cypher_alphabet]
    
    # creating an empty list that has the final string
    result = []
    
    # Doing the cypher using indexing 
    for char in text_list:

        # gets the ascii value of the lower case character
        if ord(char.lower()) > 96 and ord(char.lower()) < 123:
            # converts the ascii value to an index
            index = ord(char.lower()) - 97
            
            # stores the cyphered char in a var
            char1 = str(cypher[index])
            
            #checks to see if that char was upper case
            if char.isupper():
                result.append(char1.upper())
            else:
                result.append(char1)
        # checks to see if there is a space
        elif ord(char) == 32:
            result.append(" ")
        else:
            result.append(char)

    # convert the list to a string
    return "".join([str(elem) for elem in result])

def get_unencrypted_text(file_path):
    # storing opening the file path as a readable file
    # making sure to get catch any errors that may be thrown when
    # reading the file
    try:
        #storing the file as readable 
        f = open(file_path, "r")
        # storing the contents of the file as a string 
        file_content = f.read()
        # retunring the stirng 
        return file_content
    # making sure that an IOError is accounted for
    except IOError:
        print ("File not found: ", file_path, " Please try again!")

def main():
    
    # boolean that determines if the input is correct and acceptable
    correct_input = False
    file_name = ""
    unencrypted_text = ""
    while not correct_input:    
        file_name = input ("Please enter the file path for the text to be encrypted: ")
        # stroring the text
        unencrypted_text = get_unencrypted_text(file_name)
        
        # checking to see the file contains a text
        if len(unencrypted_text) == 0:
            print ("File is empty")
        else:
            correct_input = True
    # asking the user for a keyword input
    keyword = input ("Please enter a keyword for the mixed cipher: ")
    cipher = cypher_alphabet(keyword)

    # printing a plain text and the cipher text
    print ("Plaintext: ", string.ascii_lowercase)
    print ("Ciphertext: ", cypher_alphabet(keyword))

    # carrying out the encryption
    encryption = encrypt(unencrypted_text, cipher)
    print(encryption)

if __name__ == '__main__':
    main()






