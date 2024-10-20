

english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptedmessages = []

def loopfromindex(index, i):
    n = len(index)
    result = ' '
    for _ in range(n):
        print(f'|{index[i % n]}|', end=" ")
        i += 1
    return result

def Vignere_Square(alphabet):
    alph_length = len(alphabet)
    for i in range(alph_length):
        print(f'|{alphabet[i]}|', end='|')
    print()
    for i in range(alph_length*2):
        print(f'-',end='-')
    print()
    for i in range(alph_length):
        print(loopfromindex(alphabet,i))

def lettertoindex(letter, index):
    letter = letter.upper()
    for i, l in enumerate(index.upper()):
        if l == letter:
            return i

def indextoletter(alphabet, index):
    i = 0
    for l in alphabet:
        if i == index:
            return l
        i += 1

def Vignere_index(key_letter, plaintext_letter, alphabet):
    n = len(alphabet)
    k_i = lettertoindex(key_letter, alphabet)
    p_i = lettertoindex(plaintext_letter, alphabet)
    cipher_index = ((k_i + p_i) % n)
    cipher_letter = indextoletter(alphabet, cipher_index)
    return cipher_letter

def Vignere_encryption(keytext, plaintext, alphabet):
    r = ' '
    n = len(plaintext)
    m = len(keytext)
    for i in range(n):
       r += Vignere_index(keytext[i % m], plaintext[i], alphabet)
    return r

def reverse_Vignere_index(key_letter, ciphertext_letter, alphabet):
    n = len(alphabet)
    k_i = lettertoindex(key_letter, alphabet)
    c_i = lettertoindex(ciphertext_letter, alphabet)
    plaintext_index = ((c_i - k_i) % n)
    plaintext_letter = indextoletter(alphabet, plaintext_index)
    return plaintext_letter

def Vignere_decryption(keytext, ciphertext, alphabet):
    r = ' '
    n = len(ciphertext)
    m = len(keytext)
    for i in range(n):
       r += reverse_Vignere_index(keytext[i % m], ciphertext[i], alphabet)
    return r

def display_menu():
    options = ["Encrypt Message", "Decrypt Message", "Dump Encrypted"]
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

def display_decryption_menu(encrypted_list):
    options = [encryptedmessages]
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")




Vignere_Square(english)
#print(lettertoindex('q', english))
#print(indextoletter(english,16))
#print(Vignere_index('r','i',english))
#print(Vignere_encryption(input("What is your keytext?"),input("What is the message?"),english))
#print(reverse_Vignere_index('r','k',english))
#print(Vignere_decryption(input("What is your keytext?"),input("What is your encrypted message?"),english))

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Time to encrypt!")
        keytext = input("What is your keytext?")
        plaintext = input("What is your message?")
        newencryptedmessage = Vignere_encryption(keytext,plaintext,english)
        encryptedmessages += newencryptedmessage.split()
        print(newencryptedmessage)


    elif choice == 2:
        print("Ready to decrypt! What message will we reveal?")
        display_decryption_menu(encryptedmessages)
        choice = int(input("Which message?"))
        if choice <= len(encryptedmessages):
            keytext = input("What is the keytext?")
            print(Vignere_decryption(keytext,encryptedmessages[choice-1],english))




    elif choice == 3:
        print("Here's everything we have encrypted.")
        print(encryptedmessages)
        break
    else:
        print("Invalid choice. Please try again.")