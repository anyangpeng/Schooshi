import spacy

nlp = spacy.load('en_core_web_sm')


def qke(query):
    '''
    This Function Is Designed For Keywords Extraction From A Query

    It takes a query string and return a list of keywords (keywords chunks), only ADJ, NOUN, and PROPN are considered.

    Author:Anyang Peng
    Time: September 7, 2020 (CDT) 6:35 pm
    '''
    q = nlp(query)
    token_list = []
    keywords_lsit = []
    for token in q:
        if token.pos_ == 'NOUN' or token.pos_ == 'ADJ' or token.pos_ == 'PROPN':
            token_list.append(token)  # Generating candidate token
            for candidate in token_list:
                if candidate.pos_ == 'ADJ' and candidate.i != len(
                        q) - 1:  # Checking if ADJ is the last token, eg. French
                    if candidate.pos_ == 'ADJ' and q[(candidate.i + 1)].pos_ != 'NOUN':  # Checking if ADJ is next to
                        # a NOUN
                        token_list.remove(candidate)

    # Grouping Adjacent Words
    if len(token_list) == 1:
        keywords_lsit.append(token_list[0].lemma_)
    elif len(token_list) > 1:
        for t in range(len(token_list) - 1):
            if (token_list[t + 1].i - token_list[t].i) != 1:
                keywords_lsit.append(token_list[t].lemma_)
            else:
                keywords_lsit.append(token_list[t].lemma_ + ' ' + token_list[t + 1].lemma_)
    return keywords_lsit


