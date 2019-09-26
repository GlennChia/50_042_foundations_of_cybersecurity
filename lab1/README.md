# 1. Question 1

## 1.1 About string.printable()

<u>**string.printable() documentation**</u>

Documentation: https://docs.python.org/3/library/string.html
String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.

<u>**Understanding the code point range**</u> 

Link: https://realpython.com/python-encodings-guide/

| Code point range | Class                                     |
| ---------------- | ----------------------------------------- |
| 0 - 31           | Control/non-printable characters          |
| 32 - 64          | Punctuation, symbols, numbers, and space  |
| 65 - 90          | Uppercase English alphabet letters        |
| 91 - 96          | Additional graphemes, such as `[` and `\` |
| 97 - 122         | Lowercase English alphabet letters        |
| 123 - 126        | Additional graphemes, such as `{` and `   |
| 127              | Control/non-printable character (`DEL`)   |

- Hence only 32 (inclusive) to 126 (Inclusive) is printable 

- BUT when we use string.printable we can see that the index from 94-99 show nothing because they are string printable but not printable on the console

  ```
  94
  
  95
  
  96
  
  
  97
  
  98
  
  
  99
  
  ```

  

**<u>Characteristics</u>**

```python
import string
print(len(string.printable)) # 100
```

## 1.2 ASCII characters and their mapping

https://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html

## 1.3 Raising/throwing errors in python

https://realpython.com/python-exceptions/

```python
if value < 10:
    raise('please increase the value')
```

## 1.4 Checking if something is an integer

<u>**Checking if a string is actually an integer**</u>

```python
str.isdigit()
```

**<u>Checking if a variable is already an integer</u>**

Link: https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not

```python
isinstance(<var>, int)
```

## 1.5 Converting string to ASCII

Link: https://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python

```python
someString = 'hello'
ls = [ord(c) for c in someString] # [104, 101, 108, 108, 111]
```

## 1.6 Converting ASCII encoding to String

```python
chr(104) # 'h'
chr(97) # 'a'
```

## 1.7 Reading and writing to utf-8

Link: https://stackoverflow.com/questions/19591458/python-reading-from-a-file-and-saving-to-utf-8

```python
import io
with io.open(filename, 'r', encoding='utf8') as f:
    text = f.read()
# process Unicode text
with io.open(filename, 'w', encoding='utf8') as f:
    f.write(text)
```

## 1.8 About the map function

Link: https://book.pythontips.com/en/latest/map_filter.html

The for loop version

```python
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

The lambda and map way

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

## 1.9 Running the code

**<u>Sherlock</u>**

Encryption

```shell
./shiftcipher.py -i sherlock.txt -o sherlock.encrypt.txt -k 3 -m e
```

Decryption

```shell
./shiftcipher.py -i sherlock.encrypt.txt -o sherlock.decrypt.txt -k 3 -m d
```

# 2. Question 2

## 2.1 Some conversions

1 byte = 8 bits

- Maximum: unsigned 1111 111 = 0xFF = 255
- Minimum: unsigned 0 = 0x00 = 0

Hence the key is between 0 and 256 (Non inclusive for both) which is 

- 0x00 < key < 0xFF
- 0 < key < 256

## 2.2 ASCII and Hex

https://www.rapidtables.com/convert/number/ascii-to-hex.html

## 2.3 Reading ASCII as byes

Read in binary mode

```python
with open('some.txt', 'br') as file:
    ba = bytearray(file.read())
```

Write in binary mode 

- This reflects the unprintable characters

```
Input: defghijklmnopqrstuvwxyz{|}~ !0
Output after shifting by 192: $%&'()*+,-./0123456789:;<=>��� 
```

## 2.4 Testing the code

<u>**Simple text file**</u>

Encryption

```shell
./shiftcipher2.py -i simple.txt -o simple.encrypt2.txt -k 3 -m e
```

Decryption
```shell
./shiftcipher2.py -i simple.encrypt2.txt -o simple.decrypt2.txt -k 3 -m d
```

**<u>Sherlock</u>**

Encryption

```shell
./shiftcipher2.py -i sherlock.txt -o sherlock.encrypt2.txt -k 3 -m e
```

Decryption

```shell
./shiftcipher2.py -i sherlock.encrypt2.txt -o sherlock.decrypt2.txt -k 3 -m d
```

# 3. Question 3

## 3.1 Checking the file type

Run this command in the terminal 

```
file image
image: PNG image data, 1200 x 1200, 8-bit/color RGBA, non-interlaced
```

Alternative commands

Link: https://stackoverflow.com/questions/2227182/how-can-i-find-out-a-files-mime-type-content-type

```bash
> file --mime-type image.png
image.png: image/png

> file -b --mime-type image.png
image/png

> file -i FILE_NAME
image.png: image/png; charset=binary
```



## 3.2 Perform computations and assign them to a variable

### 3.2.1 About the $()

Link: https://stackoverflow.com/questions/27472540/difference-between-and-in-bash/27472808

The expression `$(command)` is a modern synonym for ``command`` which stands for command substitution; it means, run `command` and put its output here

Example:

```bash
echo "Today is $(date). A fine day."
```

- will run the `date` command and include its output in the argument to `echo`.

### 3.2.2 Computations and assigning the result

Link 1: https://stackoverflow.com/questions/5674022/how-to-pipe-bc-calculation-into-shell-variable

Example given

```bash
MYVAR=$(echo "scale 4;3*2.5" |bc)
```

Link 2: https://www.lifewire.com/use-the-bc-calculator-in-scripts-2200588

```bash
#!/bin/bash
echo '6.5 / 2.7' | bc
```

The [echo](https://www.lifewire.com/output-text-to-the-screen-linux-echo-command-3572040) command generates a string containing the mathematical expression contained in single quotes (6.5 divided by 2.7, in this example). The [pipe](https://www.lifewire.com/redirection-operator-2625979) operator (|) passes this string as an argument to the bc program. The output of the bc program is then displayed on the command line.

## 3.3 Conditionals

**Link 1:** https://bash.cyberciti.biz/guide/If..else..fi

**Link 2 about fi:** https://stackoverflow.com/questions/7010830/bash-whats-the-use-of-fi

fi closes the if statement, while ;; closes the current entry in the case statement.

## 3.4 Removing files

Standard file removal - `rm` command 

Link: https://www.tldp.org/LDP/abs/html/basic.html

```bash
rm some_file
```



## 3.5 Symbols

### 3.5.1 What is >

Link: https://fosspost.org/education/linux-command-line-basics-exampless

Take the output of a command and redirect it into a file (will overwrite the whole file).

### 3.5.2 What is $1

Link: https://www.unix.com/unix-for-dummies-questions-and-answers/90037-what-1-a.html

**$1** is the first commandline argument. If you run **./asdf.sh a b c d e**, then **$1** will be a, **$2** will be b, etc. In shells with functions, **$1** may serve as the first function parameter, and so forth.

Example: So when we use the command run ./bash.sh 50, $1 is the 50

## 3.6 xdg-open

https://www.geeksforgeeks.org/xdg-open-command-in-linux-with-examples/

- **xdg-open command** in the Linux system is used to open a file or URL in the user’s preferred application.
- The URL will be opened in the user’s preferred web browser if a URL is provided. 
- The file will be opened in the preferred application for files of that type if a file is provided.
- xdg-open supports *ftp*, *file*, *https* and *http* URLs. 
- This can be used inside a desktop session only. 
- It is not recommended to use xdg-open as root. Here, the zero is an indication of success while non-zero show the failure.

## 3.7 Outputting to `>/dev/null`

`>/dev/null` redirects the command standard output to the null device, which is a special device which discards the information written to it. What we are doing is to throw the command outputs into it




## 3.8 Bash file to run the key checker

```shell
rm "$1".plaintext > /dev/null
k=-1
until [[ $(file --mime-type "$1".plaintext) == *"image/png" ]]; do
    k=$(echo $k + 1 | bc)
    if (( k > 255 )); then
        exit
    fi
    echo Trying key $k
    python3 ex2.py -i "$1" -k $k -m d
done

echo Obtained PNG file with key $k
xdg-open "$1".plaintext > /dev/null
```

## 3.9 Run the script to check the file types for each of the keys

We need the `./` because we are using relative path. Otherwise we need to use the absolute path

```shell
$ ./ex3.sh flag
```

