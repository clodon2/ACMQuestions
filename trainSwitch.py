"""
Author: Corey Verkouteren
Date: 2/25/24
Project: ACM Club onlinejudge.org problem 299
Description: Sorts "train carriages" i.e. a list while only being able to swap
    the places of adjacent "carriages" (elements in the list). Returns swaps
    taken to complete the process.

Functions:
    formatSequence - reformats string of numbers into a list of those numbers
        as integers
    sortList - sorts the list with "bubble sorting" aka the sorting used by
        train swappers

Variables:
    trainLength - given input of number of carriages
    trainSequnce - given input of carriages represented as numbers in a string
        seperated by spaces


"""
trainLength = input()
trainSequence = input()


# reformat string of numbers into list of ints
def formatSequence(seq):
    seq = seq.split() # seperate string into list at spaces
    for i in range(len(seq)): # cast strings in list into ints
        seq[i] = int(seq[i])

    return seq


# sort the list lowest to highest with bubble sorting
def sortList(sList):
    sorting = True
    swapNumber = 0
    unsortedElements = len(sList)
    
    while sorting: # continue until list is sorted
        sorting = False # assume list is sorted unless below
        for i in range(unsortedElements - 1):
            if sList[i + 1] < sList[i]: # swap element positions
                swapNumber += 1 # count swap
                hold = sList[i] # needed as value gets replaced
                sList[i] = sList[i + 1]
                sList[i + 1] = hold
                sorting = True # found unsorted, continue loop
                
        unsortedElements -= 1 # now sure another element is sorted
        
    return swapNumber


trainList = formatSequence(trainSequence) # get usable list

swapNumber = sortList(trainList) # get swap amount

print(f"Optimal train swapping takes {swapNumber} swaps") # prompted return
