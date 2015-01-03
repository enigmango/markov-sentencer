# Description
A Markov sentence generator written in Python for a final project (Algorithms, University of Akron, 2014).

It takes one or more input files, picks a prefix to kick off the generated sentence(s), and outputs the sentence(s).

I haven't worked on this code since submitting it for grading. Feel free to use as you please. Pull requests welcome. 

Tested and working with Python 3.4.2 on ArchLinux.

# Operation

> $ python markov.py *path/To/TextFile* [*path/To/AnotherTextFile*]...

 **or**

> $ python markov.py CUSTOM *path/To/TextFile* [*path/To/AnotherTextFile*]...

# Parameters
* Any number of input text files can be used.
* Any parameters are assumed to point to text files unless an asterisk is used.
* Placing the word "CUSTOM" before any file parameters will prompt for a custom seed, prefix length, and number of sentences.
  * Anything prompted for is optional - simply pressing `Enter` at the prompt will use the default value.
