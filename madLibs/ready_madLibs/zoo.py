def madlibs():
    adj1 = input('adjective: ')
    noun1 = input('noun: ')
    verb_past_tense_1 = input('verb past tense: ')
    adj2 = input('adjective: ')
    adj3 = input('adjective: ')
    noun2 = input('noun: ')
    noun3 = input('noun: ')
    adj4 = input('adjective: ')
    verb2 = input('verb: ')
    adverb = input('adverb: ')
    verb_past_tense_2 = input('verb past tense: ')
    adj5 = input('adjective: ')
    str = f'Today I went to the zoo. I saw a(n)\
{adj1}\
{noun1} jumping up and down in its tree.\
He {verb_past_tense_1} {adj2}\
through the large tunnel that led to its {adj3}\
{noun2}. I got some peanuts and passed\
them through the cage to a gigantic gray {noun3}\
towering above my head. Feeding that animal made\
me hungry. I went to get a {adj4} scoop\
of ice cream. It filled my stomach. Afterwards I had to\
{verb2} {adverb} to catch our bus.\
When I got home I {verb_past_tense_2} my\
mom for a {adj5} day at the zoo.'
    return str