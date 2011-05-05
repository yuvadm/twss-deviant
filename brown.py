from nltk.corpus import brown
from nltk.text import TextCollection

# the default initialization for a corpus fails
# since files() was changed to fileids()
# anyway, brown_collection = TextCollection(brown) doesn't work
# so we use this workaround
words = [brown.words(f) for f in brown.fileids()]
brown_collection = TextCollection(words)
