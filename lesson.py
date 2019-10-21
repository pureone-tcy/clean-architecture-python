import string

s = """\

Hi $name.

$contents

Have a good time
"""

t = string.Template(s)

with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
