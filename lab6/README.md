# 1. Part I: Implementing Square and Multiply

## 1.1 Square and multiply pseudo code is given in the notes

- Convert the integer to binary and convert that to a string so we can strip the `0b` at the front

## 1.2 miller_rabin

Pseudo code can be found on [https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test](https://en.wikipedia.org/wiki/Miller–Rabin_primality_test) 

Generating a random number in a range 

-  https://docs.python.org/2/library/random.html 
- `random.randint(a, b)` - Return a random integer *N* such that `a <= N <= b`.

Illustrating a prime number example 61 with 2 rounds

1. First we need to find r and d based on 61-1=60
2. 2<sup>2</sup> * 15 = 60.
   1. r = 2
   2. d = 15
3. Enter the first iteration of the loop
   1. Pick a random integer a between 2 and 61-2=59
   2. Let's say we choose 5
   3. x = 5<sup>15</sup>%61 = 60
   4. Check condition. If x=1 or x=n-1=60 we continue the loop. Since x=60 we thus continue with the loop. On to the second iteration
4. Second iteration of the loop
   1. This time we choose a=7
   2. x =  7<sup>15</sup>%61 = 11
   3. Check condition. If x=1 or x=n-1=60 we continue the loop but it is not
   4. Now we repeat r-1 times which is just 1 time
      1. x = 11<sup>2</sup>%61 = 60
      2. Check if x=n-1=60
      3. Since it is, we continue with the loop 
5. BUT, the loops is finished already
6. Hence the number is a prime number 

## 1.3 Generating prime numbers

For an n bit binary, the greatest number is 2<sup>n</sup>-1 but if there is 100 bits, this value is 1.2676505x10<sup>30</sup>

With this random number generated we check if it is prime. If it is, we return it, else we generate a new number and continue the loop

# 2. Part II: Diffie-Hellman Key Exchange (DHKE)



# 3. Part III: Baby-Step Giant-Step Method





# Open ended questions

## What’s the advantage and disadvantage of DHKE?  



## Increase the number of bits to break slowly. To avoid     attack using Baby-Step Giant-Stepsmethod, how many bits should the key be     in DHKE protocol?