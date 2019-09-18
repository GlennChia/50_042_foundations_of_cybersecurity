from shiftcipher import encrypt
from shiftcipher import decrypt

#print(encrypt('abcdefghijk', 95))

# Encryption tests
def test_e_1():
    assert encrypt('abcdefghijk', 3) == 'defghijklmn', "Test 1 basic shift wrong"

def test_e_2():
    assert encrypt('abcdefghijk', 20) == 'uvwxyz{|}~ ', "Test 2 basic shift boundary edge wrong"

def test_e_3():
    assert encrypt('abcdefghijk', 21) == 'vwxyz{|}~ !', "Test 3 shift and exceed boundary wrong"

def test_e_4():
    assert encrypt('abcdefghijk', 30) == " !\"#$%&'()*", "Test 4 shift and all exceed boundary wrong"

def test_e_5():
    assert encrypt('abcdefghijk', 95) == "abcdefghijk", "Test 5 shift and all exceed and return original wrong"

def test_e_6():
    assert encrypt('abcdefghijk', 99) == "efghijklmno", "Test 6 shift and all exceed and return original wrong"

def test_e_7():
    assert encrypt('abcdefghijk', 125) == " !\"#$%&'()*", "Test 7 shift and all exceed twice wrong"

# Decrypt 
def test_d_1():
    assert decrypt('defghijklmn', 3) == 'abcdefghijk', "Test 1 basic shift wrong"

def test_d_2():
    assert decrypt('uvwxyz{|}~ ', 20) == 'abcdefghijk', "Test 2 basic shift boundary edge wrong"

def test_d_3():
    assert decrypt('vwxyz{|}~ !', 21) == 'abcdefghijk', "Test 3 shift and exceed boundary wrong"

def test_d_4():
    assert decrypt(" !\"#$%&'()*", 30) == "abcdefghijk", "Test 4 shift and all exceed boundary wrong"

def test_d_5():
    assert decrypt('abcdefghijk', 95) == "abcdefghijk", "Test 5 shift and all exceed and return original wrong"

def test_d_6():
    assert decrypt('efghijklmno', 99) == "abcdefghijk", "Test 6 shift and all exceed and return original wrong"

def test_d_7():
    assert decrypt(" !\"#$%&'()*", 125) == 'abcdefghijk', "Test 7 shift and all exceed twice wrong"

if __name__ == "__main__":
    print('Running encryption tests')
    test_e_1()
    test_e_2()
    test_e_3()
    test_e_4()
    test_e_5()
    test_e_6()
    test_e_7()
    print('Running decryption tests')
    test_d_1()
    test_d_2()
    test_d_3()
    test_d_4()
    test_d_5()
    test_d_6()
    test_d_7()
    print("Everything passed")