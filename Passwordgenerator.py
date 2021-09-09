import string as s
from random import *


ch = s.ascii_letters + s.digits + s.ascii_uppercase
password = "".join (choice (ch) for x in range (randint(8,10)))

print (password)
