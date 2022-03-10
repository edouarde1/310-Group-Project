from spellchecker import SpellChecker
spell = SpellChecker()

def spell_check(string):
    """takes a string and returns a list substring of corrected words"""
    err = string.split()
    correct = []
    for word in err:
        word = spell.correction(word)
        correct.append(spell.correction(word))
    return correct;

spell_check("Let us wlak on the groun")