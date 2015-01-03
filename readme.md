# Description
A Markov sentence generator written in Python for a final project (Algorithms, University of Akron, 2014).

It takes one or more input files, picks a prefix to kick off the generated sentence(s), and outputs the sentence(s).

I haven't worked on this code since submitting it for grading. Feel free to use as you please. Pull requests welcome. 

Currently it's broken, at least on Python3. Getting an incompatible seed error.

*I hope to change tabs to spaces soon - I didn't know any better at the time.*

# Operation

> $ **markov.py** *path/To/TextFile* [*path/To/AnotherTextFile*]...

 **or**

> $ **markov.py** * 

# Parameters
* Any number of input text files can be used.
* Any parameters are assumed to point to text files unless an asterisk is used.
* An asterisk as the only parameter will prompt for a custom seed, prefix length, and number of sentences. 
