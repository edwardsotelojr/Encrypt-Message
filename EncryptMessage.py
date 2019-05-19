# -*- coding: utf-8 -*-
"""
Edward Sotelo Jr
1428744
Assignment #6 
"""
import string

# encrypt message with a code word
def encrypt(message, code):
    i= 0
    cypher_text = ""
    codeCharacter = ""
    for letter in message:
        if letter.isalpha():
           codeCharacter = code[i%len(code)] #cycle through code word
           i = i + 1
           code_letter = encrypt_letter(letter, codeCharacter) # encrypt letter
           cypher_text +=  code_letter # add letter to encrypted string
        else: #if not a alphabet letter, add to encrypted string
            cypher_text += letter
    return cypher_text # return encrypted message

#encrypt letter
def encrypt_letter(message_letter, code_letter):
    alphabet = string.ascii_uppercase #string of the alphabet capitalized
    index = alphabet.find(code_letter) #find index of code character
    newAlphabet = alphabet[index:]+alphabet[:index] # reorganize the alphabet start with code character
    index2 = alphabet.find(message_letter.upper()) #index of message letter in orginal alphabet
    result = newAlphabet[index2] # letter at index2 in new alphabet
    if message_letter.islower():
        result = result.lower()
    return result

# decrypt message
def decrypt(encrypt_message, code_word):
    message = ""
    i= 0
    for letter in encrypt_message:
        if letter.isalpha():
            codeCharacter = code_word[i%len(code_word)] #cycle through letters of code word
            i = i + 1
            Plain_letter = decrypt_letter(letter, codeCharacter) # decrypt a letter
            message += Plain_letter
        else:
            message += letter
    return message

# decrypt letter
def decrypt_letter(encrypt_letter, code_letter):
    alphabet = string.ascii_uppercase #string of alphabet
    index = alphabet.find(code_letter) #index of code letter
    newAlphabet = alphabet[index:]+alphabet[:index] # reorganize alphabet
    index2 = newAlphabet.find(encrypt_letter.upper()) # index of encrypt letter in new alphabet
    result = alphabet[index2] # decrypted letter
    if encrypt_letter.islower():
        result = result.lower()
    return result
    

text = input("Enter a message to be encrypted: ")
code_word = input("Enter a code word: ")

code_word = code_word.upper()
encryptMessage = encrypt(text, code_word)
print("Encrypted message:", encryptMessage)

decrypt_message = decrypt(encryptMessage, code_word)
print("Decrypting message:", decrypt_message)


