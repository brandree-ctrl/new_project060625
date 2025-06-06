import random
import string


length = int(input("Length of password:"))
Number_options = (85**length)


y = []

for x in range(int(Number_options)):
	s = "".join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_-+={}[]|~`?/.,><") for _ in range(length))
	packets = y.append(s)
print(y)
print(Number_options)