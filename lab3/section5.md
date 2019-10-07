### Glenn Chia 1003118 (Lab 3 Section 5)

### 1. Generating the salt

For this lab, to ensure consistency of the results, imported the `random` library and initialised it with a seed `random.seed(1)`. Generate the random lowercase letters with `random.choice(ascii_lowercase)`

### 2. Results

Time taken for **<u>Unsalted</u>** (Left): 10.20s. Time taken for **<u>salted</u>**(Right): 16.30s

<img src="assets/06_rainbow_crack_win.PNG" style="zoom:30%;" />
<img src="assets/10_rainbow_crack_win_final.PNG" style="zoom:30%;" />

### 3. Analysis and and explain the difference between salted and non salted rcrack strategies

Adding a salt increases the cracking time by 6.10s. which is a 159.8% increase in the time.

Adding a different (Or in this case random) salt for each entry ensures that the attacker cannot use the same Rainbow table. For this lab, I had to generate 3 rainbow tables to break all 15 hashes. These rainbow tables had to work on strings of 6 characters. I could not use only one as the size of the table was insufficient (Not all the outputs would match). Hence, I could either increase the size of the table which meant that there would be a higher likelihood of a match or add new rainbow tables with different reduction functions. I chose the latter where each of these rainbow tables utilized their own reduction functions. When I combined them, there were more inputs and outputs that could match with the rainbow table after relevant iterations of hashing and reduction. Since more rainbow tables are used, more space is occupied and also more time is needed to vary the parameters to crack this particular combination of hashes.

With reference to the notes, adding an n bit salt essentially increases the effort by 2<sup>n</sup> times. In our case, adding 26 lower case characters to the mix increases the effort by 26 times for an attacker who is pre-computing the rainbow table 

