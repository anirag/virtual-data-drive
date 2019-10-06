# Helper functions to clean Complaint type
import nltk
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def clean_col(col):
    col = col.tolist()
    ls_col = []
    for c in col:
        c = re.sub('[^a-zA-Z- ]','',c)
        c = c.split()
        c = ' '.join(c)
        c = c.lower()
        ls_col.append(c)
    return ls_col


def cleaner_col(col, lemmatize=True, stem=False):
    ps = PorterStemmer()
    wnl = WordNetLemmatizer()
    col = col.tolist()
    ls_col = []
    for c in col:
        c = re.sub('[^a-zA-Z- ]','',c)
        c = c.split()
        c = ' '.join(c)
        c = c.lower()
        ls_word = []
        eng_stopwords = set(stopwords.words('english'))
        
        for word in c.split():
            word = re.sub(r'[-/]','',word)
            if word not in eng_stopwords:
                if lemmatize is True:
                    word=wnl.lemmatize(word)
                elif stem is True:
                    if word == 'oed':
                        continue
                    word=ps.stem(word) 
                    
            ls_word.append(word)
        words = ' '.join(ls_word)    
        ls_col.append(words)

    return ls_col

# Use case
df['CitySvcReq'] = cleaner_col(df['Complaint.Type'])
