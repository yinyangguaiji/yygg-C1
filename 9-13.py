from collections import OrderedDict
terms = OrderedDict()
terms['append()'] = '向列表末尾添加一个元素'
terms['pop()'] = '弹出列表中的指定元素'
terms['remove()'] = '按值删除元素'
terms['lstrip()'] = '去除字符串开头的空白'
terms['strip()'] = '去除字符串两端的空白'
for term_name,term in terms.items():
    print(term_name + ':' + term)
    
