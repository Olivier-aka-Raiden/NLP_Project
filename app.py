from __future__ import division
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from sys import version_info
import nltk, re, pprint, sys, getopt

#/!\Notice : Program written with python 3.4.1; print may have errors

# list of words for double negatives using negative words
NEGATIVE_WORDS = set(['hardly', 'seldom', 'scarcely', 'barely', 'rarely'])
# list of common negative words
NEGATIVE = set(['not','n\'t','nothing','nobody','never','no','none','neither','nowhere'])
# list of negative prefixes
NEGATIVE_PREFIXES = set(['in', 'un', 'im', 'non', 'ir', 'il'])
# list of words for double negatives using prefixes
NEGATIVE_PREFIX_WORDS = set()
# list of words for double negatives using bad grammar
BAD_GRAMMAR = set(['nothing','never','no','ai','not','neither','nowhere','none','nobody'])

# populate the negative prefixes set
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
for w in [w for w in wordlist if re.search('^(in|un|im|non|ir|il)', w)]:
    NEGATIVE_PREFIX_WORDS.add(w)

# remove words that are not negative
to_remove = ['in', 'under', 'understand', 'ill', 'none', 'impact', 'impede', 'impend']
for word in to_remove:
    NEGATIVE_PREFIX_WORDS.remove(word)

class DblNegatives(object):

    # check if the sentence contains a double negative
    def contains_double_negative(self, sentence):
        neg_count = 0
        tokens = word_tokenize(sentence)
        # check the number of negative meaning words
        for t in tokens:
            if t.lower() in NEGATIVE or t.lower() in NEGATIVE_WORDS or t.lower() in NEGATIVE_PREFIX_WORDS:
                #print 'FOUND A NEGATIVE WORD, IT WAS:', t
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
                print ("This sentence is a negative word sentence.\n")
                print ("The modified sentence is: ")
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
                elif word == 'ca':
                    word = 'can'
                elif word == 'n\'t':
                    word = 'not'
                elif word == 'no':
                    word = 'any'
                elif word == 'did':
                    word = ''
                elif word == 'do':
                    word = ''
                elif word == 'does':
                    word = ''
                elif word == 'go':
                    word == 'goes'
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
            if word.lower() in NEGATIVE_PREFIX_WORDS:
                print ("This sentence is a negative prefix sentence.\n")
                print ("The modified sentence is: ")
                return True
        return False

    # correct the double negative sentence using negative prefixes
    def correct_negative_prefix_sentence(self, sent):
        sent = word_tokenize(sent)
        new_sent = []
        for word in sent:
            if word.lower() not in NEGATIVE_PREFIX_WORDS and word.lower() not in NEGATIVE:
                new_sent.append(word)
            # remove the negative prefix
            else:
                for prefix in NEGATIVE_PREFIXES:
                    if prefix in word:
                        word = word[len(prefix):]
                        new_sent.append(word)
                        break
        new_sent = ' '.join(new_sent)
        print (new_sent+"\n")
    #check if there is redundant use of "not"
    def is_not_redundant(self, sent):
        sent = word_tokenize(sent)
        nb_not = 0
        redundant_words = ['not', 'n\'t', 'nothing', 'none', 'cannot', 'no', 'nowhere', 'nobody']
        for word in sent:
            if word.lower() in redundant_words:
                nb_not = nb_not + 1
        if nb_not == 2:
            print ("This sentence uses \'not\' two times.\n")
            print ("The modified sentence is: ")
            return True
        return False

    def correct_redundant_not(self, sent):
        tokens = word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        new_sent = []
        excp = 0
        #use tags to spot good words to change
        for (word,tag) in tagged:
            if len(word)>1:
                if word == 'wo':
                    word = 'won\'t'
                if word == 'ai':
                    word = 'did'
                    excp = 1
                if word == 'Ai':
                    word = ''
                if word == 'ca':
                    word = 'can'
                if word == 'got' and excp == 1:
                    word == 'get'
                if word == 'n\'t':
                    word = ''
                elif word == 'not':
                    word = ''
                elif word == 'nothing':
                    new_sent.append('something')
                elif word == 'none':
                    new_sent.append('some')
                elif word == 'no':
                    new_sent.append('any')
                elif word == 'nowhere':
                    new_sent.append('anywhere')
                elif word == 'nobody':
                    new_sent.append('somebody')
                else:
                    new_sent.append(word)
            else:
                    new_sent.append(word)
        new_sent = ' '.join(new_sent)
        print (new_sent+"\n")

    # check if it is a double negative sentence using bad grammar
    def is_bad_grammar_sentence(self, sent):
        sent = word_tokenize(sent)
        for word in sent:
            if word.lower() in BAD_GRAMMAR:
                print ("This sentence is a bad grammar sentence.\n")
                print ("The modified sentence is: ")
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
        elif word == 'nowhere':
            return 'anywhere'
        elif word == 'neither':
            return 'either'
        elif word == 'none':
            return 'none'
        elif word == 'nobody':
            return 'anybody'
        else:
            return word

    # correct the double negative sentence using bad grammar
    def correct_bad_grammar_sentence(self, sent):
        tokens = word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        modification = 0
        new_sent = []
        excp=0
        #use tags to spot good words to change
        for (word,tag) in tagged:
            if len(word)>1:
                if word == 'wo':
                    word = 'will'
                if word == 'ai':
                    word = 'didn\'t'
                    excp = 1
                if word == 'Ai':
                    word = ''
                if word == 'ca':
                    word = 'can'
                if word == 'got' and excp == 1:
                    word = 'get'
                if word == 'n\'t':
                    word = 'not'
                if (tag == 'NN' or tag == 'DT' or tag == 'RB') and (word in BAD_GRAMMAR) and modification == 0:
                    if (word != 'never'):
                        new_sent.append (self.change_bad_grammar(word.lower()))
                        if excp == 0:
                            modification = 1
                    else:
                         new_sent.append (word)
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

            if self.is_negative_word_sentence(sentence):
                self.correct_negative_word_sentence(sentence)

            elif self.is_negative_prefix_sentence(sentence):
                self.correct_negative_prefix_sentence(sentence)

            elif self.is_not_redundant(sentence):
                self.correct_redundant_not(sentence)

            elif self.is_bad_grammar_sentence(sentence):
                self.correct_bad_grammar_sentence(sentence)
        else:
            print ('This sentence does not contain a double negative.')


