from multiprocessing import Pool

import threading

word_lengths = []
words_list = ["Hallo", "ich3", "bin", "Sean"]


def calc_word_length(word):
    return len(word)


def parallel_words_with_multiprocessing_lol(words):
    with Pool() as pool:
        word_lengths_processing = pool.map(calc_word_length, words)
    return word_lengths_processing


def calculate_word_length(words, start_index, end_index, results):
    for i in range(start_index, end_index):
        results[i] = calc_word_length(words[i])


def parallel_words(words, num_threads):
    n = len(words)
    chunk_size = n // num_threads
    threads = []
    results = [[0] for i in range(num_threads)]

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size
        threads.append(threading.Thread(target=calculate_word_length, args=(words, start, end, results)))
        threads[i].start()

    for thread in threads:
        thread.join()

    word_lengths = []
    for i, result in enumerate(results):
        if i * chunk_size < n:
            word_lengths.append(result)

    return word_lengths


# call
if __name__ == '__main__':
    num_threads = 4
    results = parallel_words(words_list, num_threads)
    print(results)
