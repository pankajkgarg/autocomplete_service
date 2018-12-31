# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import string

alphabet = string.lowercase

def spellcheck(word_freqs, word):
    "Will find the most frequent word which is nearest to the given `word` and is present in the dictionary"
    
    candidates = (known(word_freqs, edits0(word)) or 
                  known(word_freqs, edits1(word)) or
                  known(word_freqs, edits2(word)) )
    
    return max(candidates, key=word_freqs.get)


def edits1(word):
    "Returns all words which are 1 distance away from given word"
    splits = word_splits(word)
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for (a, b) in splits if len(b) > 1]
    replaces = [a + c + b[1:] for (a, b) in splits for c in alphabet if b]
    inserts = [a + c + b for (a, b) in splits for c in alphabet]

    return set(deletes + transposes + replaces + inserts)


def word_splits(word):
    "Returning all possible ways of splitting a word in two parts"
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]


def known(word_freqs, words):
    "Return the subset of words that are actually in the dictionary."
    return {w for w in words if w in word_freqs}

def edits0(word): 
    "Return all strings that are zero edits away from word (i.e., just word itself)."
    return {word}

def edits2(word):
    "Return all strings that are two edits away from this word."
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}
