# Crackerjack: Multiproccessing brute-force script
# Info: https://github.com/jakekemple/Crackerjack

import sys
import random
import time
import multiprocessing as mp
import functools
import itertools



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

    #print("Total simulations to do:", num_simulations, "/n")
    #leftover = num_simulations % cores_used
    #num_simulations = num_simulations // cores_used

    #print("The cores will each do", num_simulations, "simulation, and")
    #last_core_simulations = leftover + num_simulations
    #print("the last core will do", last_core_simulations, "simulations")


    results = []
    partial_func = functools.partial(main, results)

    charset_final = []

    print("character set entered: ", charset)

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


    partial_charsets = []
    for i in charset_list:
        partial_charsets.append(i)

    print("List of partial character sets to be used for possibilities list: ", partial_charsets)

    p = mp.Pool(cores_used)
    results = p.map(partial_func, partial_charsets)
    results = list(itertools.chain.from_iterable(results))

    #print(results)
    print("Final List: ", results)

    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time))
