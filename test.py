import random, string
lenght = 100



all_symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

result = ''
for i in range(lenght):
    result += random.choice(all_symbols)
print(result)
