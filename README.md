# Crackerjack: Multiprocessing brute-force application
## Written with multiprocessing library in python 3 

This project was started for CSC 596: Special Readings, a research credit course at Missouri State University

## What is it?

Crackerjack is a simple multi-processing bruteforce script. Given character set and max length parameters, the script will try all combinations of the character set of size max length and smaller, all while utilizing all machine cores. The script only generates all possible combinations of the given parameters. It does NOT run those generated combinations against a hash or password test. That can be implemented based on the context you wish to use Crackerjack


### Get Started 
- Install python 3 if you do not already have it
- Clone the repository 


### How to run:
- From the crackerjack project directory, run
		`python crackerjack.py [charset] [maxlength]`
  in a terminal window (charset and maxlength are both integers).
  Note: If you have both Python 2 & 3 installed, run with `python3` instead
- For [charset], select an integer between 1 and 6. See "Selecting a charset" section below. 
- For [maxlength], choose an integer to designate the max size of words you wish to generate up to. For example, if you select 6, the script will generate all possible combinations of 6 character words from the charset.

### Selecting a charset:
The [charset] argument determines which group of characters you want to brute-force against. For example choosing 3 will try all possible combinations of the alphabet (uppercase and lowercase) and digits.

Charset Key:
 
1 (digits):
```
0123456789
```
 
2 (lowercase letters and digits):
```
0123456789abcdefghijklmnopqrstuvwxyz
```

3 (upper and lowercase letters):
```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```

4 (upper and lowercase letters and digits):
```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```

5 (upper and lowercase letters and common special characters):
```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

6 (upper and lowercase letters, digits, and common special characters):
```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&'()*+,-./:;<=>?@[\]^_{|}`~
```


Computation Times for password of length 5:

| charset       | time          | 
| ------------- |:-------------:|
| 1             | Instant       |
| 2             | Instant       |
| 3             | 35 sec        |
| 4             | 1.5 min       |
| 5             | ?             |
| 6             | 13.5 min      |

Computation Times for password of length 6:

| charset       | time          | 
| ------------- |:-------------:|
| 1             | Instant       |
| 2             | 200 sec       |
| 3             | 33 min        |
| 4             | 1.5 hours     |
| 5             | ?             |
| 6             | 22 hours      |

* Note: All times are for class D attacks (10 million attempts per second)

  
### External Resources & Documentation:

1. [Multiprocessing Library](https://docs.python.org/3/library/multiprocessing.html)
2. [Password Recovery Speeds](http://www.lockdown.co.uk/?pg=combi&s=articles)

