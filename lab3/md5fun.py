from string import ascii_lowercase
import time
import itertools 
import hashlib
import random
try:
    import pandas as pd
except:
    pass

random.seed(1)

# Original values after decrypting hash5.txt
original_values = ['opmen', 'tthel', 'cance', 'nized', 'tpoin', 'aseas', 'dsmto', 'egunb', 'mlhdi', 'ofror', 'hed4e', 'di5gv', 'owso9', 'sso55', 'lou0g']
def break_five_char():
    mapping = {}
    test_string = '1234567890abcdefghijklmnopqrstuvwxyz'
    answer_ls = []
    # Read in the hashes
    with open("hash5.txt") as f: 
        hash_ls = [line.rstrip('\n') for line in f]
    # Generate the mapping of hash value to decrypted values
    combinations = itertools.product(test_string, repeat=5)
    for indiv_combinations in combinations:
        indiv_combinations = ''.join(indiv_combinations)
        a = hashlib.new('md5')
        encoded_combination = indiv_combinations.encode('utf-8')
        a.update(encoded_combination)
        hashed_string = a.hexdigest()
        mapping[hashed_string] = indiv_combinations
    # Look for the decrypted values and add them to a list
    for indiv_hash in hash_ls:
        try:
            answer_ls.append(mapping[indiv_hash])
        except:
            answer_ls.append('error')
    return answer_ls

def generateNormalHash(list_to_hash):
    hashed_list = []
    normal_list = []
    letters = ascii_lowercase
    for indiv_values in list_to_hash:
        # Generate a random lower case character and add it to the value
        indiv_values += random.choice(letters)
        normal_list.append(indiv_values)
        # Hash the 6 char string
        a = hashlib.new('md5')
        encoded_combination = indiv_values.encode('utf-8')
        a.update(encoded_combination)
        hashed_string = a.hexdigest()
        hashed_list.append(hashed_string)
    with open('salted6.txt', 'w') as f:
        for indiv_hashes in hashed_list:
            f.write(indiv_hashes) 
            f.write('\n')
    return (hashed_list, normal_list)


def save_to_df(hashed_value, decrypted_ls, file_name):
    answerdf = pd.DataFrame()
    answerdf['hashedValue'] = hashed_value
    answerdf['unhashed'] = decrypted_ls
    answerdf.to_csv(file_name)

start_time = time.time()
# print(break_five_char())
results = generateNormalHash(original_values)
save_to_df(results[0], results[1], 'salted6.csv')
print("Total running time is %s seconds" % (time.time() - start_time))





