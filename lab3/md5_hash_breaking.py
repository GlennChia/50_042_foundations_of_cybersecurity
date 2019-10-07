import requests
import json
import time
try:
    import pandas as pd
except:
    pass


# Original values after decrypting hash5.txt
def break_hash():
    mapping = {}
    hash_ls = []
    answer_ls = []
    test_cases = 0.0
    success = 0.0
    # Read in the hashes
    with open("hashes.txt") as f: 
        banned_list = ['=== Weak ===', '=== Moderate ===', '=== Strong ===', '']
        for line in f:
            line = line.rstrip('\n')
            if line not in banned_list:
                hash_ls.append(line)
                test_cases += 1
    # Read my own JSON mapper
    # Online tools used: https://hashkiller.co.uk/Cracker/MD5
    with open('glenn_mapping.json') as json_file:
        data = json.load(json_file)
    # Look for the decrypted values and add them to a list
    for indiv_hash in hash_ls:
        print(indiv_hash)
        try:
            url = "http://www.nitrxgen.net/md5db/{}.json".format(indiv_hash)
            headers = {
                'Accept': "*/*",
                'Cache-Control': "no-cache",
                'Host': "www.nitrxgen.net",
                'Accept-Encoding': "gzip, deflate",
                'Connection': "keep-alive",
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers)
            response_json = json.loads(response.text)
            decrypted_hash = response_json['result']['pass']
            if decrypted_hash != '':
                answer_ls.append(decrypted_hash)
                success += 1
            else:
                try:
                    decrypted_hash = data[indiv_hash]
                    answer_ls.append(decrypted_hash)
                    success += 1
                except:
                    answer_ls.append('error')
        except:
            answer_ls.append('error')
    print('The success rate is {}'.format(success/test_cases))
    return (hash_ls, answer_ls)

def save_to_df(hashed_value, decrypted_ls, file_name):
    answerdf = pd.DataFrame()
    answerdf['hashedValue'] = hashed_value
    answerdf['unhashed'] = decrypted_ls
    answerdf.to_csv(file_name)

start_time = time.time()
decryption_result = break_hash()
save_to_df(decryption_result[0], decryption_result[1], 'competition.csv')
print("Total running time is %s seconds" % (time.time() - start_time))
