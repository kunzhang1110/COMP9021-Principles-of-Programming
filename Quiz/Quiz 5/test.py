import re
DATA = "Hey, you - what are you doing here!?"
print(re.findall(r"[\w\s]+", DATA))