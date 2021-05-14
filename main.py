import random
import string

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
try:
    pass_len = int(input("Enter password length : "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # random.shuffle(s)
    print("Your Generated password is:")
    # print("".join(s[0:pass_len])) or we can use
    p = random.sample(s, pass_len)
    print("".join(p))
except Exception as e:
    # print(e)
    print("Please enter a valid value")
