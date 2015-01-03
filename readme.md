# Description
A Markov sentence generator written in Python for a final project (Algorithms, University of Akron, 2014).

It takes one or more input files, picks a prefix to kick off the generated sentence(s), and outputs the sentence(s).

I haven't worked on this code since submitting it for grading. Feel free to use as you please. Pull requests welcome. 

Tested with Python 2.7.6. Python 3 or higher may not run do to the use of raw_input() function, but I haven't tested that.

# Operation
Run from command line as shown below.

### Example
> $ **markov.py** *path/To/TextFile* [*path/To/AnotherTextFile*]...

 **or**

> $ **markov.py** * 

# Parameters
* Any number of input text files can be used.
* Any parameters are assumed to point to text files unless an asterisk is used.
* An asterisk as the only parameter will prompt for a custom seed, prefix length, and number of sentences. 
