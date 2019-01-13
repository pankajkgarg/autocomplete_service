Autocomplete server
Refer to problem_statement.pdf for details on the assignment.

Usage:  export FLASK_APP=autocomplete/server.py; flask run


A running version of the app is available at http://developermuse.com/search?word=play



Challenges:
The assignment purpose is to develop an Autocomplete service with a given pool of approx 300,000 words. 


In a usual autocomplete service, the word can match from the begining only, but here the task is made trickier by the fact that the query can match words in the middle as well. This rules out the application of Trie data structure to solve the problem.

Solutions explored:
Ukkonen algorithm, KMP algorithm

Solution:
To enable searching anywhere in the middle, we join all words with a separator e.g. '$', and then search for all locations of query in the combined string. We know that word boundaries can be found using our separator, using this information and locations, we can find all words which contain the given query.

KMP algorithm was implemented for substring search.

But a native Python solution is not fast enough for the problem and Python native string search capabilities were used. 


