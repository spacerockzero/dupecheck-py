# TODO: Use multiprocessing on iterables, since this can be intense

import nltk

nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re
from string import punctuation
from dupecheck.contractions_list import contractions_dict
from dupecheck.utils import v_print
from autocorrect import Speller


# setup
stopword = stopwords.words("english")
wordnet_lemmatizer = WordNetLemmatizer()
snowball_stemmer = SnowballStemmer("english")
spell = Speller()


# functions

# credit: many of these from https://github.com/pemagrg1/Text-Pre-Processing-in-Python

# convert text to lowercase
def lower(text):
    lowered = [w.lower() for w in word_tokenize(text)]
    return lowered


def lower_to_text(text):
    lowered = lower(text)
    return TreebankWordDetokenizer().detokenize(lowered)


# remove html tags
def remove_html(text):
    return re.sub("<[^<]+?>", "", text)


# remove numbers
def remove_numbers(text):
    return "".join(c for c in text if not c.isdigit())


# replace smart quotes with dumb quotes
def smart_to_dumb_quotes(text):
    return text.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")


# replace dumb quotes with smart quotes
def dumb_to_smart_quotes(text):
    return text.replace('"', "“").replace('"', "”").replace("'", "’").replace("'", "‘")


# remove punctuation
def remove_punctuation(text):
    punctuations = """’”“�!()-[]{};:'"\,<>./?@#$%^*_~"""
    return "".join(c for c in text if c not in punctuations)


# lemmatize (like stemming, but links words with similar meaning to one word root form)
def lemmatize(text):
    """returns list of tokenized words"""
    word_tokens = nltk.word_tokenize(text)
    lemmatized_words = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
    return lemmatized_words


def lemmatize_to_text(text):
    """returns text string"""
    lemmatized = lemmatize(text)
    return TreebankWordDetokenizer().detokenize(lemmatized)


def stem(text):
    """returns list of tokenized words"""
    word_tokens = nltk.word_tokenize(text)
    stemmed_words = [snowball_stemmer.stem(word) for word in word_tokens]
    return stemmed_words


def stem_to_text(text):
    """returns text string"""
    stemmed = stem(text)
    return TreebankWordDetokenizer().detokenize(stemmed)


def word_tokenize(text):
    """returns list of tokenized words"""
    return nltk.word_tokenize(text)


def sentence_tokenize(text):
    """returns list of tokenized sentences, with stopwords removed"""
    word_tokens = nltk.word_tokenize(text)
    removing_stopwords = [word for word in word_tokens if word not in stopword]
    return removing_stopwords


def expand_contractions(text, contractions_dict=contractions_dict):
    contractions_pattern = re.compile(
        "({})".format("|".join(contractions_dict.keys())),
        flags=re.IGNORECASE | re.DOTALL,
    )

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = (
            contractions_dict.get(match)
            if contractions_dict.get(match)
            else contractions_dict.get(match.lower())
        )
        expanded_contraction = expanded_contraction
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


def spelling_fix(text):
    """returns list of tokenized words"""
    spells = [spell(w) for w in (nltk.word_tokenize(text))]
    return spells


def spelling_fix_to_text(text):
    """returns string"""
    fixed = spelling_fix(text)
    return TreebankWordDetokenizer().detokenize(fixed)


def word_counts(text):
    word_count = {}
    counts = []
    for word in word_tokenize(text):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # List in sorted order
    for w in sorted(word_count, key=word_count.get, reverse=True):
        counts.append([w, word_count[w]])
    return counts


