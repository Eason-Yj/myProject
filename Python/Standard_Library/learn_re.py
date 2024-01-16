import re

pattern = "adfasdfasfdasfd"
re.compile(pattern, flags=1)
'''
pattern：正则模型
falgs ：匹配模式,比如忽略大小写，多行模式等
返回值: Pattern 对象
'''


def findall_exp():
    exclude = ['jpg', 'azw3', 'epub', 'mobi', 'pdf', 'docx']

    match = ""

    for i in exclude:
        match += ".{}$|".format(i)
    match = match.strip("|")  # .jpg$|.azw3$|.epub$|.mobi$|.pdf$|.docx$

    print(re.compile(match).findall("fdasdfasdfadsf__asfd1.jpg"))
    print(re.compile(match).findall("fdasdfasdfa.md__asfd1.epub"))
    print(re.compile(match).findall("fdadfasdfa.pdf__asfd1.pdf"))


def groupdict():
    # 分组查询 (?P<province>\d{3})
    s1 = '1102231990xxxxxxxx'
    res1 = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s1)
    print(res1.groupdict())

    s2 = 'bdscddbcdabbbscndnnndcadnnbdae=-1.13-0=am'
    res2 = re.search('^b.*c$', s2)
    res2 = re.search('^d.*d$', s2)
    res2 = re.search('^=.*=$', s2)
    res2 = re.search('(?P<province>^b.*c$)(?P<city>^d.*d$)(?P<born_year>^=.*=$)', s2)
    print(res2.groupdict())


groupdict()
