import re

from bs4 import BeautifulSoup

file = open("example.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# https://cuiqingcai.com/1319.html


#转换成树状结构， 类似与lxml
# print(bs.title)
# print(bs.li)
# print(bs.head)

# 1.Tag 标签及其内容：第一个内容
# print(bs.title.string)
# print(bs.body.form.ul.li)
# print(type(bs.body.form.ul.li))

# 2. NavigableString 标签里的内容字典
# print(bs.body.form.attrs)
# print(type(bs.body.form.attrs))

# 3. BeautifulSoup 整个文档
# print(bs.name)
# print(bs)
# print(type(bs))

# 4. Comment 是一个特殊的 NavigableString，输出的内容仅含string，不含注释符号
# print(bs.a.string)
# print(type(bs.a.string))


#______________
#文档的遍历
# print(bs.head.contents)
# print(type(bs.head.contents))
# print(bs.head.contents[1])
# print(type(bs.head.contents[1]))

#文档的搜索
# 1.（1）find_all() 找到所有 li 节点
# print(bs.find_all("li"))

# (2) 正则表达式:使用search方法来匹配内容，找到所有包含 li 字符的节点
# t_list = bs.find_all(re.compile("li"))
# print(t_list)

# (3) 方法： 传入一个函数，根据函数的要求搜索
# def name_exists(tag):
#     return tag.has_attr("name")
# print(bs.find_all(name_exists))

# 2.kwargs 参数
# print(bs.find_all(type="email"))
# print(bs.find_all(class_=True)) #带class的节点及其所有子节点

# 3.text 参数
# t_list = bs.find_all(text=["标题呀","身体"])
# print(t_list)
#
# print(bs.find_all(text=re.compile('\d')))

# css 选择器
# print(bs.select('title'))
# print(bs.select('.aaa')) #class
# print(bs.select('#net')) #id
# print(bs.select('li')) #标签选择器
# print(bs.select('li[id="net"]')) #属性
# print(bs.select('head>title')) #子标签选择器
#
# print(bs.select('.aaa ~ #net')) #兄弟标签，先找class aaa再找 id net








file.close()



