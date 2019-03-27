#password_gen.py
import random
import string

user_passlength = input("How many characters do you want your password to be?: ")
user_passlength = int(user_passlength) #turns user input into an integer

letter = string.ascii_letters + string.digits + string.punctuation  #can remove string.punctuation if we just want letters and numbers
pattern_list = string.ascii_letters + string.digits + string.punctuation  # " "
out_string = ''
length = user_passlength
for num in range(length):
    out_string = out_string + random.choice(pattern_list)
print(out_string)
