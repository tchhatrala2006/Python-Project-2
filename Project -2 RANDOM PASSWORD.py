import random as r
import string as s


user=int(input("Enter the Password Length: "))
a=r.choices(s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation,k=user)
print("".join(a))