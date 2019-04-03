"""
自定义元类
"""
def renameattr(classname, parentclass, attrs):
    print('通过原方法重新定义类')
    # print(classname)
    # print(parentclass)
    # print(attrs)
    # print(classname.lower()[0]+"_")
    newattrs = {}
    for k, v in attrs.items():
        # print(k,v)
        if not k.startswith('__'):
            k = classname.lower()[0]+"_" + k
            newattrs[k] = v
    print(newattrs)
    return type(classname, parentclass, newattrs)


class Good(metaclass=renameattr):
    id = None
    name = None


print(hasattr(Good, 'id'))
print(hasattr(Good, 'g_id'))
g = Good()
print(g.__dir__())
print(hasattr(g, 'g_id'))
print(hasattr(g, 'g_name'))
