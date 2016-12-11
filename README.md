# Crackerjack: Multiprocessing brute-force application
## Written with multiprocessing library in python 3 

This project was started for CSC 596: Special Readings, A research credit course at Missouri State University


### Get Started 
- Install python 3 if you do not already have it
- Clone the repository 


### How to run:
- From the crackerjack project directory, run
		`python crackerjack [character set] [max length]`
  in a terminal window (character set is a string, max length is an integer).
  Note: If you have both Python 2 & 3 installed, run with `python3` instead
- For [character set], this is where you will put the string of characters you want to be ran through the possibility checker. All possible combinations of characters will be built from the character set. 
- For [max length], choose an integer to designate a max size the possibility checker will run up to on [character set], PER PROCESS. For example, if the process is checking 'abc' with a set [max length] of 2, the script will compute all possible combinations of 'abc' as 2 character strings: 'aa', 'ab', 'ac', etc..

### Selecting a charset:
The [charset] argument determines which group of characters you want to brute-force against. For example choosing 3 will try all possible combinations of the alphabet (uppercase and lowercase) and digits.

Charset Key:
 
 - 1: digits
 ```0123456789```
 
 - 2: letters (lower) and digits
 ```0123456789abcdefghijklmnopqrstuvwxyx```

 - 3: letters (upper and lower)
 ```ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx```

 - 4: letters (upper and lower) and digits
 ```0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx```

 - 5: letters (upper and lower) and common special characters 
 ```ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx!#$%&'()*+,-./:;<=>?@[\]^_`{|}~```

 - 6: letters (upper and lower), digits, and common special characters 
 ```0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx!#$%&'()*+,-./:;<=>?@[\]^_`{|}~```

* Note: All times are for class D attacks (10 million attempts per second)

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

  
### External Resources & Documentation:

1. [Multiprocessing Library](https://docs.python.org/3/library/multiprocessing.html)

