#!/usr/bin/python

#Tyler Wengerd
#Final Project - text generation with Markov chain algorithm
#Algorithms
#University of Akron
#4/25/2014

#Tested and working on ArchLinux with Python 3.4.2 using "python ./markov.py"

import sys # for passing input args
import os # for getting file size
import random # for choosing random element from dict entry
import string # for string.lower()
import time

''' global variables '''
prefixDict = {} # this is our precious

# exclusions
honorifics = ["mr.", "mrs.", "dr.", "ms.", "rev.", "fr.",
                "atty.", "prof.", "pres.", "gov.", "sr.", "mgr.", 
                "cpl.", "sgt.", "capt.", "lt.", "col.", "gen.",
                "'mr.", "'mrs.", "'dr.", "'ms.", "'rev.", "'fr.",
                "'atty.", "'prof.", "'pres.", "'gov.", "'sr.", "'mgr.", 
                "'cpl.", "'sgt.", "'capt.", "'lt.", "'col.", "'gen.",
                '"mr.', '"mrs.', '"dr.', '"ms.', '"rev.', '"fr.',
                '"atty.', '"prof.', '"pres.', '"gov.', '"sr.', '"mgr.', 
                '"cpl.', '"sgt.', '"capt.', '"lt.', '"col.', '"gen.']
                
quoteEndings = [".'", "!'", "?'", '."', '?"', '!"']
sentenceEndings = [".", "!", "?"]



''' being file processing '''
def processFiles(fnames):
    fileCounter = 0 # number of files we will be parsing - they all get added to the precious
    for filename in fnames:
        fileCounter = fileCounter + 1
        print("Processing file " + str(fileCounter) + "/" + str(len(fnames)) + "...")
        
        fullText = [] # tracking lines in this file

        f = open(filename, 'r') # f's our file

        # create 1d array of words: fullText
        for line in f:
            #print str( int( float(lineCount)/estLineCount * 100 ) ) + "% complete"
            fullText.extend(line.split()) # splits words by whitespace into a list, extends that list as a part of fullText
            # now we have a list of words

        for i in range(len(fullText)-prefLen):
            prefix = ' '.join(fullText[i:i+prefLen]) # combine the prefLen words, separated by spaces
            if prefix in prefixDict:
                prefixDict[prefix].append(fullText[i + prefLen]) # append next word to entry in dictionary - duplicates will be duplicated, making random choice automatically weighted
            else:
                prefixDict[prefix] = [fullText[i + prefLen]]# create entry in dictionary (must initialize it was a list
        # for entry in prefixDict: # debug
            #print entry + " >>> " + str(prefixDict[entry]) # debug
        print("done with file: " + filename)
        f.close()

''' picking seed '''
def pickSeed():
    pSeed = random.choice(list(prefixDict.keys())) # initial seed

    while "." in pSeed or '."' in pSeed: # if we have a period in seed originally it throws off sentence count - just a nitpick
        pSeed = random.choice(list(prefixDict.keys())) # choose different seed

    return pSeed


'''text generation '''
def makeMarkov(mSeed):
    sentenceList = mSeed.split() # initial sentence setup
    countSentences = -1 # allow a init sentence from random seed

    while numSentences > countSentences:
        '''
        Gets last prefLen words of current sentence
        and looks them up in prefix dictionary, which returns list of possible following words.
        chooses a random entry from the list of possible following words
        and appends that choice to the current sentence
        and repeats! We're on our way.
        We have to do the ' '.join (which joins elements, placing a space in between)
        because the dictionary sees it as a single string (it can't hash lists)
        but we have to use a list for sentenceList so we can index words and append correctly.
        '''
        sentenceList.append(random.choice(prefixDict[' '.join(sentenceList[-prefLen:])])) 
        
        lastWord = sentenceList[-1]
        # if the current last word ends with a proper sentence ending and it's not part of an honorific
        if lastWord.lower not in honorifics and (lastWord[-1] in sentenceEndings or lastWord[-2:] in quoteEndings):
            countSentences += 1    

    madeMarkov = ' '.join(sentenceList) # sentence separated by spaces
    return madeMarkov

''' output cleanup '''
def textCleanup(markovIn, custom):
    output = markovIn # to being with

    output = output.split() # remove whitespace at beginning and end
    output = ' '.join(output)
    
    if custom == 0:
        # removing first sentence
        delIndex = -1
        for ending in sentenceEndings:
            tempDel = output.find(ending) # get index of first ending punctuation mark
            if tempDel > delIndex and tempDel != len(output)-1: # it's lower than the last one we found, and it exists
                delIndex = tempDel

        if output[delIndex:] in quoteEndings: # There's a " or ' after it, meaning it's the end of a sentence in quotations
            delIndex += 1 # let's remove the endquote too

        if delIndex != len(output)-1: # if it's the last part we can keep the sentence
            output = output[delIndex+1:] # removes (everything before index delIndex) + (char at delIndex) + (space afterwards) and keeps everything after

        # first sentence removed
    
    # quotation mark detection - we're giving up on single quotes - too much of a hassle with possessives and conjunctions
    oddDQ = output.count('"') % 2 != 0 # are there an odd number of double quotes
            
    if oddDQ == 1:
        if output[-1] == '"': # last char is "
            output = '"' + output # add to beginning
        else:
            output = output + '"' # add to ending
            
    # quotation marks should be ok now

    # final cleanup
    output = output.split() # one more time
    output[0] = output[0].title() # capitalize first alpha character
    output = ' '.join(output) # done!

    return output
    
    
''' Main operation '''
cmdIndex = 1
customSeed = 0
listOut = ""

if sys.argv[1] == "CUSTOM": # custom specified
    uSeed = input("Seed: ")
    numSentences = input("Number of sentences: ")
    prefLen = input("Prefix length (higher is more accurate to the text): ") # second last is the prefix length
    listOut = input("Print dictionary? ")
    
    try:
        uSeed = str(uSeed)
    except:
        uSeed = ""
    
    try: 
        numSentences = int(numSentences)
    except:
        numSentences = 1
        
    try:
        prefLen = int(prefLen)
    except:
        if uSeed != "":
            prefLen = len(uSeed.split()) # automatically choose prefix length based on seed length
        else:
            prefLen = 2
    cmdIndex += 1
    
else: # we use defaults
    numSentences = 1 # defaults to 1 sentence
    prefLen = 2 # prefix length defaults to 2
    uSeed = "" # no user seed

    
beginTime = time.time()

filenames = sys.argv[cmdIndex:] # get the filenames

processFiles(filenames)
if uSeed != "":
    seed = uSeed
    customSeed = 1
else:
    seed = pickSeed()
    
if prefLen != len(seed.split()): # prefix length doesn't match size of seed
    print("Error: Number of words in seed must be equal to prefix length.")
    exit()
    
try:
    markovOut = makeMarkov(seed)
except:
    print('Error: Incompatible seed ("' + seed + '" not found in dictionary).')
    exit()
finalOut = textCleanup(markovOut, customSeed)

if listOut == "y":
    fDict = open("dict.txt", 'w')
    fDict.write(str(prefixDict))
    fDict.close()
print(finalOut)
print("Time: " + str(time.time() - beginTime) + " seconds")
