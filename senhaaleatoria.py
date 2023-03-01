import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all = lower + upper + numbers
lenght = 8
senha = "".join(random.sample(all, lenght))
print(senha)
    