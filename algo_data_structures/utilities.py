import random

def generate_list(elements):
    result = []
    for i in range (0,elements):
        element = random.randint(0,100)
        result.append(element)
    return result