# heavy pre-processing, used to text comparisons
def pre_process_text(text, verbose=False):
    """shine up dem words real nice"""
    # TODO  multiprocessing, and time each step for verbose logs
    v_print(verbose, "Cleaning: smart_to_dumb_quotes")
    text = smart_to_dumb_quotes(text)

    v_print(verbose, "Cleaning: expand_contractions")
    text = expand_contractions(text)

    v_print(verbose, "Cleaning: remove_punctuation")
    text = remove_punctuation(text)

    v_print(verbose, "Cleaning: lower_to_text")
    text = lower_to_text(text)

    v_print(verbose, "Cleaning: remove_html")
    text = remove_html(text)

    v_print(verbose, "Cleaning: remove_numbers")
    text = remove_numbers(text)

    # v_print(verbose, "Cleaning: spelling_fix_to_text")
    # text = spelling_fix_to_text(text)

    # v_print(verbose, "Cleaning: lemmatize_to_text")
    # text = lemmatize_to_text(text)

    v_print(verbose, "Cleaning: done.")

    return text


test_text = """
“He’s in trouble,” said Skeet.

Kemper seemed to be impressed. “Maybe he should have a drink of water, or some kind of crack.”

Outside, someone in the crowd shouted, “For Dr. Arroway!” and for Dr. Stringson.

quickShip”He wouldn’t drink his beer,” Laurel said.

And with that, the conversation seemed to be abruptly broken off.

reportprint”Have to go,” Charles Freck said. seemed to be abruptly broken off.

reportprint”Have to go,” Charles Freck said. “I can’t talk, about this; you’ll have to carry on, meek as I am.” He managed, half-smile, to extricate himself and walk beside the flag captain, whom the captain over the flapple had promoted to “First Lieutenant” — in response to a hint that Charley might be about to tell a falsehood.

The vidphone booth operator, a female, said, “You are still on the flag, sir, but you are a hint that Charley might be about to tell a falsehood.

The vidphone booth operator, a female, said, “You are still on the flag, sir, but you are seeing a Miss Smith at the projector. Her brother is there and he made it clear by doing something that your flag says on the flagpole.”

The message Beresher held up and Charley turned to her. “Why?” he said. “How could they miss a connection with you?”

�Charley said, “I’ll tell you something,” and hung up the phone. The screen became dark and then it flicked on once more and Charley’s face filled it with message Beresher held up and Charley turned to her. “Why?” he said. “How could they miss a connection with you?”

�Charley said, “I’ll tell you something,” and hung up the phone. The screen became dark and then it flicked on once more and Charley’s face filled it with anguish. “Don’t blame me,” he said. “They had no choice; they got stuck in the prob system. And it’s infectious. The damn vistermans sure as hell didn’t have an idea what it was doing to people in my family! God, what a chance you had! But I guess they— the damn fools—letting the rest of us out … there’s a great biological advantage in intuition, don’t you agree?” He ceased talking, then, me,” he said. “They had no choice; they got stuck in the prob system. And it’s infectious. The damn vistermans sure as hell didn’t have an idea what it was doing to people in my family! God, what a chance you had! But I guess they— the damn fools—letting the rest of us out … there’s a great biological advantage in intuition, don’t you agree?” He ceased talking, then, and sat facing them. His arms, his shoulders—they were broad, muscular, on his good leg, but he sagged.

“What’s wrong, Captain?”

He looked at her.

Dong said, “He says, ‘No.’ .”

“But—he doesn’t mean that he doesn’t.”

“They mean it to him, I guess. Don’t you see? They’re all of us a lot older than he is— what it was doing to people in my family! God, what a chance you had! But I guess they— the damn fools—letting the rest of us out … there’s a great biological advantage in intuition, don’t you agree?” He ceased talking, then, and sat facing them. His arms, his shoulders—they were broad, muscular, on his good leg, but he sagged.

“What’s wrong, Captain?”

He looked at her.

Dong said, “He says, ‘No.’ .”

“But—he doesn’t mean that he doesn’t.”

“They mean it to him, I guess. Don’t you see? They’re all of us a lot older than he is—don’t we—you know.”

“I’m sorry,” Ben said, and crossed his face, covering his mouth.

�The Ship’s cop drew her gun. “I’ll kill him. I don’t think there’s any point in killing him.”

“But,” Dong said, “this is the middle of town; nobody will fire at anyone, now that he’s there. You have the direct conduit from this planet; if he dies—”

“It
"""

# processed = pre_process_text(test_text)
# print(processed)
