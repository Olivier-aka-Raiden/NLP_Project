from __future__ import division
import nltk
from collections import Counter
from nltk import word_tokenize
import re
from nltk.corpus import wordnet as wn

#/!\Notice : I wrote this program with python 3.4.1 so don't be surprised if print makes errors in your compiler.

#list of words used for first case:
NEGATIVE_WORDS = ['hardly', 'seldom', 'scarcely', 'barely', 'rarely']
#list of words used to spot the negative words in a sentence
NEGATIVE = ['not','n\'t','nothing','nobody','never','no']
#list of words used to change the words in the last case with bad grammar
BAD_GRAMMAR = ['nothing','never','no']

class DblNegatives(object):
    #helper fonctions :
    def change(self,word):
        if word == 'nothing':
            return 'anything'
        elif word == 'never':
            return 'ever'
        elif word == 'no':
            return 'any'
    #check if there is double negative in sentence:
        #can be changed later if we decide to split this function for each case for more efficiency
    def isDblNegatives(self,sentence):
        neg = 0
        tokens = word_tokenize(sentence)
        #check the amount of negative meaning words
        for t in tokens:
            if len(t)>1:
                if t.lower() in NEGATIVE:
                    neg = neg+1
        if neg == 2:
            print("this is a sentence with a double negative.")
            return True
        else:
            return False
    #first case when there is negative word such as Hardly etc.
    def correctSent1(self,sent):
        sent = word_tokenize(sent)
        new_sent = []
        for word in sent:
            if len(word)>1:
                #change n't into not
                if word == 'n\'t':
                    word = 'not'
                #Here we change every negative word into his corresponding good word
                if word not in NEGATIVE:
                    new_sent.append(word)
            else:
                new_sent.append(word)          
        new_sent = ' '.join(new_sent)
        print (new_sent+"\n")
    #TODO : second case
    #third case with bad grammar:
        #this one should be improve in order to get better result but it works for the example sentence
    def correctSent2(self,sent):
        tokens = word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        new_sent = []
        #use tags to spot good words to change
        for (word,tag) in tagged:
            if len(word)>1:
                if word == 'n\'t':
                    word = 'not'
                if tag == 'NN' and word in BAD_GRAMMAR:
                    new_sent.append (self.change(word))
                else:
                    new_sent.append(word)
            else:
                    new_sent.append(word)
        new_sent = ' '.join(new_sent)
        print (new_sent)
def main():
    #To do:
    #change the program to deal with a list of sentences from a .txt file
    #create 3 fonctions one for each situation 1: negative words 2: prefixes 3:bad grammar
    #change the current list of words into dictionary or more suitable data type.

    #this is an idea of what will be the result for one sentence.
    sentence = "We never heard nothing like that."
    sentence2 = "I couldn't hardly wait to get to the party."
    dn = DblNegatives()
    print (sentence2)
    if (dn.isDblNegatives(sentence)):
        print("The modified sentence is : ")
        dn.correctSent1(sentence2)
    else:
        print("Bye")
    
    print(sentence)
    if (dn.isDblNegatives(sentence)):
        print("The modified sentence is : ")
        dn.correctSent2(sentence)
    else:
        print("Bye")

if __name__ == '__main__':
    main()
