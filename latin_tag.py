from os import system #Needed to run bash commands.
from subprocess import check_output #Needed to run bash commands.
from sys import argv #Needed for command-line arguments.

# This file is organized with the more important functions
# first for ease of comprehension.

# DEPENDENCIES:
# - bash
# - Whitacker's Words (a Latin dictionary and parser):
# https://github.com/mk270/whitakers-words


def main():
    # The main function loops thru all command-line
    # arguments and tags each one with the tagFile()
    # function.
    # If no argugment is given, returns only message.
    if len(argv) < 2:
        print("Please give file[s] for tagging as command-line argument.")
    else:
        for x in argv[1:]:
            tagFile(x)
            print("File \"",x,"\" sucessfully tagged.",sep="")

def tagFile(file):
    # This is the main command
    output=""
    inp=""

    #Read the given file into `inp`.
    with open(file) as x: inp+=x.read()

    # Split input text into words.
    inp=inp.split()

    #For every word:
    for x in inp:
        # Run it through `words`, which will return
        # the possible parts of speech to be assigned
        # to pos (part of speech).
        pos=wordIt(x)
        # Each word goes onto the output...
        output=output+x+"//"+pos
        # And if there's sentence final punctuation at
        # the end, we add a newline, else just a space.
        if x[-1] in punc:
            output=output+"\n"
        else:
            output=output+" "
    # Finally, we write our compiled output to a file
    # named whatever the name of the original file was
    # with '.tagged' appended to the end to prevent
    # overwriting.
    writeFile(file+".tagged",output)

def wordIt(word):
    # wordIt() is where the magic happens.
    # Give this function a word, and it will
    # process it with the bash command `words`,
    # which is typically a Latin dictionary
    # program and parser.
    # This command runs the word in `words`, but
    # Selects greps and awks out only the possible
    # parts of speech.
    bashcomm="echo | words %s | grep -v \; | grep -v \] | grep -v ENTER | awk '{print $2}' | sort -u" % word
    pos=check_output(['bash','-c', bashcomm])
    # Decoding the bash output into a proper Python
    # string.
    pos=pos.decode("utf-8")
    # Use subbing() to replace to get the tags I want.
    pos=subbing(pos)
    return pos

def writeFile(file, output):
    # Takes a file and output.
    # Writes the output to the
    # file.
    with open(file,'w') as new:
        new.write(output)

# For ease of use, I want parts of speech to be stored
# as single letters, not the sequences that `words`
# yields by default.
# The var `subs` is a dic of tuples for replacing the
# first with the second.
# E.g. the sequence ADV which `words` uses is replaced
# with simply D, etc.
subs={('\n',''),
            ('ADJ','A'),
            ('CONJ','C'),
            ('ADV','D'),
            ('PRON','O'),
            ('INTERJ','I'),
            ('NUM','M'),
            ('PREP','P'),
            ('VPAR','R'),
            ('SUFFIX','S')
            }

# This is the command that will actually replace all
# the proper substitutes. I used the `replace` method
# rather than having to load the re package.
def subbing(x):
    for tup in subs: x=x.replace(tup[0],tup[1])
    return x

# End of sentence markers.
punc=".!?"

main()
