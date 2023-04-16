import string
import re
from nltk.corpus import stopwords
import pandas as pd

stop_words = set(stopwords.words('english'))

# remove numbers
def remove_numbers(text):
    'Remove all the numbers from the text'
    result = re.sub(r'\d+', '', text)
    return result

# remove special characters
def remove_special_characters(text):
    'Remove all the special characters from the text'
    pattern = r'[^a-zA-z0-9\s]'
    text = re.sub(pattern, '', text)
    return text

# remove extra spaces
def remove_extra_spaces(text):
    'remove extra spaces from the text'
    text = re.sub(' +', ' ', text)
    return text

def word_tokenize(text):
    'tokenize the text'
    text = text.split()
    return text

# remove stop words
def remove_stop_words(text):
    'remove stop words from the text'
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stop_words]
    filtered_sentence = (" ").join(tokens_without_sw)
    return filtered_sentence

# remove all preprocessing
def remove_all_preprocessing(text):
    'Remove all the preprocessing from the text'
    text = remove_numbers(text)
    text = remove_special_characters(text)
    text = remove_extra_spaces(text)
    text = remove_stop_words(text)
    return text

def process_text(training_dataset, val_dataset, testing_dataset):
    'run all process above to clean titles'

    stop_words = set(stopwords.words('english'))
    punctuations = string.punctuation

    # apply all preprocessing
    training_dataset['proc_title'] = training_dataset['title'].apply(lambda x: remove_all_preprocessing(x))
    val_dataset['proc_title'] = val_dataset['title'].apply(lambda x: remove_all_preprocessing(x))
    testing_dataset['proc_title'] = testing_dataset['title'].apply(lambda x: remove_all_preprocessing(x))

    # get rid of \
    training_dataset['proc_title'] = training_dataset['proc_title'].apply(lambda x: x.replace('\\', ''))
    val_dataset['proc_title'] = val_dataset['proc_title'].apply(lambda x: x.replace('\\', ''))
    testing_dataset['proc_title'] = testing_dataset['proc_title'].apply(lambda x: x.replace('\\', ''))
    # lower case
    training_dataset['proc_title'] = training_dataset['proc_title'].apply(lambda x: x.lower())
    val_dataset['proc_title'] = val_dataset['proc_title'].apply(lambda x: x.lower())
    testing_dataset['proc_title'] = testing_dataset['proc_title'].apply(lambda x: x.lower())

    return training_dataset, val_dataset, testing_dataset

if __name__ == "__main__":
    training_dataset = pd.read_csv('data/training_dataset.csv')
    val_dataset = pd.read_csv('data/val_dataset.csv')
    testing_dataset = pd.read_csv('data/testing_dataset.csv')
    training_dataset, val_dataset, testing_dataset = process_text(training_dataset, val_dataset, testing_dataset)