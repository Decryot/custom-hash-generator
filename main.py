import random

# you can add more characters to further encrypt your hash
letters = ["a","c","d","e","f","i","l","m","n","o","r","u"
          ,"0","1","2","3","4","5","6","7","8","9"]

hash_test = []
max_hash_letters = 3
min_hash_letters = 2

# creates a sequence of letters for each letter

def encrypt_word(word):
    word_letters = list(word)
    encrypted_word = ""

    for i in word_letters:
        for j in range(len(letters)):
            if str.lower(i) == letters[j]:
                encrypted_word += hash_test[j]

    print(encrypted_word)

def save_hash():
    file = open("hash.txt","w+")
    for hash_code in hash_test:
        file.write(hash_code + "\n")

def create_hash():
    global letters

    for letter in range(len(letters)):
        random_count_for_hash = random.randint(min_hash_letters,max_hash_letters)
        new_hash = ""

        for count in range(random_count_for_hash):
            letter_id = random.randint(0,len(letters)-1)
            new_hash += letters[letter_id]

        hash_test.append(new_hash)
        print(new_hash + " " + letters[letter])

    save_hash()
    encrypt_word("hello, what are you doing")

create_hash()
