#!/usr/bin/python

# pwPermutator
# Takes a list of passwords from the input file
# then permutates upper/lowercase for all entries.
#
# e.g. abcd becomes abcd, abcD, abCd, abCD, aBcd, aBcD, aBCd, aBCD
# and so forth

# We do this by applying a bit mask over all the alphabetic fields and
# just adding up. entries under the mask get 32 removed from the ascii
# value, which makes them uppercase thanks to the ASCII chart. 

# Take all entries from the input file. default them all to lowercase
# also fuck whitespace

def permutateUppercase(inputString, bitmask):
    outputString = ""
    bitpos = 0
    for c in inputString:
        if c.isalpha():
            if (bitmask[bitpos] == "0"):
                outputString += c
            else:
                outputString += chr(ord(c)-32)
            bitpos=bitpos+1
        else:
            outputString += c

            
    return outputString

fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
    
content = [x.strip().lower() for x in content]

for raw in content:
    numberOfAlphabeticCharacters = len([c for c in raw if c.isalpha()])    
    
    print "Working on "+raw+". Expecting "+str(2**numberOfAlphabeticCharacters)+" permutations"

    for i in range(0, 2**numberOfAlphabeticCharacters):
        bitmask = format(i, "0"+str(numberOfAlphabeticCharacters)+"b")
        print permutateUppercase(raw, bitmask)

