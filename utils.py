from brown import brown_collection
from consts import SN, SN_

def NS(noun):
    """Noun sexiness function
    Returns a real value measure of the maximum similarity a noun `n not in SN`
    has to each of the `nouns in SN_`
    """
    # return 10**-7 for nouns that occur less than 200 times
    return brown_collection.tf_idf(noun, SN_)
