# What will this code do?

import re

s="https://github.com"

obj2 = re.findall('://www.([\w\-\.]+)', s)
print(obj2)