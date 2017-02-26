mysring = "ThiS is String with Upper and lower case Letters"
alphabet = ["a","c","d","e","g","h","i","l","n","o","p","r","s","t","u","w"]

def count (mystring,f_letter):
    count=0
    for letter in alphabet:
        if (letter.lower()== f_letter.lower()):
            count+=1
    return count
for letter in alphabet:
    n=count(mystring,letter)
    if (n>0):
        print("{0} {3}".format(letter,n))





##myString = ("ThiS is String with Upper and lower case Letters").lower().replace(" ","")
##print("a",myString.count('a'))
##print("c",myString.count('c'))
##print("d",myString.count('d'))
##print("e",myString.count('e'))
##print("g",myString.count('g'))
##print("h",myString.count('h'))
##print("i",myString.count('i'))
##print("l",myString.count('l'))
##print("n",myString.count('n'))
##print("o",myString.count('o'))
##print("p",myString.count('p'))
##print("r",myString.count('r'))
##print("s",myString.count('s'))
##print("t",myString.count('t'))
##print("u",myString.count('u'))
##print("w",myString.count('w'))

