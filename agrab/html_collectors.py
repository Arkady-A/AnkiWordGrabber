# this file is for defining all classes and methods that
# are needed to collect word/defininition
from .data import Word
import requests as req
from bs4 import BeautifulSoup
import re

def load_data(link):
    '''
    Collects html from a link
    Parameters
    ----------
    link : str
        html link
    Returns
    -------
    str of None
        html text or None if the status code of the response was 404
    '''
    response = req.get(link)
    if response.status_code == 404:
        return None
    else:
        return response.text


def collect_oxford(word):
    '''
    Collects definitions for a given word. If the dictionary
    returns different word (e.g. requesting "evolving" from lexico
    will return definition of "evolve") this function will return
    a definition for returned from lexico word
    Parameters
    ----------
    word : str
        A word for which the deffinition should be found
    Returns
    -------
    object of type data.Words or None
        Object that will handle all definitions from the dictionary
        if the word haven't been found returns None
    '''
    word = word.strip().lower()
    link = 'https://www.lexico.com/en/definition/{}'.format(word)
    source = 'web:dictionary.lexico.com'
    raw_html = load_data(link)
    # is raw_html is none that means that load data got 404 error
    if raw_html is None:
        return None
    parser = BeautifulSoup(raw_html, 'html.parser')
    # if you've found a string starting 'No exact' that means the dictionary
    # haven't found the words you were searching
    no_results = bool(parser.find(text=re.compile('No exact')))
    if no_results:
        return None
    # in the dictionary the word is contained in a span object
    # with a class 'hw'
    word_from_html = parser.find('span', class_='hw').contents[0]
    # every section of definition is lied inside a section object with
    # a class 'gramb'. A section is definitions within a part of speech
    # e.g. noun section, verb section e.t.c
    sections = parser.find_all('section', class_='gramb')
    # collect all possible pronouns
    pronounciations = parser.find_all('span', class_='phoneticspelling')
    # convert them into a list
    pronounciations = [pronoun.text for pronoun in pronounciations]
    
    word_definitions = Word(word_from_html, pronounciations)
    for section in sections:
        # this will return part_of_speech
        part_of_speech = section.find('span', class_='pos').text
        # gets all sections of definitions
        sections_of_defitions = section.find_all('div', class_='trg')
        for sub_section in sections_of_defitions:
            # main definition is contained in span with trg class.
            # there's subsenses in the definition section, but it's
            # beign ignored at least for now
            definition_html = sub_section.find('span', class_='ind')
            # because we dont collect subsense if there is not definition
            # we should skip that iteration
            if definition_html is None:
                continue
            definition = definition_html.text
            examples_sections = sub_section.find_all('li', class_='ex')
            # this will create list of examples
            examples = [exmpl.text for exmpl in examples_sections]
            synonyms_section = sub_section.find_all('strong', class_='syn')
            # same as above - will create a list of synonyms
            synonyms = [synm.text for synm in synonyms_section]
            word_definitions.add_definition(definition, part_of_speech,
                                            examples, source, synonyms)
    return word_definitions
