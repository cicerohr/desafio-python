"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    Examples:
        >>> add_prefix_un('happy')
        'unhappy'
        >>> add_prefix_un('manageable')
        'unmanageable'

    Args:
        word: containing the root word.

    Returns:
        of root word prepended with 'un'.
    """
    return f'un{word}'


def make_word_groups(vocab_words: list) -> str:
    """Transform a list containing a prefix and words into a string with the
    prefix followed by the words with prefix prepended.

    This function takes a `vocab_words` list and returns a string with the
    prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
        'en :: enclose :: enjoy :: enlighten'
        >>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
        'pre :: preserve :: predispose :: preposition'
        >>> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
        'auto :: autodidactic :: autograph :: automate'
        >>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
        'inter :: intertwine :: interconnected :: interdependent'

    Args:
        vocab_words: of vocabulary words with prefix in first index.

    Returns:
        of prefix followed by vocabulary words with prefix applied.
    """
    return f' :: {vocab_words[0]}'.join(vocab_words)


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'
        >>> remove_suffix_ness('sadness')
        'sad'

    Args:
        word: of word to remove suffix from.

    Returns:
        of word with suffix removed & spelling adjusted.
    """
    if word[-5] == 'i':
        return f'{word[:-5]}y'
    return word[:-4]


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    Examples:
        >>> adjective_to_verb('I need to make that bright.', -1)
        'brighten'
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

    Args:
        sentence: that uses the word in sentence.
        index: index of the word to remove and transform.

    Returns:
        word that changes the extracted adjective to a verb.
    """
    return f'{sentence[:-1].split(" ")[index]}en'
