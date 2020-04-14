import re

phone_text = """
(748) 328-7711
(435) 601-8233
(272) 339-6320
(633) 404-1943
(761) 870-4352
(890) 166-3349
"""

# str.replace
print('With String Replace:')
alt_phone_text = phone_text.replace('(', '').replace(') ', '').replace('-', '')
print(alt_phone_text)

# re.sub
print('With re.sub:')
sub_phone_text = re.sub(r'[^\d\n]', '', phone_text)
# r specifies a raw string
print(sub_phone_text)
