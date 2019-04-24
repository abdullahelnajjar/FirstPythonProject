# generate a password with length "passlen" with no duplicate characters in the password

import random
import string

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
passlen = 12
p = "".join(random.sample(s, passlen))
print(p)



def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password? '))))


print(pw_gen(8))

