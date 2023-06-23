def add_prefix_un(word):
    return 'un' + word
print(add_prefix_un("happy"))

def make_word_groups(words):
    return [words[0] + ' :', words[0] + words[1], words[0] + words[2], words[0] + words[3]]
print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))

def remove_suffix_ness(word):
    word = word.replace('ness', '')
    if word[-1] == 'i':
        return word[:-1] + 'y'
    else:
        return word
print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))

def adjective_to_verb(sentence, index):
    sentence = sentence.split()
    if index == -1:
        return sentence[index].replace('.', '') + 'en'
    else:
        return sentence[index] + 'en'
print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))