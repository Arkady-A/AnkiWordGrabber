class Word():
    '''
    Class that handles words and their definitions
    '''

    def __init__(self, word, pronounciations ):
        '''
        Parameters
        ----------
            word : str
        '''
        self.word = word
        self.pronounciations = pronounciations
        # dictionary of structure {'column':[rows]}
        self.definitions = {'definitions': [], 'part_of_speech': [],
                            'examples': [], 'source': [],
                            'synonyms': []}

    def add_definition(self, definition, part_of_speech, examples,
                       source='Not Specified', synonyms=[]):
        '''
        Adds a definition to list of definitions
        Parameters
        ----------
        definition : str
            A definition for a word
        part_of_speech : str
            Word's part of speech in which the definition applies (noun,
            verb e.t.c.)
        source : str optional
            The source of definition
        '''
        for column, var in list(zip(self.definitions, [definition,
                                                       part_of_speech,
                                                       examples,
                                                       source,
                                                       synonyms])):
            self.definitions[column].append(var)
        return True

    def drop_definition(self, index):
        '''
        Drop a definition from the list of definitions
        Parameters
        ----------
        index : int
            Values between 0 and n. Index that indentifies the definition
        Returns
        -------
        dictionary
            dropped definition
        '''
        dropped_definition = {}
        for column in self.definitions:
            dropped_definition[column] = self.definitions[column].pop(index)
        return dropped_definition

    def get_definitions(self):
        '''
        Returns
        -------
        Definitions
        '''
        return self.definitions

    def __str__(self):
        return 'Word:\t{}\nPronounciations:\t{}\n'.format(self.word, ', '.join(
            self.pronounciations))+str(self.definitions)
