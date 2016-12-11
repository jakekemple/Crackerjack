# Crackerjack: Multiproccessing brute-force script
# Info: https://github.com/jakekemple/Crackerjack

import sys
import time
import multiprocessing as mp
from itertools import product

# generator is ran by the individual processes
def generator(first_char, wordtail_length, length):
    # Generate all strings of length `length` starting with `first_char`.
    # Once length > wordtail_length, only the wordtail_length characters
    # need to be generated.
    total_completed = 0
    if length <= wordtail_length:
        assert first_char == ""
        # creating all combinations of length charset here (short strings)
        for t in product(charset, repeat=length):
            result = "".join(t)
            #print(result)
            # To compare to hash or keyword, do something with result here
            total_completed += 1
    else:
        assert len(first_char) + wordtail_length == length
        # creating all combinations of length charset here (longer strings)
        for t in product(charset, repeat=wordtail_length):
            result = first_char + "".join(t)
            #print(result)
            # To compare to hash or keyword, do something with result here
            total_completed += 1 # word counter
    return total_completed

def count_completed(completed_chunk):
    global total_completed
    total_completed += completed_chunk
    #print(total_completed, 'completed')

# Bruteforce algorithm. Tests combination possibilities
# of characters in charset
def bruteforce(pool, chunk_size=1000000):
    charset_length = len(charset)

    # This chunk sets max largest wordtail_length to be
    # computed without separating jobs by first_char
    wordtail_length = 1
    while charset_length**wordtail_length <= chunk_size:
        wordtail_length += 1
    wordtail_length -= 1

    # short strings: generate words from size 1 to short words max
    max_short_len = min(wordtail_length, maxlength)
    for length in range(1, max_short_len + 1):
        pool.apply_async(generator, args=("", wordtail_length, length),
                         callback=count_completed)
    # longer strings: generate words from short words max to maxlength
    for length in range(max_short_len + 1, maxlength + 1):
        # Get the cartesian product chars in the charset
        for t in product(charset, repeat=length-wordtail_length):
            first_char = "".join(t) # Remove punctuation

            # Run generator function for on each process with args
            pool.apply_async(generator, args=(first_char, wordtail_length, length),
                             callback=count_completed)


if __name__ == "__main__":

    print("\nCores on machine to be used:", mp.cpu_count())

    cores_used = None # defaults to all available cores
    charset = int(sys.argv[1])
    maxlength = int(sys.argv[2])

    total_completed = 0

    if charset == 1:
        charset = "0123456789"
    elif charset == 2:
        charset = "0123456789abcdefghijklmnopqrstuvwxyx"
    elif charset == 3:
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx"
    elif charset == 4:
        charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx"
    elif charset == 5:
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    elif charset == 6:
        charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    else:
        print("Please choose and integer between 1 and 6")
        quit()

    print("Character set chosen:", charset)
    print("...Working....\n")

    start = time.time()

    # Multiprocessing setup here
    pool = mp.Pool(cores_used)
    bruteforce(pool)
    pool.close()
    pool.join()

    # Add the size of each charset^i, where each i is 1 through maxlength
    total_possibility_size = sum(len(charset)**i
                   for i in range(1, maxlength + 1))

    # Check that the number of words generated match the expected total number of all possibilities
    assert total_completed == total_possibility_size, (total_completed, total_possibility_size)


    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time), "\n")
