# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import os, collections, io, csv, operator
from . import levenshtein_spellcheck

SolutionTuple = collections.namedtuple("Solution", ["word", "freq", "is_begin", "exact_match", "inverse_len"])

parent_dir = os.path.dirname(os.path.abspath(__file__))

WORD_FREQ_FILENAME = "word_search.tsv"
WORD_FREQ_FILEPATH = os.path.join(parent_dir, WORD_FREQ_FILENAME)

class Autocomplete(object):
    def __init__(self, word_freq_filepath=WORD_FREQ_FILEPATH):
        """
        Will combine the words by a separator into a very long string;
        Will then search for the given pattern in the combined string
        And, then compute the words using the positions and separator
        (Can't use Trie data structure, because pattern can occur anywhere in the string)

        :param word_freq_filepath:
        """
        self.word_freq_filepath = word_freq_filepath

        self.word_freqs = self.get_word_freq(word_freq_filepath)

        self.separator = "$"

        all_words = self.word_freqs.keys()
        self.all_words_joined = self.separator.join(all_words) + self.separator


    def get_word_freq(self, word_freq_filename):
        """
        :return: A dict of word freqs word-> freq
        """
        with io.open(word_freq_filename, encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=b"\t")
            word_freqs = dict(list(reader))
            word_freqs = {word: int(count) for word, count in word_freqs.items()}
            word_freqs = collections.Counter(word_freqs)

        return word_freqs

    def find_matching_words(self, pattern):
        "Finding words from the dataset which contain the given `pattern`"
        words_found = []
        for pos in native_substring_search(self.all_words_joined, pattern):
            # Finding the word boundaries

            # Finding the index of the end of the word
            end_counter = 1
            while self.all_words_joined[pos + end_counter] != self.separator:
                end_counter += 1

            end_index = pos + end_counter

            # Finding the beginning of the word
            if pos != 0:
                start_counter = 1
                while self.all_words_joined[pos - start_counter] != self.separator:
                    start_counter += 1

                start_index = pos - start_counter + 1
            else:
                start_index = 0

            words_found.append(self.all_words_joined[start_index:end_index])

        return words_found

    def find_autocomplete_answers(self, query, max_results=10):
        "Ranking words in the following order (exact_match, begins_with, inverse_length_of_word, word_freq)"
        words_found = self.find_matching_words(query)  # Finding all words before sorting

        if not words_found:
            # Using spellcheck to find an alternate version of given word
            query = levenshtein_spellcheck.spellcheck(self.word_freqs, query)
            words_found = self.find_matching_words(query)

        solution_freq_tuples = []
        for word in words_found:
            freq = self.word_freqs[word]
            is_begin = word.startswith(query)
            exact_match = word == query
            solution_freq_tuples.append(SolutionTuple(word, freq, is_begin, exact_match, 1.0 / len(word)))

        # print(solution_freq_tuples)
        solution_freq_tuples.sort(key=operator.itemgetter(3, 2, 4, 1), reverse=True)

        return [row.word for row in solution_freq_tuples[:max_results]]



def native_substring_search(haystack, needle):
    start = 0
    positions = []
    while True:
        pos = haystack.find(needle, start)
        if pos == -1:
            break

        positions.append(pos)
        start = pos + len(needle)

    return positions








