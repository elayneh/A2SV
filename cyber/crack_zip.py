# coding=UTF-8
"""
Brute force cracking of ZIP compression file password using a dictionary
"""
import zipfile
import threading

# Define a function to check if the password is correct
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode())
        print("Found Password : ", password)
        return password
    except Exception:
        # Exception handling
        pass

def main():
    # Specify the ZIP file to be cracked
    zFile = zipfile.ZipFile(input("Please enter the ZIP file you want to crack, for example: C:\\a.zip\n"))
    # Specify the dictionary file to be used
    dictfile = input("Please enter the dictionary file to be used, enter 0 to use the default dictionary\n")
    if dictfile == '0':
        dictfile = "pwd_collection.txt"
    passFile = open(dictfile)
    for line in passFile.readlines():  # Read the dictionary file line by line
        password = line.strip('\n')  # Delete extra line breaks
        t = threading.Thread(target=extractFile, args=(zFile, password))  # Create thread
        t.start()  # Start thread
        guess = extractFile(zFile, password)  # Try each line read password
        if guess:  # Successfully read
            print('Password = ', password)
            return
        else:
            continue
    print("password not found")

if __name__ == '__main__':
    main()
