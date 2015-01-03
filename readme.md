# Description
A Markov sentence generator written in Python for a final project (Algorithms, University of Akron, 2014).

It takes one or more input files, picks a prefix to kick off the generated sentence(s), and outputs the sentence(s).

Tested and working with Python 3.4.2 on ArchLinux.

Feel free to use as you please. Pull requests welcome. 

*This is part of an ongoing project to put some of my old school projects on GitHub - the going will be slow, as I have to go through backups and recovered files.*


# Operation

`python ./markov.py path/To/TextFile [path/To/AnotherTextFile]...`

 **or**

`python ./markov.py CUSTOM path/To/TextFile [path/To/AnotherTextFile]...`

# Parameters
* Any number of input text files can be used.
* Placing the word "CUSTOM" before any file paths will prompt for a custom seed, prefix length, and number of sentences.
  * All prompt imputs are optional - simply pressing `Enter` at the prompt will use the default value.
