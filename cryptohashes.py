from turtle import clear
import clipboard
import hashlib
import keyboard
import os
import time


#predifined hash functions
hashermd5 = hashlib.md5()
hashersha1 = hashlib.sha1()
hasherblake2b = hashlib.blake2b()
hasherblake2s = hashlib.blake2s()
#hasherpbkdf2_hmac = hashlib.pbkdf2_hmac() needs an input hash_name
#hasherscrypt = hashlib.scrypt() needs password
hashersha224 = hashlib.sha224()
hashersha256 = hashlib.sha256()
hashersha384 = hashlib.sha384()
hashersha3_224 = hashlib.sha3_224()
hashersha3_256 = hashlib.sha3_256()
hashersha3_384 = hashlib.sha3_384()
hashersha3_512 = hashlib.sha3_512()
hashersha512 = hashlib.sha512()
hashershake_128 = hashlib.shake_128()
hashershake_256 = hashlib.shake_256()

hashList = ["hashermd5" , "hashersha1", "hasherpbkdf2_hmac" , "hasherscrypt" , "hasherblake2b" , "hasherblake2s" , "hashersha224", "hashersha256", "hashersha384", "hashersha3_224", "hashersha3_256", "hashersha3_384", "hashersha3_512", "hashersha512", "hashershake_128", "hashershake_256", "help"]
    
def InitiateApp():
    print('Welcome to Hasher dev3.0, this is a demonstration app for the hashlib python library, here you will be able to conveniently test, learn about, and use all of the avaiable hash functions')
    print('Below is a list of hash types: ')            
    print("hashermd5, hashersha1, hasherpbkdf2_hmac, hasherscrypt, hasherblake2b, hasherblake2s, hashersha224, hashersha256, hashersha384, hashersha3_224, hashersha3_256, hashersha3_384, hashersha3_512, hashersha512, hashershake_128, hashershake_256")
    print("To learn about hash functions type 'help'")
    desiredhash = input("Type hash name: ")
   
    def Tick():
        # check user input against list, return the index of the matching element
        try:
            if hashList.index(desiredhash) == 0 : #hashermd5
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 1: #hashersha1
                hashcreate(desiredhash)

            elif hashList.index(desiredhash) == 2 : #hasherpbkdf2_hmac
                    #insert function for pbkdf2_hmac
                print("pbkdf2_hmac is currently unimplemented Sorry !")

            elif hashList.index(desiredhash) == 3: #hasherscrypt
            
                print("Scrypt is currently unimplemented Sorry !")
                
            elif hashList.index(desiredhash) == 4: #hasherblake2b
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 5: #hasherblake2s
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 6: #hashersha224
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 7: #hashersha256
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 8: #hashersha384
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 9: #hashersha3_224
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 10: #hashersha3_256
                hashcreate(desiredhash)
            
            elif hashList.index(desiredhash) == 11: #hashersha3_384
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 12: #hashersha3_512
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 13: #hashersha512
                hashcreate(desiredhash)
                
            elif hashList.index(desiredhash) == 14: #hashershake_128
                hashcreate(desiredhash)
            
            elif hashList.index(desiredhash) == 15: #hashershake_256
                hashcreate(desiredhash)
            
            elif hashList.index(desiredhash) == 16: #help
                print("About Hash Functions\n A hash function takes an input of any length and produces a fixed-length string, this means you can input a string of any length, short or long and the result will always have a fixed length! Try this out for yourself!  Equally important is the one way nature of hash functions, that is: If you're given the output of a hash function, it is mathematically infeasible to compute or invert the hash back to the original input or message. ")
                print("This section is in active development")
        except:
            menu_exit = input("Sorry, that is not a valid function\n Menu or Exit: 'm'or 'e'\n ")
            if menu_exit == "m":
                clearConsole()
                InitiateApp()
            elif menu_exit == "M":
                clearConsole()
                InitiateApp()
            elif menu_exit == "e":
                exit()
            elif menu_exit == "E":
                exit()
            else:
                input("Type 'm' for main menu or 'e' to exit program ")
                menu_exit
    Tick()
    
#wrap all hash function inside a function loop that terminates on a specific keypress
def clearConsole():
    clear = lambda: os.system("cls" if os.name in ('nt', 'dos') else ('clear'))
    clear()
    

def scrypt():
    return True

def pbkdf2_hmachash():
    return True


