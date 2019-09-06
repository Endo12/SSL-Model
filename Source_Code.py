import random
import timeit
alphabet = 'abcdefghijklmnopqrstuvwxyz' #alphabet str to be used in encryption and decryption methods
def encrypt_str(num, code):#uses caesar cipher
    encrypted = ''
    for letter in code:
        if letter.isalpha(): #makes sure the character is actually a letter
            new_loc = alphabet.index(letter) + num
            if new_loc > 25: #handles special case where the index goes out of desired bounds
                new_loc -= 26
            encrypted += alphabet[new_loc]
        else:
            encrypted += letter
    return encrypted
def decrypt_str(num, code):
    decrypted = ''
    for letter in code:
        if letter.isalpha():
            old_loc = alphabet.index(letter) - num
            if old_loc < 0: #handles special case where index goes out of desired bounds
                old_loc += 26
            decrypted += alphabet[old_loc]
        else:
            decrypted += letter
    return decrypted
def ent_con(direction='continue '): #This method is used to prompt user to hit enter to continue
    while True:
        s = input('Press enter to ' + direction) #Custom directions can also be given
        if s == '':
            print('\n')
            break
stmt = '''
def hack(key):
    for num in range(0,26):
        if num == key:
            return num
''' #used for timeit, the method figures out what the casear cipher key is
#message.txt is the file being "sent"
print('Welcome to this SSL Model Program!')
print('This program will model how the Secure Sockets Layer (SSL) works at a basic level')
print('The real life equivalent of certain parts of the model will be put in parentheses (like this) and will be '
      'reviewed right before you need to hit enter to continue')
print("Let's say I (the Client) want to send something to my friend (the Server)")
print("However, I want to do this in such a way that other people (Hackers) can't read the message")
print('SSL encoding can be used to ensure that I can do just that')
ent_con('begin the simulation ')
print('To start, I must call my friend so that he knows I want to send a package')
ent_con('call friend (message server) ')
print('Message received!')
print("Now, my friend will send me a lock that I can lock (encrypt) my package with")
print("In this model, the 'lock' is a Caesar Cipher, specifically the number of times the alphabet is shifted")
ent_con('receive lock (encrypted security certificate)')
lock = random.randint(0,25)
print(f'The lock has been received! The lock in this example is {lock}')
print("Next, I have to lock my package with the lock given to me by my friend")
ent_con('lock package (encrypt data) ')
package = encrypt_str(lock,'message.txt')
print('Data encrypted!')
print("Now it's time to send the locked package with the key to my friend")
ent_con()
print("Oh no! The package has been intercepted by thieves (hackers)! However, this is where SSL connections shine")
print("Because of how internet connections were built, the thieves will only have access to the locked package, "
      "not the key to access the data")
print("Consequently, the thieves are going to have to guess the key themselves")
ent_con()
print("Note that for this model, we are using the Caesar Cipher, which isn't considered secure encryption in the "
      "wider world of cybersecurity")
ent_con()
time = timeit.timeit(stmt,number=10000)
print(f"Despite Caesar Ciphering being a poor encrypting method, it still took the hackers {(3.1536e+22)*6} seconds to crack "
      f"the SSL connection itself and {time} seconds to break the Casear Cipher") #Source: https://www.digicert.com/TimeTravel/
ent_con()
print("For comparison, this is 6 times the lifespan of universe!")
ent_con()
print("The package (data) has reached my friend (server)!")
ent_con('open package')
my_file = open(decrypt_str(lock,package))
print(my_file.read())