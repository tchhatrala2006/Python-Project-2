import random as r
import string as s

l=[]
letter=int(input("Enter the Letter Length: "))
digit=int(input("Enter the Digit Length: "))
special_character=int(input("Enter the special_character Length: "))

letter_length=r.choices(s.ascii_letters,k=letter)
digit_length=r.choices(s.digits,k=digit)
special_character_length=r.choices(s.punctuation,k=special_character)

for i in letter_length:
    l.append(i)

for i in digit_length:
    l.append(i)

for i in special_character_length:
    l.append(i)

for i in l:
    r.shuffle(i)
    print(i,end="")

