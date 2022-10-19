###################  ESCAPE SEQUENCES  ###################

# A string is a chain of caracters ( letters )
#  Regular string escape sequence
# when using the same quotes within
# a string assignment (value):
# you would end up by closing the pair of quotes.
# This is where escape sequences take place

# escape sequence: anti-slack "\"
antislash_escape_sequence ='It\'s amazing'
print('\n1. ESCAPE SEQUENCE - ANTI SLASH \\:\n \'It\\\'s amazing\': the antislash \\ is escaping the \' caracter;\n  Result:', antislash_escape_sequence)

# escape sequence: \n
new_line_escape_sequence = 'It\'s amazing\n    New line'
print('\n\n\n2. ESCAPE SEQUENCE - NEW LINE \\n:\n"It\\\'s amazing\\n New line":  the new line escape returning \nthe left side to a new line:\n  Result:\n   ', new_line_escape_sequence )

# escape sequence: \n
tab_escape_sequence = 'It\'s amazing\n    New line \n\t Indented with \\t'
print('\n\n\n2. ESCAPE SEQUENCE - TAB \\t:\n"It\\\'s amazing\\n New line \\t Indented with \\t":  the new line escape returning \nthe left side to a new line:\n  Result:\n   ', tab_escape_sequence )