# Crackerjack: Multiproccessing brute-force script
# Info: https://github.com/jakekemple/Crackerjack

import sys
import random
import time
import multiprocessing as mp
import functools
import itertools

# Basic bruteforce algorithm. Tests combination possibilities
# of characters in charset
def bruteforce(charset, maxlength):
    return (
        list(''.join(candidate)
            for candidate in itertools.chain.from_iterable(
            itertools.product(charset, repeat=i)
                for i in range(1, maxlength + 1)
            )
        )
    )

def main(results, partial_charset):
    results = bruteforce(partial_charset, maxlength)
    return results

if __name__ == "__main__":
    print("")
    print("Cores on machine to be used:", mp.cpu_count())

    cores_used = mp.cpu_count()
    charset = str(sys.argv[1])
    maxlength = int(sys.argv[2])

    start = time.time()

    charset_final = []
    results = []
    partial_func = functools.partial(main, results)

    print("character set entered: ", charset)

    # This code block creates partial_charsets from charset to be used in each process
    chunk_size = len(charset)//cores_used
    print("Chunk Size: ", chunk_size)
    if len(charset) % cores_used: chunk_size += 1
    iterator = iter(charset)
    for _ in range(cores_used):
        charset_slice = list()
        for _ in range(chunk_size):
            try: charset_slice.append(next(iterator))
            except StopIteration: break
        charset_slice = ''.join(charset_slice)
        charset_final.append(charset_slice)
    charset_list = charset_final

    # Creates list of partial_charsets to be iterated over by p.map
    partial_charsets = []
    for i in charset_list:
        partial_charsets.append(i)

    print("List of partial character sets to be used for possibilities list: ", partial_charsets)

    # Multiprocessing setup here
    p = mp.Pool(cores_used)
    results = p.map(partial_func, partial_charsets)
    results = list(itertools.chain.from_iterable(results))

    #print(results)
    print("Final List: ", results)

    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time))
