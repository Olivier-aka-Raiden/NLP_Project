from __future__ import division
import nltk
from collections import Counter
from nltk import word_tokenize
import re
from nltk.corpus import wordnet as wn

NEGATIVE_WORDS = ['hardly', 'seldom', 'scarcely', 'barely', 'rarely']
NEGATIVE = ['not','n\'t','nothing','nobody','never','no']
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
            
    def isDblNegatives(self,sentence):
        neg = 0
        tokens = word_tokenize(sentence)
        for t in tokens:
            if len(t)>1:
                if t.lower() in NEGATIVE:
                    neg = neg+1
        if neg == 2:
            print("this is a sentence with a double negative.")
            return True
        else:
            return False
    def correctSent1(self,sent):
        sent = word_tokenize(sent)
        new_sent = []
        for word in sent:
            if len(word)>1:
                if word == 'n\'t':
                    word = 'not'
                if word not in NEGATIVE:
                    new_sent.append(word)
            else:
                new_sent.append(word)          
        new_sent = ' '.join(new_sent)
        print (new_sent+"\n")
    def correctSent2(self,sent):
        tokens = word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        new_sent = []
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
