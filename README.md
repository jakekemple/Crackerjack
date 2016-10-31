# Crackerjack: Multiprocessing brute-force application
## Written with multiprocessing library in python 3 

This project was started for CSC 596: Special Readings, A research credit course at Missouri State University


### Get Started 
- Clone the repository 


### How to run:
- From the crackerjack project directory, run
		`python crackerjack [character set] [chunk size]`
  in a terminal window (character set is a string, chunk size is an integer).
  Note: If you have both Python 2 & 3 installed, run with `python3` instead
- For [character set], this is where you will put the string of characters you want to be ran through the possibility checker. All possible combinations of characters will be built from the character set. 
- For [chunk size], choose an integer to designate a max size the possibility checker will run up to on [character set], PER PROCESS. For example, if the process is checking 'abc' with a set [chunk size] of 2, the possibilty will show all combinations of 'abc' as 2 character strings.
  
### External Resources & Documentation:

1. [Multiprocessing Library](https://docs.python.org/3/library/multiprocessing.html)

