# regex features

# non capturing group
# use for structure when later reference is not needed
In [421]: re.compile(r'(https?|ftp)://(?P<url>.*?)[.]').search("https://abc.com").groups()
Out[421]: ('https', 'abc')

In [422]: re.compile(r'(?:https?|ftp)://(?P<url>.*?)[.]').search("https://abc.com").groups()
Out[422]: ('abc',)

# reference named group which matched previously
In [404]: re.compile(r'function\s+(?P<fname>[_a-z]\w*)\s*;\s*begin\b(?P<content>.*?)\bend\s+(?P=fname)\s*;').match("function foo;begin end foo;")
Out[404]: <re.Match object; span=(0, 27), match='function foo;begin end foo;'>

# make assertions what is preceding and what is following
In [379]: re.compile(r'(?<!x)AND(?!y)').search("YANDY")
Out[379]: <re.Match object; span=(1, 4), match='AND'>

In [381]: re.compile(r'(?<=x)AND(?=y)').search("xANDy")
Out[381]: <re.Match object; span=(1, 4), match='AND'>

# select pattern depending on what group matched before
In [369]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|2)').search("2=2")
Out[369]: <re.Match object; span=(0, 3), match='2=2'>

In [370]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("2=2")
Out[370]: <re.Match object; span=(0, 3), match='2=2'>

In [371]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("2=3")
Out[371]: <re.Match object; span=(0, 3), match='2=3'>

In [372]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("1=3")

In [373]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("1=1")
Out[373]: <re.Match object; span=(0, 3), match='1=1'>

In [374]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("1=2")

In [375]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("3=2")

In [376]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("2=2")
Out[376]: <re.Match object; span=(0, 3), match='2=2'>

In [377]: re.compile(r'((?P<x>1)|(?P<y>2))=(?(x)1|\d)').search("2=1")
Out[377]: <re.Match object; span=(0, 3), match='2=1'>