def hashcreate(hashtype):
    
    if hashtype == 'hashermd5':
        tohash = input('Input text to hash: ')
        hashermd5.update(tohash.encode('utf-8'))
        hashresult = hashermd5.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)



    elif hashtype == 'hashersha1':
        tohash = input('Input text to hash: ')
        hashersha1.update(tohash.encode('utf-8'))
        hashresult = hashersha1.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == 'hasherblake2b':
        tohash = input('Input text to hash: ')
        hasherblake2b.update(tohash.encode('utf-8'))
        hashresult = hasherblake2b.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)


    elif hashtype == 'hasherblake2s':
        tohash = input('Input text to hash: ')
        hasherblake2s.update(tohash.encode('utf-8'))
        hashresult = hasherblake2s.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)
      
    elif hashtype == 'hashersha224':
        tohash = input('Input text to hash: ')
        hashersha224.update(tohash.encode('utf-8'))
        hashresult = hashersha224.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == 'hashersha256':
        tohash = input('Input text to hash: ')
        hashersha256.update(tohash.encode('utf-8'))
        hashresult = hashersha256.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == 'hashersha384':
        tohash = input('Input text to hash: ')
        hashersha384.update(tohash.encode('utf-8'))
        hashresult = hashersha384.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == 'hashersha3_224':
        tohash = input('Input text to hash: ')
        hashersha3_224.update(tohash.encode('utf-8'))
        hashresult = hashersha3_224.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)


    elif hashtype == 'hashersha3_256':
        tohash = input('Input text to hash: ')
        hashersha3_256.update(tohash.encode('utf-8'))
        hashresult = hashersha3_256.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)
    elif hashtype == 'hashersha3_384':
        tohash = input('Input text to hash: ')
        hashersha3_384.update(tohash.encode('utf-8'))
        hashresult = hashersha3_384.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == "hashersha3_512":
        tohash = input('Input text to hash: ')
        hashersha3_512.update(tohash.encode('utf-8'))
        hashresult = hashersha3_512.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == "hashersha512":
        tohash = input('Input text to hash: ')
        hashersha512.update(tohash.encode('utf-8'))
        hashresult = hashersha512.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)
    elif hashtype == "hashershake_128":
        tohash = input('Input text to hash: ')
        hashersha512.update(tohash.encode('utf-8'))
        hashresult = hashersha512.hexdigest()
        print(hashresult)
        hash_Reroute(hashresult)

    elif hashtype == "hashershake_256":
        tohash = input('Input text to hash: ')
        hashershake_256.update(tohash.encode('utf-8'))

        length = int(input("Input hash length 128 up to 256: "))
        hashresult = hashershake_256.hexdigest(length)
        print(hashresult)
        hash_Reroute(hashresult)     
            

        print(hashresult)
        #hash_Reroute(hashresult)
    else:
        hash_Error()

def hash_Error():
    errorinput = input("That is not a valid hash return to main menu or exit? 'm' or'e'")
    print(errorinput)
    if errorinput == "m":
        clearConsole()
        InitiateApp()

    elif errorinput == "M":
        clearConsole()
        InitiateApp()
    elif errorinput == "e":
            exit()
    elif errorinput == "E":
            exit()
    else:
        input("Enter m or e to reoute to main menu or exit program")
        errorinput
    
def hash_Reroute(hashresult):
    user_resp = input("Type 'm' for main menu or 'e' to exit program or, to copy hash to clipboard type 'c'\n ")

    if user_resp == "m":
            clearConsole()
            InitiateApp()
    elif user_resp == "M":
            clearConsole()
            InitiateApp()
    elif user_resp == "e":
        exit()
    elif user_resp == "E":
        exit()
    elif user_resp == "C":
        try:
            clipboard.copy(hashresult)
            print("Copied to Clipboard!")      
            time.sleep(5)          
            clearConsole()
            InitiateApp()
        except:
            print("Copy failed!")
            time.sleep(5)
            clearConsole()
            InitiateApp()
            
    elif user_resp == "c":
        try:
            clipboard.copy(hashresult)
            print("Copied to Clipboard!")  
            time.sleep(5)              
            clearConsole()
            InitiateApp()
        except:
            print("Copy failed!")
            time.sleep(5)
            clearConsole()
            InitiateApp()
    else:
        input("Enter 'm' or 'e' to reoute to main menu or exit program")
        user_resp


            


InitiateApp()
