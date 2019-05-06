import json
import spacy
import inflect


p = inflect.engine()
nlp = spacy.load('en_core_web_sm')
words = json.load(open('english-words/words_dictionary.json', 'r'))


def is_singular(word)
    return p.singular_noun(word) == False


def get_next_noun(word, n):
    noun_counter = 0
    w_is_singular = is_singular(word)
    for i, w in enumerate(words):
        if w == word:
            for i2, w2 in enumerate(words):
                if i <= i2:
                    if word in w2:
                        continue
                    doc = nlp(w2)
                    token = [t for t in doc][0]
                    w2_is_singular = is_singular(w2)
                    if token.pos_ == 'NOUN':
                        if w_is_singular and w2_is_singular:
                            noun_counter = noun_counter + 1
                        if not w_is_singular:
                            noun_counter = noun_counter + 1
                    if noun_counter == n:
                        return w2


def rewrite(poem, noun_count):
    doc = nlp(poem)
    new_poem = ''
    for token in doc:
        new_word = token.text
        if token.pos_ == 'PUNCT':
            new_poem = new_poem + new_word
            continue
        if token.pos_ == 'NOUN':
            new_word = get_next_noun(token.text, noun_count)
        new_poem = new_poem + ' ' + new_word
    return new_poem


if __name__ == '__main__':
    poem = """
    Mary had a little lamb,
    whose fleece was white as snow.
    """
    new_poem = rewrite(poem, 10)
    print(new_poem)
