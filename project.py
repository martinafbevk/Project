

 #helper function
def  clean_text(txt):
    """hat takes a string of text txt as a parameter and returns a
    list containing the words in txt after it has been “cleaned”."""
    
    
    for symbol in """.,?"'!;:""":
        txt = txt.replace(symbol, '')
        
    words = txt.lower().split()
        
    return words


class TextModel:
    
    def __init__(self, model_name) :
        """ constructs a new TextModel object by accepting a string model_name
        as a parameter and initializing the following three attributes:"""


        self.name = model_name
        self.words = ({})  # number of times each word appears in the text.
        self.word_lengths = ({}) #number of times each word length appears.
        
    def __repr__(self):
        result = "text model name: " + str(self.name) + "\n  number of words: " + str(len(self.words)) + "\n  number of word lengths: " + str(len(self.word_lengths))
        return result
    
    def add_string(self, s):
        """that adds a string of text s to the model by augmenting the 
        feature dictionaries defined in the constructor."""
        
     # Add code to clean the text and split it into a list of words.
     # *Hint:* Call one of the functions you have already written!
    
        word_list = clean_text(s)
        
        for w in word_list:
          
            
          if w in self.words:
                self.words[w] += 1
          else:
                self.words[w] = 1
                
          length = len(w)
          if length in self.word_lengths:
                self.word_lengths[length] += 1
          else:
                self.word_lengths[length] = 1 
                
    def add_file(self, filename):
        """that adds all of the text in the file identified by 
        filename to the model."""
        
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        content = f.read()
        
        self.add_string(content)
            
        
    def save_model(self):
    
        """Saves the TextModel object self by writing its various 
            feature dictionaries to files."""
    
  
        words_filename = self.name + '_words'
        with open(words_filename, 'w') as f_words:
            f_words.write(str(self.words))

   
        word_lengths_filename = self.name + '_word_lengths'
        with open(word_lengths_filename, 'w') as f_word_lengths:
            f_word_lengths.write(str(self.word_lengths))
            
    def read_model(self):
        
        """that reads the stored dictionaries for the called TextModel object
            from their files and assigns them to the attributes of the called TextModel."""
            
    
        words_filename = self.name + '_words'
        with open(words_filename, 'r') as f_words:
            words_str = f_words.read()
            self.words = dict(eval(words_str))

            
        word_lengths_filename = self.name + '_word_lengths'
        with open(word_lengths_filename, 'r') as f_word_lengths:
            word_lengths_str = f_word_lengths.read()
            self.word_lengths = dict(eval(word_lengths_str))

 #helper function
def  clean_text(txt):
    """hat takes a string of text txt as a parameter and returns a
    list containing the words in txt after it has been “cleaned”."""
    
    
    for symbol in """.,?"'!;:""":
        txt = txt.replace(symbol, '')
        
    words = txt.lower().split()
        
    return words

def stem(s):
    """The function should then return the stem of s. The stem of a word is 
       the root part of the word, which excludes any prefixes and suffixes
    """
    if s[-3:] == "ing":
        s = s[:-3]
    elif s[-1] == "s":
            s = s[:-1]
    elif s[-2:] == "er":
        s = s[:-2]
    elif s[-1] == "y":
        s = s[:-1] + "i"
    elif len(s) >= 4 and s[-4:] == "ies":
        return stem(s[:-3])
    elif s[-2:] == "ly":
        s = s[:-2]
    elif s[-1] == "e":
        s = s[:-1]
    else:
        return s
    return s
    rest = stem(s)
    return rest


