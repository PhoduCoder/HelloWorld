##Sample script to generate 
## a random password.
##This password should fulfill
##min 8 characters, max 15 characters
##a special characters 
##Author: Gaurav Parashar

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print password
