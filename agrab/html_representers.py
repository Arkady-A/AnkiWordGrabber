# this file is for defining all classes and methods that
# are needed to represent word/definintion in html format
from yattag import Doc
import pandas as pd


def html_represent_by_prtofspch(word_definitions):
    '''
    Will represent definitions in html format
    Parameters
    ----------
    word_definitions : object of type data.Word
        An instance containing definitions
    Returns
    -------
    str
        html representation of the instance
    '''
    # collect the word from the object
    word = word_definitions.word
    pronouns = word_definitions.pronounciations
    # convert Word object to dataframe
    word_definitions = pd.DataFrame(word_definitions.get_definitions())
    doc, tag, text = Doc().tagtext()
    groups = word_definitions.groupby('part_of_speech')
    # with tag encapsulates a tag
    with tag('strong'):
        text(word)
    # shows all pronounciations
    text(' ')
    text(', '.join(pronouns))
    for name, group in groups:
        with tag('div', style='margin-bottom:20px;'):
            with tag('div', style='padding-left:10px;'):
                with tag('span'):
                    with tag('strong'):
                        # name of the group is part of speech
                        text(name.lower())
            for index, row in group.iterrows():
                # going though every definitions for part of speech
                with tag('div', style='padding-left:20px;padding-right:20px; margin-bottom: 8px'):
                    # this will create dot symbol
                    doc.asis('&#8226 ')
                    # writing definition
                    text(row['definitions'])
                    # showing synonyms
                    synonyms = row['synonyms']
                    if len(synonyms) > 0:
                        with tag('span', style='color: #898989;'):
                            text(' ('+', '.join(row['synonyms'][:4])+')')
                    with tag('div', style='padding-left:15px;color:#545454'):
                        # showing less than 2 examples
                        for example in row['examples'][:2]:
                            if example != 'None':
                                text(example)
                                doc.stag('br')
    return doc.getvalue()
