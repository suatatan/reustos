import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.

# duplicated entry remover in data frame 

def remove_duplicate(df):
    df = df.drop_duplicates(subset=['title'], keep='first')
    return df

# function to remove the stop words
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))