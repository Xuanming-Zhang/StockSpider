import re

with open('tmp.html','r',encoding='utf-8') as fd:
    item = fd.read()
    # print(item)
    # print(re.findall(r'<img.*src="(.*?)"',item))
    # print(re.findall(r'<img.*src="(.*)" ', item))
    bd=re.findall(r'<p class="">(.*?)</p>',item,re.S)
    print(bd)
    bd=bd[0]
    print(bd)
    x= re.findall('<br/\s*>\s*',bd)
    print(x)
    bd = re.sub('<br/\s*>\s*',' ',bd)
    print(bd)