import random
from urllib.request import urlopen
import sys

# set the link to WORD_URL variable
WORD_URL = "http://learncodethehardway.org/words.txt"
# create an empty list name WORDS
WORDS = []
# creat a dictionary name PHRASE
PHRASE = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** parameter",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ parameters",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self.",
    "****.**** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # print(">>>>>>", repr(WORDS))

# define a function that take 2 params snippet and phrase
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in # pick each word from the list and capitalizes it
                    random.sample(WORDS, snippet.count("%%%"))] # create a random list of words in WORDS, lenght = number of %%% that counted in a snippet
    print(">>>> ", snippet.count("%%%"))
    other_names = random.sample(WORDS, snippet.count("***")) # create a random list of words in WORDS, length = number of *** that counted in a snippet
    results = [] # create an empty list name result
    param_names = [] # create an empty list name param

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class name
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# kepp going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASE.keys())
        print(">>>>> ", repr(snippets))
        random.shuffle(snippets)
        print("<<<<<", repr(random.shuffle(snippets)))
        for snippet in snippets:
            phrase = PHRASE[snippet]
            print(">>>>", repr(PHRASE[snippet]))
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")
