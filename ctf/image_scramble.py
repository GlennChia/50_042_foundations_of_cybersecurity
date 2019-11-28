import base64
import random

random.seed(1)
random_sequence = random.sample(range(0, 8), 8)
print(random_sequence)

# Permutaion function retrieved from https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 
    l = [] 
    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 

def image_to_bytes(image_path):
    with open(image_path, "rb") as image:
        str1 = base64.b64encode(image.read())
    fragments = []
    for index, value in enumerate(random_sequence):
        fragments.append(str1[len(str1)*value:len(str1) * (value + 1)])
    fragmented = b''
    for i in fragments:
        fragmented += i
    with open('encrypt.txt', 'wb') as text:
        text.write(fragmented)
    return True

def bytes_to_image(encrypt_path):
    with open(encrypt_path, "rb") as image:
        original = image.read()
        fragments = []
        for i in range(8):
            fragments.append(original[len(original)*i:len(original) * (i + 1)])
        fragmented = b''
        while random_sequence != []:
            value = random_sequence.index(min(random_sequence))
            fragmented += fragments[value]
            random_sequence.remove(min(random_sequence))
        str1 = base64.b64decode(fragmented)
    with open('image.PNG', 'wb') as text:
        text.write(str1)
    return True

def bytes_to_image_brute_force(encrypt_path):
    permutations = permutation(list('1234567'))

    with open(encrypt_path, "rb") as image:
        original = image.read()
        fragments = []
        for i in range(8):
            fragments.append(original[len(original)*i:len(original) * (i + 1)])
    for index, permutation_indiv in enumerate(permutations):
        permutation_copy = permutation_indiv
        fragmented = b''
        while random_sequence != []:
            value = permutation_copy.index(min(permutation_copy))
            fragmented += fragments[value]
            permutation_copy.remove(min(permutation_copy))
        str1 = base64.b64decode(fragmented)
        file_out_name = 'image{}.PNG'.format(index)
        with open(file_out_name, 'wb') as text:
            text.write(str1)
    return True

  
image_to_bytes('raw_hash.PNG')
bytes_to_image('encrypt.txt')