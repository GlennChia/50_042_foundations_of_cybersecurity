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

## 1.4 Converting bytes to integer

Link: https://docs.python.org/3/library/stdtypes.html

```python
int.from_bytes(b'\x00\x10', byteorder='big')
# 16
```

- The *byteorder* argument determines the byte order used to represent the integer. If *byteorder* is `"big"`, the most significant byte is at the beginning of the byte array.

# 2. Understanding bits and their index

- Leftmost bit is k79
- Rightmost bit is k0

```
k79 k78 k77 ... k3 k2 k1 k0 
```



# 3. Implementing present

## 3.1 Function 1: addRoundKey

- For this it XORs the key and the state 

```python
def addRoundKey(state, Ki):
    state = state ^ Ki
    return state
```

## 3.2 Function 2: sBox Layer

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

## 3.3 Function 3: pLayer

- Input: 64 bits
- Output: 64 bits
- Essentially it is a substitution. Based on the current position, we shift the location of that bit to another location based on a table
- We will need a mask of `0x01` so that we can do an `&` operation and isolate a single bit such that we can then shift it to its correct location
- I will illustrate this with a 16 bit example for the first 2 iterations. The 20 bit example is 1110 1001 0010 0101 1110
  - The first index is index 0
    - We shift the state by the index which is 0. Hence, the state is preserved. 
    - We then perform an `&` operation with `0x01` which makes the state `0000 0000 0000 0000 0000`
    - According to the mapping, the first bit will stay at its position. Hence it does not shift
    - We take this and XOR with the output (Output starts at 0).
    - Hence, the output is `0000 0000 0000 0000 0000`
  - The second index is index 1
    - We shift the state by the index which is 1. Hence we get `0111 0100 1001 0010 1111`
    - We then perform an `&` operation with `0x01` which makes the state `0000 0000 0000 0000 0001`
    - According to the mapping, the first index is mapped to the 16th index (index starts from 0). Hence, after the shift of 16 bits we have  `0001 0000 0000 0000 0000`
    - We take this and XOR with the output 
    - Hence, the output is now `0001 0000 0000 0000 0000`

```python
def pLayer(state):
    # use the pmt array for the mapping
    output = 0
    for i in range(64):
        shifted_value = ((state >> i) & 0x01) << pmt[i]
        output = output | shifted_value
    return output
```

## 3.4 Function 4: Generate the round keys (To be used in all rounds later)

The formula is given in the paper.

```python
def genRoundKeys(key):
    # roundKeys = []
    roundKeys = [32]
    for i in range(1,FULLROUND+2): # (K1 ... K32)
        roundKeys.append(key >> 16)
        # Perform the shift. [k79k78 . . . k1k0] = [k18k17 . . . k20k19]
        # Part 1 is to get the first 19 bits and then shift it to the left. 
        # Part 2 is to make bit 19 first bit
        key = ((key & (2**19-1)) << 61) | (key >> 19)
        # [k79k78k77k76] = S[k79k78k77k76]
        key = (sbox[key >> 76] << 76) | (key & (2**76-1))
        # [k19k18k17k16k15] = [k19k18k17k16k15] ⊕ round_counter
        # round_counter varies from 1(00001) to 32 (100000) but at 32 it doesn't flow back to affect anything
        key = key ^ (i << 15)
    return roundKeys
```

## 3.4 Decryption

Basically just reversing the steps

# 4. Implementing ECB

## 4.1 Displaying the image from the command line

Changing directory into the one with the code

```bash
/mnt/c/Users/Glenn/Desktop/Github/50_042_foundations_of_cybersecurity/lab4
```

Install ImageMagick

```bash
sudo apt-get install imagemagick
```

Displaying the image

```bash
display Tux.ppm
```

## 4.2 Running the ECB

Encryption

```bash
python ecb.py -i Tux.ppm -o qn3 -k 0 -m e
```

Decryption

```bash
python ecb.py -i qn3 -o Tux_d.ppm -k 0 -m d
```

## 4.3 Understanding the input

When I read in the Tux.ppm, I get

```
\n245 189 12 245 189 12 245 189 12 245 189 12 245 189 12 245 189 12 242 182 12 \n245 189 12 245 189 12 245 189 12 245 189 12 235 196 12 243 205 12 235 196 12 \n225 180 10 207 148 7 136 95 7 10 6 4 2 2 4 2 2 4 2 2 4 2 2 4 2 2 4 2 2 4 2 2 4 \n2
```

The range is from 0 to 255. 255 in bits is 1111 1111 (8bits)

present takes in 64 bit blocks and encrypts them. Hence, we need to find a way to read the stream 64 bits at a time

## 4.4 Reading in 64 bits/8bytes at a time

There is no way where we can read in 64 bits at a time. Instead, Python has a nice way of reading in 8 bytes at a time 

Link: https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte

```python
with open("myfile", "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        byte = f.read(1)
'''
Alternatively
'''
with open("myfile", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        byte = f.read(1)
```

My fear is that it misses the first byte. Hence, I tweak it a little

```python
with open("myfile", "rb") as f:
    finished = False
    while not finished:
        # Do stuff with byte.
        byte = f.read(1)
        if byte == b"":
            finished = True
```

## 4.5 Adding the padding

The simplest way is to to use an `&` with a 64 bit `1`. This ensures that `1`s from the original will remain as well as `0`. If the number of bits is less than that, it will be padded with `1`s

```python
fout.write((byte & (2**64-1)).to_bytes(8, byteorder='big'))
```