class TextModel:
    
    def __init__(self, model_name) :
        """ constructs a new TextModel object by accepting a string model_name
        as a parameter and initializing the following three attributes:"""

        self.name = model_name
        self.words = {}  # number of times each word appears in the text.
        self.word_lengths = {} #number of times each word length appears.
        self.stems = {}
        self.sentence_lengths = {}
        self.repetition = {}
        # self.similarity_scores =  #ask
        # self.classify = #aks

        
        
    def __repr__(self):
        result = "text model name: " + str(self.name) + "\n  number of words: " + str(len(self.words)) + "\n  number of word lengths: " + str(len(self.word_lengths)) + "\n"
        result += "  number of stems: " + str(len(self.stems)) + "\n"
        result += "  number of sentence lengths: " + str(len(self.sentence_lengths)) + "\n"
        result += "  number of word repetitions: " + str(len(self.repetition)) + "\n"
        return result
    
    def add_string(self, s):
        """that adds a string of text s to the model by augmenting the 
        feature dictionaries defined in the constructor."""
        
     # Add code to clean the text and split it into a list of words.
     # *Hint:* Call one of the functions you have already written!
        word_list = clean_text(s)
        
        for w in word_list:
          
            
          if w in self.words:
                self.words[w] += 1
          else:
                self.words[w] = 1
                
          length = len(w)
          if length in self.word_lengths:
                self.word_lengths[length] += 1
          else:
                self.word_lengths[length] = 1 
                
          stemmed_word = stem(w)
          if stemmed_word in self.stems:
             self.stems[stemmed_word] += 1
          else:
             self.stems[stemmed_word] = 1
        
          if w in self.repetition:
              self.repetition[w] += 1
          else:
              self.repetition[w] = 1     
                
                
        sentence_list = s.split(". ")
        for sentence in sentence_list:
           cleaned_s = clean_text(sentence)
           length = len(cleaned_s)
           if length in self.sentence_lengths:
              self.sentence_lengths[length] += 1 
           else:
              self.sentence_lengths[length] = 1
                  
              
        
        words_in_total = len(word_list)
        for word in self.repetition:
             self.repetition[word] /= int(words_in_total)
              
             
                
    def add_file(self, filename):
        """that adds all of the text in the file identified by 
        filename to the model."""
        
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        content = f.read()
        
        self.add_string(content)
            
        
    def save_model(self):
    
        """Saves the TextModel object self by writing its various 
            feature dictionaries to files."""
    
  
        words_filename = self.name + '_words'
        with open(words_filename, 'w') as f_words:
            f_words.write(str(self.words))

   
        word_lengths_filename = self.name + '_word_lengths'
        with open(word_lengths_filename, 'w') as f_word_lengths:
            f_word_lengths.write(str(self.word_lengths))
            
        sentence_lengths_filename = self.name + '_sentence_lengths'
        with open(sentence_lengths_filename, 'w') as f_sentence_lengths:
            f_sentence_lengths.write(str(self.sentence_lengths))
            
            
        stems_filename = self.name + '_stems'
        with open(stems_filename, 'w') as f_stems:
            f_stems.write(str(self.stems))
            
            
        repetition_filename = self.name + '_repetition'
        with open(repetition_filename, 'w') as f_repetition:
            f_repetition.write(str(self.repetition))
        
        
    def read_model(self):
        
        """that reads the stored dictionaries for the called TextModel object
            from their files and assigns them to the attributes of the called TextModel."""
            
    
        words_filename = self.name + '_words'
        with open(words_filename, 'r') as f_words:
            words_str = f_words.read()
            self.words = dict(eval(words_str))

            
        word_lengths_filename = self.name + '_word_lengths'
        with open(word_lengths_filename, 'r') as f_word_lengths:
            word_lengths_str = f_word_lengths.read()
            self.word_lengths = dict(eval(word_lengths_str))
            
        sentence_lengths_filename = self.name + '_sentence_lengths'
        with open(sentence_lengths_filename, 'r') as f_sentence_lengths:
            sentence_lengths_str = f_sentence_lengths.read()
            self.sentence_lengths = dict(eval(sentence_lengths_str))

        stems_filename = self.name + '_stems'
        with open(stems_filename, 'r') as f_stems:
            stems_str = f_stems.read()
            self.stems = dict(eval(stems_str))
        
        repetition_filename = self.name + '_repetition'
        with open(repetition_filename, 'r') as f_repetition:
            repetition_str = f_repetition.read()
            self.repetition = dict(eval(repetition_str))
    
        
        
    def similarity_scores(self, other):
         """computes and returns a list of log similarity scores measuring 
            the similarity of self and other – one score for each type of 
            feature
         """
         scores = [compare_dictionaries(other.words, self.words), \
                 compare_dictionaries(other.word_lengths, self.word_lengths), \
           compare_dictionaries(other.stems,self.stems ), \
          compare_dictionaries(other.sentence_lengths,self.sentence_lengths), \
                 compare_dictionaries(other.repetition,self.repetition)]
                       
         return scores
     
    def classify(self, source1, source2):
         """compares the called TextModel object (self) to two other “source”
            TextModel objects (source1 and source2) and determines which of 
            these other TextModels is the more likely source of the called 
            TextMode
         """
         scores1 = self.similarity_scores(source1)
         scores2 = self.similarity_scores(source2)
         
         print("scores for", source1.name, ": ", scores1)
         print("scores for", source2.name, ": ", scores2)
         
         count_source1 = 0
         count_source2 = 0
         
         for i in range(len(scores1)):
             if scores1[i] > scores2[i]:
                 count_source1 += 1
             elif scores2[i] > scores1[i]:
                 count_source2 += 1
        
         if count_source1 > count_source2:
            print(self.name, "is more likely to have come from", source1.name)
         else:
            print(self.name, "is more likely to have come from", source2.name)
    

import math            
def compare_dictionaries(d1, d2):
    """take two feature dictionaries d1 and d2 as inputs, and it should 
       compute and return their log similarity score 
    """
    if not d1:
        return -50
    total = sum(d1.values())
    
    score = 0
    for i in d2:
        if i in d1:
            probability = d1[i] / total
        else:
            probability = 0.5 / total
        score += math.log(probability) * d2[i]
    return score


def test():
        """ Generates instances of TextModels (source1, source2, mystery), 
            appends sample texts, and categorizes'mystery' according to how 
            closely it resembles'source1' and'source2'
        """
        source1 = TextModel('source1')
        source1.add_string('It is interesting that she is interested.')

        source2 = TextModel('source2')
        source2.add_string('I am very, very excited about this!')

        mystery = TextModel('mystery')
        mystery.add_string('Is he interested? No, but I am.')
        mystery.classify(source1, source2)



def run_tests():
    """ Generates TextModel instances for TV show sources, appends sample
        texts from relevant files, and categorizes new texts according to how 
        close they are to the original sources
    """
    source1 = TextModel('friends')
    source1.add_file('Friends_text.txt')

    source2 = TextModel('How I met your Mother')
    source2.add_file('HMYM_text.txt')

    new1 = TextModel('New Girl')
    new1.add_file('New_Girl_text.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('Suits')
    new2.add_file('Suits_text.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('Gossip Girl')
    new3.add_file('Gossip_Girl_text.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('Money Heist')
    new4.add_file('Money_Heist_text.txt')
    new4.classify(source1, source2)

         
            
            
                
                     
            
       
        

        
        