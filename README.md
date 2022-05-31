# Shuffling Algorithms using Python 3 (The Fisher-Yates Algorithm)
-----------------------------------

## About the Algorithm
   __Shuffling__ is a method used to randomize an ordered collection of objects, that can anything from cards to digits and characters. Among many methods the most effecient method of shuffling anorderd collection of objects is the [Fisher-Yates shuffle](https://wikipedia.org/wiki/Fisher-Yates_shuffle). __Fisher-Yates shuffle__ was popularized by __Donald Knuth__ which is a simple algorithm using radomized permutation with the __O(n)__ time complexity. Fisher-Yates algorithm is an in-place shuffling algorithm.

   __Note :__ A very important thing to note is that like all the other randomized algorithms whose correctness and effeciency depends on the type of Pseudo random number generator this is the same for Fisher-Yates as well. 
   
   Python's random module contains __random.shuffle__ method that uses the Fisher-Yates algorithm and Mersanne Twister PRNG for pseudo random number generation. __numpy__ also has an in-place shuffling method that works faster and is more accurate since it uses different pseudo random number generator called PCG64 Family of PRNG. More about the PRNG used by numpy by default can be found at [Random Generator module](https://numpy.org/doc/stable/reference/random/generator.html).

   The bias in random permutation will depend upon a few things 
   - implementation error
   - or the use of PRNG with less statistical variance