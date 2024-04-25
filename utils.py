import random
import string

def generate_pass(length,numbers=True,characters=True):
    digits = string.digits
    letters = string.ascii_letters
    special = string.punctuation
    
    super_set = letters
    
    if numbers:
        super_set += digits
    if characters:
        super_set += special
        
    password = ''
    password = ''.join(random.choice(super_set) for _ in range(length))
    return password

