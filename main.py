import random
import re
import time

hash_letters = ["a","c","d","e","f","i","l","m","n","o","r","u"
                ,"0","1","2","3","4","5","6","7","8","9"]

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ", ".","-",",","'"
          ,"0","1","2","3","4","5","6","7","8","9"]

hash_test = []

max_hash_letters = 10
min_hash_letters = 3

# creates a sequence of letters for each letter

# decrypts custom hash
def decrypt_word(hash_word):
    counter = 0
    word_letters = list(hash_word)
    word = hash_word
    split_words = []
    decryptedword = ""
    file = None
    for i in range(len(word_letters)):
        try:
            file = open("hash.txt", "r")

            for hash_code in file:
                if (word.startswith(hash_code.strip())):
                    word = word.replace(hash_code.strip(),"",1)
                    decryptedword += letters[counter]
                counter+=1
            counter = 0

        except:
            print("file not found")
    return decryptedword

def encrypt_word(word):

    word_letters = list(word)
    encrypted_word = ""

    for wordletter in word_letters:
        for letter_id in range(len(letters)):
            if str.lower(wordletter) == letters[letter_id]:
                encrypted_word += hash_test[letter_id].strip()

    print(encrypted_word)

def load_hash():
    file = open("hash.txt", "r")
    for hash_code in file:
        hash_test.append(hash_code)

def save_hash():
    file = open("hash.txt","w+")
    for hash_code in hash_test:
        file.write(hash_code + "\n")

def create_hash(can_save_hash):
    global letters

    for letter in range(len(letters)):
        random_count_for_hash = random.randint(min_hash_letters,max_hash_letters)
        new_hash = ""

        for count in range(random_count_for_hash):
            letter_id = random.randint(0,len(hash_letters)-1)
            new_hash += hash_letters[letter_id]

        if can_save_hash:
            hash_test.append(new_hash)

    if can_save_hash:
        save_hash()
    else:
        load_hash()

    encrypt_word("hello")

    #word = decrypt_word("cf8frf9nmcf8")
    #print(word)

create_hash(False)
