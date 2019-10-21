# Glenn Chia 1003118

50.042 Foundations of Cybersecurity Lab 5

# 1. Create a table for addition and multiplication for GF(2<sup>4</sup>), using (x<sup>4</sup> + x<sup>3</sup>+ 1) as the modulus.

For this test case we will use 

- g4 = x<sup>3</sup>+x<sup>2</sup>+1  
- g5 = x<sup>2</sup>+x

| Row  | Powers                        | Operation                         | New Result                    | Reduction | After reduction (XOR) |
| ---- | ----------------------------- | --------------------------------- | ----------------------------- | --------- | --------------------- |
| 1    | x<sup>0</sup> . g<sub>4</sub> |                                   | x<sup>3</sup>+x<sup>2</sup>+1 | N         |                       |
| 2    | x<sup>1</sup> . g<sub>4</sub> | x . x<sup>3</sup>+x<sup>2</sup>+1 | x<sup>4</sup>+x<sup>3</sup>+x | Y         | x + 1                 |
| 3    | x<sup>2</sup> . g<sub>4</sub> | x . x+1                           | x<sup>2</sup>+x               | N         |                       |

We then take the `After reduction` results associated with row 2, 3

Result = (x<sup>2</sup> + x) + (x+1)  = x<sup>2</sup>+1

**Addition table**

|                   | x<sup>0</sup> | x<sup>1</sup> | x<sup>2</sup> | x<sup>3</sup> |
| ----------------- | ------------- | ------------- | ------------- | ------------- |
| x<sup>2</sup> + x | 0             | 1             | 1             | 0             |
| x+1               | 1             | 1             | 0             | 0             |
| Result            | 1             | 0             | 1             | 0             |

Result is x<sup>2</sup>+1

<div style="page-break-after: always;"></div>

# 2. Second example with a different GF(2<sup>n</sup>)

For this part we will use the test case to illustrate

- p1 = x<sup>5</sup>+x<sup>2</sup>+x  
- p4 = x<sup>7</sup>+x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x  
- modp = x<sup>8</sup>+x<sup>7</sup>+x<sup>5</sup>+x<sup>4</sup>+1

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

**Addition table** 

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

<div style="page-break-after: always;"></div>

# 3. Lab's test case

![](assets/test_case.PNG)