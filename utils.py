from brown import brown_collection

from consts import SN, SN_

MIN_NS = 10**-7

def NS(noun):
    
    """
    Noun sexiness function
    Returns a real value measure of the maximum similarity
    a `noun` not in SN has to each noun in SN_
    """

    # return MIN_NS for nouns that occur less than 200 times
    return brown_collection.tf_idf(noun, SN_)

def AS(adj):

    """
    Adjective sexiness function
    Returns a real value measure of how likely an adjective `adj`
    is to modify a noun in SN
    """

    # implementation should return relative frequency of adj
    # in sentences in erotica corpus that contain at least
    # one noun in SN
    return 0

def VS(verb):

    """
    Verb sexiness function
    Returns a real value measure of how much more likely a verb 
    phrase `verb` is to appear in an erotic context than a
    nonerotic one
    """

    # let S_E be the set of sentences in the erotica corpus
    # that contain nouns in SN. let S_B be the set of all
    # sentences in the Brown corpus. given sentences s with
    # verb v
    return 0