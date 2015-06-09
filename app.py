from __future__ import division
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from sys import version_info
import nltk, re, pprint

#/!\Notice : Program written with python 3.4.1; print may have errors

#list of words for double negatives using negative words
NEGATIVE_WORDS = set(['hardly', 'seldom', 'scarcely', 'barely', 'rarely'])
#list of common negative words
## NOTE: Can change this to a lookup table... didn't --> did and n't (or not)
NEGATIVE = set(['not','n\'t','nothing','nobody','never','no'])
#list of words for double negatives using prefixes
NEGATIVE_PREFIXES = set()
#list of words for double negatives using bad grammar
BAD_GRAMMAR = set(['nothing','never','no','ai','not'])

# populate the negative prefixes set
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
for w in [w for w in wordlist if re.search('^(in|un|im|non|ir).+', w)]:
    NEGATIVE_PREFIXES.add(w)

class DblNegatives(object):
    def __init__(self):
        pass

    # check if the sentence contains a double negative
    def contains_double_negative(self, sentence):
        neg_count = 0
        tokens = word_tokenize(sentence)
        # check the number of negative meaning words
        for t in tokens:
            if (t.lower() in NEGATIVE) or (t.lower() in NEGATIVE_WORDS) or (t.lower() in NEGATIVE_PREFIXES):
                #print ('FOUND A NEGATIVE WORD, IT WAS:', t)
                neg_count += 1
        if neg_count > 1 and neg_count % 2 == 0:
            print("This is a sentence with a double negative.")
            return True
        else:
            return False

    # check if it is a double negative sentence using negative words
    def is_negative_word_sentence(self, sent):
        sent = word_tokenize(sent)
        for word in sent:
            if word.lower() in NEGATIVE_WORDS:
                print ('This sentence is a negative word sentence.')
                return True
        return False

    # correct the double negative sentence using negative words
    def correct_negative_word_sentence(self, sent):
        sent = word_tokenize(sent)
        new_sent = []
        for word in sent:
            if len(word)>1:
                #change n't into not
                if word == 'wo':
                    word == 'will'
                if word == 'ca':
                    word = 'can'
                if word == 'n\'t':
                    word = 'not'
                #Here we change every negative word into his corresponding good word
                if word not in NEGATIVE:
                    new_sent.append(word)
            else:
                new_sent.append(word)
        new_sent = ' '.join(new_sent)
        print (new_sent+"\n")

    # check if it is a double negative sentence using negative prefixes
    def is_negative_prefix_sentence(self, sent):
        sent = word_tokenize(sent)
        for word in sent:
            if word.lower() in NEGATIVE_PREFIXES:
                print ('This sentence is a negative prefix sentence.')
                return True
        return False

    # correct the double negative sentence using negative prefixes
    def correct_negative_prefix_sentence(self, sent):
        sent = word_tokenize(sent)
        new_sent = []
        for word in sent:
            pass
        #print (new_sent+"\n")


    # check if it is a double negative sentence using bad grammar
    def is_bad_grammar_sentence(self, sent):
        sent = word_tokenize(sent)
        for word in sent:
            if word.lower() in BAD_GRAMMAR:
                print ('This sentence is a bad grammar sentence.')
                return True
        return False

    # helper function to correct words in the bad grammar sentences
    def change_bad_grammar(self, word):
        if word == 'nothing':
            return 'anything'
        elif word == 'never':
            return 'ever'
        elif word == 'no':
            return 'any'
        elif word == 'not':
            return ''

    # correct the double negative sentence using bad grammar
    def correct_bad_grammar_sentence(self, sent):
        tokens = word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        modification = 0
        new_sent = []
        #use tags to spot good words to change
        for (word,tag) in tagged:
            if len(word)>1:
                if word == 'wo':
                    word = 'will'
                if word == 'ai':
                    word = 'don\'t'
                if word == 'ca':
                    word = 'can'
                if word == 'n\'t':
                    word = 'not'
                if (tag == 'NN' or tag == 'DT' or tag == 'RB') and (word in BAD_GRAMMAR) and modification == 0:
                    new_sent.append (self.change_bad_grammar(word))
                    modification = 1
                else:
                    new_sent.append(word)
            else:
                    new_sent.append(word)
        new_sent = ' '.join(new_sent)
        print (new_sent+"\n")

    # processes a sentence and checks if it has a double negative
    # if so, corrects the double negative
    def process_sentence(self, sentence):
        print ('The sentence is:', sentence)
        if (self.contains_double_negative(sentence)):
            print("The modified sentence is: ")
            if self.is_negative_word_sentence(sentence):
                self.correct_negative_word_sentence(sentence)
            elif self.is_negative_prefix_sentence(sentence):
                self.correct_negative_prefix_sentence(sentence)
            elif self.is_bad_grammar_sentence(sentence):
                self.correct_bad_grammar_sentence(sentence)
        else:
            print ('This sentence does not contain a double negative.'+"\n")


def main():
    dn = DblNegatives()
    print('*/----------------------------------------------------------------*/')
    print('*/CS372 NLP project: Double negatives')
    print('*/objective: correcting sentences with double negative to make')
    print('*/easier to understand.')
    print('*/----------------------------------------------------------------*/')
          
    # read test sentences from a text file
    sentences = [line.rstrip('\n') for line in open('sentences.txt')]
    for sentence in sentences:
        dn.process_sentence(sentence)

    # take in user input of sentences
    sent = ""
    py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

    while(True):
        if py3:
            sent = input("Enter a sentence (\"quit\" to exit the program): ")
            if (sent == "quit"):
                break;
            dn.process_sentence(sent)
        else:
            sent = raw_input("Enter a sentence (\"quit\" to exit the program): ")
            if (sent == "quit"):
                break;
            dn.process_sentence(sent)

if __name__ == '__main__':
    main()
