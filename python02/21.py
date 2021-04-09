import re

#(you can change the word to whatever below)
text_to_speak = '''
abc
ABC
123

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

Judyms.com

321-555-4321
123.555.1234

Mrs. ugly
Mrs. pretty
Mrs. perfect
Mrs. inperfect
Mrs. shark

'''

sentence = 'Start a sentence and bring it to an end'

pattern = re.compile(r'sentence')
#(you can write: r'/d/d[-.]/d/d' or this: r'[^a-zA-Z]'
# or: r'\d{3}.\d{3}.\d{4}' in it
# you can also change the word to whatever)

matches = pattern.finditer(text_to_speak)
#(you can wirght any word as the same down below)



for match in matches:
    print(match)
    #(you can hashtag for match in matches:
    # and detlete the first thing before the word
    # print)