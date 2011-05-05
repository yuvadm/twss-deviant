from brown import brown_collection
from consts import SN, SN_

def NS(noun):
    """Noun sexiness function
    Returns a real value measure of the maximum similarity
    a `noun` not in SN has to each noun in SN_
    """
    # return 10**-7 for nouns that occur less than 200 times
    return brown_collection.tf_idf(noun, SN_)

def AS(adj):
    """Adjective sexiness function
    Returns a real value measure of how likely an adjective `adj`
    is to modify a noun in SN
    """
    # implementation should return relative frequency of adj
    # in sentences in erotica corpus that contain at least
    # one noun in SN
    return 0

def VS(verb):
    """Verb sexines function
    Returns a real value measure of how much more likely a verb 
    phrase `verb` is to appear in an erotic context than a
    nonerotic one
    """
    return 0