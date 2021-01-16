letters_array = [element[0] for element in names]

print(letters_array)
"""
for i in range(5):
    numbers = [random.randint(0, 10) for x in range(4)]
    print (numbers)
"""

numbers2 = [[random.randint(0, 10) for x in range(4)] for y in range(5)]
print (numbers2)