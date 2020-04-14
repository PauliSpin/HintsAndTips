import re
phone_text = """
(748) 328-7711
(435) 601-8233
null
(272) 339-6320

(633) 404-1943
not a number
(761) 870-4352
(890) 166-3349
+44 7070123456
"""

phone_numbers = [
    '(748) 328-7711',
    '(435) 601-8233',
    'null',
    '(272) 339-6320',
    '',
    '(633) 404-1943',
    'not a number',
    '(761) 870-4352',
    '(890) 166-3349',
    '+44 7070123456'
]

print('Match: ')
for ph in phone_numbers:
    if re.match(r'\(\d{3}\)', ph):
        print(ph)

print()
print('Search:')
res = re.search(r'\(761\) 870-4352', phone_text)
span = res.span()                       # tuple recording the start and
# end position of the match found in the string
print(span)                             # prints (80, 94)
# Print the phone_text string from position
print(phone_text[span[0]:span[1]])
# 80 to 94
