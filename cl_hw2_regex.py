
import re
import collections


gutenbergWords = gutenberg.words()[:100000] # first 100000 words of Gutenberg
shakespeareRawText = shakespeare.raw()[:20000] # first 20000 characters of shak$

def applyRegEx(compiledRegEx):
    """Looks for all matches for the given regular expression and returns
    them sorted in a string"""
    resultSet = set()
    for word in gutenbergWords:
        matching = compiledRegEx.match(word)
        if matching:
            resultSet.add(word)
    sortList = list(resultSet) # transforms the Set into a List
    sortList.sort()
    return ', '.join(sortList)

# EXCERCISE 3 Part 1
regex0 = r'^word$'
regex1 = r'^e.{4}ing$'
regex2 = r'^w.[^aeiou]$'
regex3 = r'^[aeod]{2,}$'
regex4 = r'^[Aa].*[Aa].*[Aa].*$'

print('Matches for the regular expressions 0-4:')
i=0
for regex in (regex0, regex1, regex2, regex3, regex4):
    compiledRegEx = re.compile(regex)
    print('regex',i,':', applyRegEx(compiledRegEx))
    i+=1

# EXCERCISE 3 Part 2
# - - - - - - - - - - - - - - - - - - - -

print('\nResult for your regular expression 5:')

regex5 = r'^<SPEAKER>CLEOPATRA</SPEAKER>$'

def count_speaker(regex5):
    #shakespeareRawText = open('shakespeare.txt','r')
    with open('shakespeare.txt', 'r') as myfile:
        shakespeareRawText = myfile.read()
        speaker_list = []
        speaker_list = re.findall(regex5,str(shakespeareRawText))
        print(speaker_list)
        speaker_counter = {x:speaker_list.count for x in speaker_list}
        print(speaker_counter)

count_speaker(regex5)