def main(argv):
    print('*/----------------------------------------------------------------*/')
    print('*/CS372 NLP project: Double negatives')
    print('*/objective: correcting sentences with double negative to make')
    print('*/easier to understand.')
    print('*/----------------------------------------------------------------*/')

    dn = DblNegatives()

    score = 0
    total_score = 0
    num_scored = 0

    # get user's command line arguments
    try:
        opts, args = getopt.getopt(argv, "hti")
    except getopt.GetoptError:
        print ('usage: app.py -t')
        print ('usage: app.py -i')
        sys.exit(2)

    for opt, arg in opts:
        # print usage
        if opt == '-h':
            print ('usage: app.py -t')
            print ('usage: app.py -i')
            sys.exit()

        # read test sentences from a text file
        elif opt == "-t":
            sentences = [line.rstrip('\n') for line in open('sentences.txt')]
            for sentence in sentences:
                dn.process_sentence(sentence[:-1])

                # process the manual scoring
                # 1 - the program incorrectly detects presence of double negative
                # 2 - the program correctly detects but incorrectly modifies
                # 3 - the program correct detects and correctly modifies
                score = int(sentence[-1])
                total_score += score
                num_scored += 1

            print ('The average score of the program is:', total_score / num_scored)
            print ('The number of sentences scored so far is:', num_scored)

        # take in user input of sentences
        elif opt == "-i":
            sent = ""
            py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

            total_score = 204
            num_scored = 73

            while(True):
                if py3:
                    sent = input("Enter a sentence (\"quit\" to exit the program): ")
                    if (sent == "quit"):
                        break;
                    dn.process_sentence(sent)
                    score = int(input("Enter the score for the correction: "))
                    total_score += score
                    num_scored += 1
                    print ('The average score of the program is:', total_score / num_scored)
                    print ('The number of sentences scored so far is:', num_scored)
                else:
                    sent = raw_input("Enter a sentence (\"quit\" to exit the program): ")
                    if (sent == "quit"):
                        break;
                    dn.process_sentence(sent)
                    score = input("Enter the score for the correction: ")
                    total_score += score
                    num_scored += 1
                    print ('The average score of the program is:', total_score / num_scored)
                    print ('The number of sentences scored so far is:', num_scored)


if __name__ == '__main__':
    main(sys.argv[1:])
