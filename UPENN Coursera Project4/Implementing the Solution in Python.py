# class Entry:
# def __init__(self, input_word, input_synonyms):
# self.word = input_word
# self.synonyms = input_synonyms

e1 = Entry("happy", ["cheerful", "blissful", "trial"])
e2 = Entry("sad", ["depressed", "down"])
e3 = Entry("angry", ["mad", "emotional"])
Thesaurus = [e1, e2, e3]

doc1 = ["here", "sad", "happy", "document", "angry"]
doc2 = ["I", "mad", "sad", "angry", "cheerful", "trial", "happy"]
Corpus = [doc1, doc2]

All_words = []


# print(Corpus)
# print(e1.word, e1.synonyms)
def search(keyword):
    thesaurus_search(keyword)
    # print(All_words)

    return doc_search(All_words)


def thesaurus_search(string):
    # This first part will search for our keyword in the Thesaurus
    for entry in Thesaurus:
        if entry.word == string:
            # print("Match found in Thesaurus!")
            All_words.append(string)

            for synonym in entry.synonyms:
                All_words.append(synonym)


def doc_search(All_words):
    test = []

    for my_word in All_words:
        count = 0
        for document in Corpus:
            for doc_word in document:
                if my_word == doc_word:
                    # print("The word is " + my_word)
                    count = count + 1
        mytuple = (my_word, count)
        test.append(mytuple)
    # print(test)
    print(type(test))
    print(type(test[0]))
    return test

    # return # modify to return a list of tuples


input = "happy"
output = search(input)  # invoke the method using a test input
print(output)  # prints the output of the function
# do not remove this line!
