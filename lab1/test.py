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

if __name__ == "__main__":
    test_e_1()
    test_e_2()
    test_e_3()
    test_e_4()
    test_e_5()
    test_e_6()
    test_e_7()
    print("Everything passed")