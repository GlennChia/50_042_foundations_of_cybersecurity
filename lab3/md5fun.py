from string import ascii_lowercase
import time
import pandas as pd
import itertools 
import hashlib

answerdf = pd.DataFrame()

start_time = time.time()

mapping = {}
test_string = '1234567890abcdefghijklmnopqrstuvwxyz'
answer_ls = []


with open("hash5.txt") as f: 
    hash_ls = [line.rstrip('\n') for line in f]

# print(hash_ls)

combinations = itertools.product(test_string, repeat=5)

for indiv_combinations in combinations:
    indiv_combinations = ''.join(indiv_combinations)
    a = hashlib.new('md5')
    encoded_combination = indiv_combinations.encode('utf-8')
    a.update(encoded_combination)
    hashed_string = a.hexdigest()
    mapping[hashed_string] = indiv_combinations

for indiv_hash in hash_ls:
    try:
        answer_ls.append(mapping[indiv_hash])
    except:
        answer_ls.append('error')

print(answer_ls)

print("--- %s seconds ---" % (time.time() - start_time))

answerdf['hashedValue'] = hash_ls
answerdf['unhashed'] = answer_ls
answerdf.to_csv('3_brute_force.csv')

