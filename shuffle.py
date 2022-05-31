
# quality of the shuffle depends on the quality of PRNG which in random.randint case in Mersenne \
# Twister(most tested and used) PRNG. 

# numpy also has random shuffle function that used a different PRNG called Permuted Congruential 
# generator or PCG.

# use numpySuffle() which provides more statistical variance.

"""
# Shuffling methods.
# Primary way to shuffle uses Fisher-Yates algorithm.
# random module provids 2 methods to shuffle a list of values.
# Note : random.shuffle does not work on str type 
# Fisher-Yates is the more effecient shuffling algorithm and is the working bases for randon.shuffle()

"""

# Fisher-Yates method of random permutations :: 



def FisherYates(List: list)-> None:
    """
    This function does an in-place shuffle 
    i.e. no new list is created. 
    """
    from random import randint

    for i in range(len(List)-1,0,-1):
        j = randint(0,i+1) 
        List[i],List[j] = List[j],List[i]
    

# using Python buil-in random.shuffle (Also Fisher-Yates)

def shuffle(List: list)-> None :
    from random import shuffle
    newList = List
    # shuffles list in place 
    shuffle(newList)

# using random.sample

def SampleShuffle(List: list) -> list:
    """
    This method generates a new list 
    instead of doing an in-place shuffle
    """
    from random import sample
    newList = sample(List,len(List))
    return newList

def naiveShuffle(List: list)-> list:
    """
    Naive shuffling method 

    """
    from random import randint
    for i in range(len(List)):
        index = randint(0,len(List)-1)
        temp  = List.pop(index)
        List.append(temp)
    return List

# shuffling a string since random.shuffle doesn't work on str

def StrShuffle(arg: str)-> str:
    """
    Shuffle a string sequence using 
    Fisher-Yates shuffle
    """
    # remove all the whitespaces and extra 
    # lowercase all the characters
    def filterStr(arg):
        from string import ascii_lowercase
        temp = ""
        for i in arg.lower():
            if i in ascii_lowercase:
                temp += i
        return temp
    # convert the str to list
    StrList = list(filterStr(arg))
    from random import sample
    # convert back from list to str
    newStr = "".join(sample(StrList,len(StrList)))
    return newStr

# using numpy PCG64 (Permuted Congruential generator) instead of MT19937 (Mersenne Twister)
# more accurate than random.shuffle 

def numpyShuffle(List: list)-> None:
    
    try:
       import numpy as np
       rng = np.random.default_rng()
       # shuffle list in place.
       rng.shuffle(List)
    except ModuleNotFoundError:
        print("numpy not installed !")



