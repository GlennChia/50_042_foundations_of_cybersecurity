# 1. Part 1: Algebraic Structures

## 1.1 Polynomial 2 class

### 1.1.1 add and sub

- An important thing to note is that the array may be of different size. There are 2 options for dealing with this
- Hence, make the 2 arrays the same size by padding the shorter one with zeroes with an `append`

```python
if len_p1 > len_p2:
    for zero_counter in range(difference_length):
        p2._coeffs.append(0)
else:
    for zero_counter in range(difference_length):
        self._coeffs.append(0)
```

From this, we can then do the XOR

```python
for index, indiv_bit in enumerate(self._coeffs):
    add_result.append(p2._coeffs[index] ^ indiv_bit)
```

### 1.1.2 Multiplication

- For this part we will use the test case to illustrate
  - p1 = x<sup>5</sup>+x<sup>2</sup>+x  
  - modp = x<sup>8</sup>+x<sup>7</sup>+x<sup>5</sup>+x<sup>4</sup>+1

```python
print ('p1=x^5+x^2+x')
print ('p4=x^7+x^4+x^3+x^2+x')
print ('modp=x^8+x^7+x^5+x^4+1')
p1=Polynomial2([0,1,1,0,0,1])
p4=Polynomial2([0,1,1,1,1,0,0,1])
modp=Polynomial2([1,0,0,0,1,1,0,1,1]) # This is different from the one provided in the notes 
p5=p1.mul(p4,modp)
```

| Row  | Powers                        | Operation                                                    | New Result                                                   | Reduction | After reduction (XOR)                                        |
| ---- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| 1    | x<sup>0</sup> . P<sub>4</sub> |                                                              | x<sup>7</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x    | N         |                                                              |
| 2    | x<sup>1</sup> . P<sub>4</sub> | x . x<sup>7</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x | x<sup>8</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup> | Y         | x<sup>7</sup>+x<sup>3</sup>+x<sup>2</sup>+1                  |
| 3    | x<sup>2</sup> . P<sub>4</sub> | x . x<sup>7</sup>+x<sup>3</sup>+x<sup>2</sup>+1              | x<sup>8</sup>+x<sup>4</sup>+x<sup>3</sup>+x                  | Y         | x<sup>7</sup>+x<sup>5</sup>+x<sup>3</sup>+x+1                |
| 4    | x<sup>3</sup> . P<sub>4</sub> | x . x<sup>7</sup>+x<sup>5</sup>+x<sup>3</sup>+x+1            | x<sup>8</sup>+x<sup>6</sup>+x<sup>4</sup>+x<sup>2</sup>+x    | Y         | x<sup>7</sup>+x<sup>6</sup>+x<sup>5</sup>+x<sup>2</sup>+x+1  |
| 5    | x<sup>4</sup> . P<sub>4</sub> | x . x<sup>7</sup>+x<sup>6</sup>+x<sup>5</sup>+x<sup>2</sup>+x+1 | x<sup>8</sup>+x<sup>7</sup>+x<sup>6</sup>+x<sup>3</sup>+x<sup>2</sup>+x | Y         | x<sup>6</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x+1 |
| 6    | x<sup>5</sup> . P<sub>4</sub> | x . x<sup>6</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x+1 | x<sup>7</sup>+x<sup>6</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x | N         |                                                              |

We then take the `After reduction` results associated with row 2, 3, 6

Result = (x<sup>7</sup>+x<sup>3</sup>+x<sup>2</sup>+1) + (x<sup>7</sup>+x<sup>5</sup>+x<sup>3</sup>+x+1) + (x<sup>7</sup>+x<sup>6</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x) = x<sup>7</sup>+x<sup>6</sup>+x<sup>4</sup>+x<sup>3</sup>

<u>**Guide to doing the addition**</u>

Doing the first addition

|                                               | x<sup>0</sup> | x<sup>1</sup> | x<sup>2</sup> | x<sup>3</sup> | x<sup>4</sup> | x<sup>5</sup> | x<sup>6</sup> | x<sup>7</sup> |
| --------------------------------------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| x<sup>7</sup>+x<sup>3</sup>+x<sup>2</sup>+1   | 1             |               | 1             | 1             |               |               |               | 1             |
| x<sup>7</sup>+x<sup>5</sup>+x<sup>3</sup>+x+1 | 1             | 1             |               | 1             |               | 1             |               | 1             |
| Result                                        | 0             | 1             | 1             | 0             | 0             | 1             | 0             | 0             |

Doing the second addition

|                                                              | x<sup>0</sup> | x<sup>1</sup> | x<sup>2</sup> | x<sup>3</sup> | x<sup>4</sup> | x<sup>5</sup> | x<sup>6</sup> | x<sup>7</sup> |
| ------------------------------------------------------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| x<sup>5</sup>+x<sup>2</sup>+x                                |               | 1             | 1             |               |               | 1             |               |               |
| x<sup>7</sup>+x<sup>6</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x |               | 1             | 1             | 1             | 1             | 1             | 1             | 1             |
| Result                                                       | 0             | 0             | 0             | 1             | 1             | 0             | 1             | 1             |

The result is x<sup>7</sup>+x<sup>6</sup>+x<sup>4</sup>+x<sup>3</sup>

### 1.1.3 Division



## 1.2 Galois field class





# Misc: Bug fixes

## 1. Using the class' `__str__()` method

I could not get it to work initially because I was returning the result as `return add_result` 

Instead, I need to return an Object which will be captured by the test case and then printed. Previously I returned an array and when we print it, it just printed an array.

Line 7 is the issue and we change it to the commented code 

```python
class Polynomial2:
    def __init__(self,coeffs):
        self._coeffs = coeffs
        
    def add(self,p2):
        # Some logic here
        return add_result # Polynomial2(add_result) 
    
    def __str__(self):
        formatted_polynomial = ''
        temporary_coeffs = self._coeffs
        temporary_coeffs.reverse()
        for index_coeff, indiv_coeff in enumerate(temporary_coeffs):
            if index_coeff == len(temporary_coeffs) - 1:
                if indiv_coeff == 1:
                    formatted_polynomial += 'x^{}'.format(0)
                else:
                    formatted_polynomial = formatted_polynomial[: -1]
            else:
                if indiv_coeff == 1:
                    formatted_polynomial += 'x^{}+'.format(len(temporary_coeffs) - 1 - index_coeff)
        return formatted_polynomial

p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)  # OVER HERE WE SHOULD BE RETURNING AN OBJECT OF THE CLASS
print ('p3= p1+p2 = {}'.format(p3))  # WHEN WE PRINT THE OBJECT IT WILL PRINT THE STRING RETURNED FROM THE __str()__ METHOD
```

