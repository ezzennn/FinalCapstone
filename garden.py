import spacy
nlp = spacy.load('en_core_web_sm')
gardenpathSentences = ['The complex houses married and single soldiers and their families', 'The horse raced past the barn fell', 'Mary gave the child a Band-Aid', 'That Jill is never here hurts', 'The cotton clothing is made of grows in Mississipi']
for i in gardenpathSentences:
    doc = nlp(i)
    print(([token.orth_ for token in doc]))

for i in gardenpathSentences:
    nlp_i = nlp(i)
    print([(i, i.label_, i.label) for i in nlp_i.ents])

entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

# GPE - Geopolitical Entity (Correctly Used)
# PERSON - Person (Correctly Used)