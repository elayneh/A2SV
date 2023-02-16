import itertools as its
words = ["1234567890abcdefghijklmnopqrstuvwxyz"] # a set of password characters
r =its.product(words,repeat=5)  # random combination of 8 characters
dic = open("pwd_collection.txt","a")      # store wifi combinations in file
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
