#TODO task1
import re

email = [
    "user1@example.com",
    "user2@gmail.com",
    "user3@yahoo.com",
    "user4@hotmail.com"
]

domain_pattern = r'@([a-zA-Z0-9.-]+)'

domains = [re.search(domain_pattern, i).group(1) for i in email]

print(domains)

#task2
import re

text = "basketball, football, mouse, animal, award, cup"

vowel_re = r'\b[aeiouAEIOU][a-zA-Z]*\b'

vowel_words = re.findall(vowel_re, text)

print(vowel_words)
#task3
import re

text = "basketball:football-mouse,animal/award]cup"

split_pattern = r'[,;|\-]'

split_parts = re.split(split_pattern, text)

print(split_parts)
