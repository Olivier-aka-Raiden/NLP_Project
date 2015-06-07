from __future__ import division
import nltk
from collections import Counter
from nltk import word_tokenize
import re
from nltk.corpus import wordnet as wn
from sys import version_info

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
        # check the number of negative meaning words
        for t in tokens:
            if t.lower() in NEGATIVE or t.lower() in NEGATIVE_WORDS:
                #print 'FOUND A NEGATIVE WORD, IT WAS:', t
                neg = neg + 1
        if neg % 2 == 0:
            print("This is a sentence with a double negative.")
            return True
        else:
            return False

        
    # check for the first case
    def is_negative_word_sentence(self, sent):
        sent = word_tokenize(sent)
        for word in sent:
            if word.lower() in NEGATIVE_WORDS:
                return True
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

    # check for third case
    def is_bad_grammar_sentence(self, sent):
        sent = word_tokenize(sent)
        for word in sent:
            if word.lower() in BAD_GRAMMAR:
                return True
        return False
    
    #third case with bad grammar:
        #this one should be improve in order to get better result but it works for the example sentence
    def correctSent2(self,sent):
        tokens = word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        new_sent = []
        #use tags to spot good words to change
        for (word,tag) in tagged:
            if len(word)>1:
                if word == 'wo':
                    word = 'will'
                if word == 'n\'t':
                    word = 'not'
                print(tag)
                if tag == 'NN' or tag == 'DT' and word in BAD_GRAMMAR:
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
    sentences = [line.rstrip('\n') for line in open('sentences.txt')]
    #create 3 fonctions one for each situation 1: negative words 2: prefixes 3:bad grammar
    #change the current list of words into dictionary or more suitable data type   dn = DblNegatives()
    dn = DblNegatives()
    for sentence in sentences:
        print ('The sentence is:', sentence)
        if (dn.isDblNegatives(sentence)):
            print("The modified sentence is: ")
            if dn.is_negative_word_sentence(sentence):
                dn.correctSent1(sentence)
            elif dn.is_bad_grammar_sentence(sentence):
                dn.correctSent2(sentence)
            print()
        else:
            print ('This sentence does not contain a double negative.')
            print()

    # take in user input of sentences
    sent = ""
    py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

    while(True):
        if py3:
            sent = input("Enter a sentence (\"quit\" to exit the program): ")
            if (sent == "quit"):
                break;
            print ('The sentence is:', sent)
            if (dn.isDblNegatives(sent)):
                print("The modified sentence is: ")
                if dn.is_negative_word_sentence(sent):
                    dn.correctSent1(sent)
                elif dn.is_bad_grammar_sentence(sent):
                    dn.correctSent2(sent)
                print()
            else:
                print ('This sentence does not contain a double negative.')
            print()
        else:
            sent = raw_input("Enter a sentence (\"quit\" to exit the program): ")
            if (sent == "quit"):
                break;
            print ('The sentence is:', sent)
            if (dn.isDblNegatives(sent)):
                print("The modified sentence is: ")
                if dn.is_negative_word_sentence(sent):
                    dn.correctSent1(sent)
                elif dn.is_bad_grammar_sentence(sent):
                    dn.correctSent2(sent)
            print()
if __name__ == '__main__':
    main()
