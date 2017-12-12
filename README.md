# Corpus Latinum Lucae

This will be tools to create a searchable Latin Corpus built from texts from [theLatinLibrary.com](http://thelatinlibrary.com/).

Right now, I've finished a part-of-speech tagger that uses [Whitacker's Words](https://github.com/mk270/whitakers-words) to tag text documents. This is what [`latin_tag.py`](latin_tag.py) is.

## `latin_tag.py`

The tagger. Feed it a text via command-line argument (or many) and will produce a tagged equivalent in `FILENAME.tagged`.

### Dependencies:
+ [Whitacker's Words](https://github.com/mk270/whitakers-words) 
+ `bash`

### Known bugs

+ Can't handle text with semicolons. Or brackets []. Will fix soon.

## Next on the list:

+ system for generating the tagged corpus
+ way to search the corpus
