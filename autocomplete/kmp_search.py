# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'


def kmp_substring_search(haystack, pattern, max_results=None):
    "Find all positions of `pattern` in the given large string `haystack`"
    partial_match_table = create_partial_match_table(pattern)

    pattern_len = len(pattern)
    match_positions = []
    pattern_counter = 0
    for i, char in enumerate(haystack):
        # print haystack[i], pattern[pattern_counter], i, pattern_counter

        if char == pattern[pattern_counter]:
            pattern_counter += 1
            if pattern_counter == pattern_len:
                # match found
                match_positions.append(i - pattern_len + 1)

                if max_results and len(match_positions) == max_results:
                    break

                pattern_counter = 0

        elif pattern_counter > 0:
            partial_match_length = pattern_counter
            # partial_match_length - partial_match_table[partial_match_length - 1]
            pattern_counter = partial_match_table[partial_match_length - 1]


    return match_positions


def create_partial_match_table(pattern):
    "Create partial match table according to KMP Algorithm"
    partial_match_table = []
    for i in range(len(pattern)):
        substring = pattern[:i + 1]
        proper_prefixes = get_proper_prefixes(substring)
        proper_suffixes_set = set(get_proper_suffixes(substring))

        largest_prefix_len = 0
        for prefix in proper_prefixes:
            if prefix in proper_suffixes_set and len(prefix) > largest_prefix_len:
                largest_prefix_len = len(prefix)

        partial_match_table.append(largest_prefix_len)

    return partial_match_table


def get_proper_prefixes(substring):
    "Get all proper prefixes of a given string"
    return [substring[:j] for j in range(len(substring))]


def get_proper_suffixes(substring):
    "Get all proper suffix of given string"
    return [substring[j + 1:] for j in range(len(substring))]



