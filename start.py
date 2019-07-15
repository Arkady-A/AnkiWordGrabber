# this function will collect definitions
from agrab.html_collectors import collect_oxford
# this function will represent definitions in html format
from agrab.html_representers import html_represent_by_prtofspch
import time
import pandas as pd
import random
import os

output_file_path = 'output.txt'
input_file_path = 'input.csv'
words_not_found = []

input_df = pd.read_csv(input_file_path)
print('list of words: ', ', '.join(input_df.loc[:, 'words'].values))
if os.path.exists(input_file_path):
    print('Input file found')
    with open(output_file_path, 'w') as f:
        for word in input_df.loc[:, 'words']:
            # sleep in random time between 1 and 3 seconds
            time.sleep(random.random()*2+1)
            # collectin information about a word
            word_info = collect_oxford(word)
            # None when word haven't been found
            if word_info is None:
                print('Word "{}" is *not* found'.format(word))
                words_not_found.append(word)
                continue
            # represent it in html format
            html_repr = html_represent_by_prtofspch(word_info)
            f.write('='*10+'\n')
            f.write(html_repr)
            f.write('\n'+'='*10)
            f.write('\n')
            print('Word "{}" is found!'.format(word))
    print('List of words that are not found:', words_not_found)
    pd.DataFrame(words_not_found, columns=['words']).to_csv('not_found.csv',
                                                            index=False)
else:
    print('[ERORR] Input file isnt found')

# repr = html_represent_by_prtofspch(a)
