from string import ascii_lowercase
import time
import itertools 
import hashlib
import random
import json
try:
    import pandas as pd
except:
    pass

random.seed(1)

# Original values after decrypting hash5.txt
def break_hash():
    mapping = {}
    hash_ls = []
    answer_ls = []
    test_cases = 0
    success = 0
    # Read in the hashes
    with open("hashes.txt") as f: 
        banned_list = ['=== Weak ===', '=== Moderate ===', '=== Strong ===', '']
        for line in f:
            line = line.rstrip('\n')
            if line not in banned_list:
                hash_ls.append(line)
                test_cases += 1
    # Create a dictionary of the mappings
    #with open("10-million-password-list-top-1000000.txt") as f1:
    with open("100KDict.txt") as f1: 
        for line in f1:
            line = line.rstrip('\n')
            a = hashlib.new('md5')
            encoded_combination = line.encode('utf-8')
            a.update(encoded_combination)
            hashed_string = a.hexdigest()
            mapping[hashed_string] = line
    # Store into JSON
    with open('mapping.json', 'w') as fp:
        json.dump(mapping, fp)
    # Look for the decrypted values and add them to a list
    for indiv_hash in hash_ls:
        try:
            answer_ls.append(mapping[indiv_hash])
            success += 1
        except:
            answer_ls.append('error')
    print('The success rate is {}'.format(success/test_cases))
    return (hash_ls, answer_ls)

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
decryption_result = break_hash()
save_to_df(decryption_result[0], decryption_result[1], 'competition.csv')
print("Total running time is %s seconds" % (time.time() - start_time))





