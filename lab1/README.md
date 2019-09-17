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

**<u>Characteristics</u>**

```python
import string
print(len(string.printable)) # 100
```

## 1.2 ASCIIcharacters and their mapping

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



## 1.6 Reading and writing to utf-8

Link: https://stackoverflow.com/questions/19591458/python-reading-from-a-file-and-saving-to-utf-8

```python
import io
with io.open(filename, 'r', encoding='utf8') as f:
    text = f.read()
# process Unicode text
with io.open(filename, 'w', encoding='utf8') as f:
    f.write(text)
```

## 1.7 Running the code
./shiftcipher.py -i sherlock.txt -o some.txt -k 3 -m e