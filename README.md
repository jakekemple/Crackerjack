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
  
### External Resources & Documentation:

1. [Multiprocessing Library](https://docs.python.org/3/library/multiprocessing.html)

