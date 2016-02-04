# TASK : One
# 1) Generate the list of all multiword corrections in the wikied
# corpus in a seperate file sorted by decreasing frequency.

# Result = freq <multiword>


import nltk
from nltk import word_tokenize
import re

FILENAME ="data/partial_test" # test
#FILENAME = "data/enwikibooks-20140326-pages-meta-history.xml.txt.wiked" # actual

# to hold the correction words or phrases
CORRECTIONS = []

# hold dict of multiword with its Frequency
FREQDICT = {}

# Regular Expression
REGX_SHALLOW = re.compile(r"(\[|\{)(\-|\+).*(\+|\-)(\]|\})", re.IGNORECASE)

REGX_ERROR = re.compile(r"\[[\s-]?\w.*?\]", re.IGNORECASE)
REGX_CORRECT = re.compile(r"\{[\s\+]?\w.*?\}", re.IGNORECASE)


def is_multiword(text):
    """
    check if correction word is multi-word
    checking if phrase consist of multiple word
    :param text:
    :return:
    """
    if len(text) > 2:
        return True
    return False


def extract_correction_word(text, regex):
    """
    function to comb each line of data for correction phrase
    :param text: raw text
    :param regex: regular expression
    :return:
    """
    result = []
    list = regex.finditer(text)
    if result is not None:
        result = [i.group() for i in list]
        return result
    else:
        return None



def extract_pattern_text(text, regex):
    """
    Extract the raw text from the correction phrases or words
    {+ someWords +} = somWords
    [+ someOtherWords +] = someOtherWords
    :param text, regex:
    text = data for processing
    regex = regular expression
    :return:text
    processed data
    """
    text_list = re.finditer(regex, text)
    result = [i.group() for i in text_list]
    if len(result) > 0:
        result = [i for i in result if len(i) > 0]
        return result
    else:
        return None




def main():
    with open(FILENAME) as fd:
        for line in fd:
            if not line.startswith("#"):
                res = extract_correction_word(line, REGX_SHALLOW)
                if not res == None:
                    CORRECTIONS.append(res)
    print("Extracted text: ")
    for l in CORRECTIONS:
        error, correct = extract_correction_word(str(l), REGX_ERROR), \
                         extract_correction_word(str(l), REGX_CORRECT)
        error_list = [extract_pattern_text(e, r"\w*")for e in error if len(e) > 0]
        correct_list = [extract_pattern_text(c, r"\w*") for c in correct if len(c) > 0]

        print("Error : ", [is_multiword(w) for w in error_list])
        print("Correct : ", [is_multiword(w) for w in correct_list])




if __name__ == "__main__":
    main()

