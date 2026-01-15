# 5. Use the re module to write a script that searches through a paragraph and extracts all
# words that start with an uppercase letter (e.g., "London", "Python") to identify proper
# nouns or sentence starters.

import re

paragraph="London is the capital of England,in England, Python is popular language"
search=r'[A-Z][a-z]*'
result=re.findall(search,paragraph)
print("Words that start with an uppercase letter:",result)