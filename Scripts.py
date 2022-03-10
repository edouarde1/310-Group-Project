from spellchecker import SpellChecker

def spell_check(str_input):
    """Returns a list of spellchecked words """
    str_input = str_input.split()
    for word in str_input:
        word = SpellChecker().correction(word)
    return str_input;