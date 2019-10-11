# 1. Helper methods and code

Link: https://wiki.python.org/moin/BitwiseOperators

## 1.1 Using a XOR for the bits

```python
x ^ y
```

## 1.2 Shift 

Right shift

- Shift the bits right by y places. This is equivalent to dividing x by 2<sup>y</sup>

```python
x >> y
```

## 1.3 Useful conversions

1 = 00001

31 = 11111

32 = 100000

2**19-1 = 524287 = 00000000000001111111111111111111 (This has 19 1s)

2**76-1 = Basically something that has 76 1s

# 2. Understanding bits and their index

- Leftmost bit is k79
- Rightmost bit is k0

```
k79 k78 k77 ... k3 k2 k1 k0 
```



# 3. Implementing present

Function 1: addRoundKey

- For this it XORs the key and the state 

```python
def addRoundKey(state, Ki):
    state = state ^ Ki
    return state
```

Function 2: sBox Layer

- Input: 64 bit input
- Output: 64 bit output after the substitution
- We do 4 bits by 4 bits starting from the LSB. These 4 bits (We call it SBOXIN) are passed into the SBox, manipulated to say SBOXOUT. We use SBOXOUT to replace the original SBOXIN
- We first need a mask of 0xF which is `1111` in bits. 
- We also intitialize with `0000 0000`
- To illustrate how the sBox works, let's imagine we use an 8 bit input `1011 1001`
- We for loop through the range of indices. 
  - The first index is 0
    - Now we use the mask on the whole input which is `1011 1001 & 0000 1111` which produces `0000 1001` which is essentially the first 4 LSB
    - We pass this into the SBOX to make the substitution. 1001 is 9 and we map it to the SBOX which produces 0xE which is 1110
    - We then need to shift it left by i*4 which is 0 for now so we have `0000 1110` 
    - We append this to the output with an OR operation. `0000 0000 | 0000 1110` which gives `0000 1110`
    - Then shift the state by 4 bits to the right to prepare for the next step so we get `0000 1011`
  - The second index is 1
    - Now we use the mask on the whole input which is `0000 1110 & 0000 1111` which produces `0000 1110` which is essentially the new first 4 LSB
    - We pass this into the SBOX to make the substitution. 1110 is 14 and we map it to the SBOX which produces 0x1 which is 0001
    - We then need to shift it left by i*4 which is 1 so we shift each bit by 4 to the left for now so we have `0001 0000` 
    - We append this to the output with an OR operation. `0001 0000 | 0000 1110` which gives `0001 1110` which does not interfere with our first operation on index 0

```python
def sBoxLayer(state):
    mask = 0xf
    output = 0
    for i in range(16):
        sboxOut = sbox[state & mask]
        output = output | (sboxOut<<(i*4))
        state = state >> 4
    return output
```

Function 3



Function 4



