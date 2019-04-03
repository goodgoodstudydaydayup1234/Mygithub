"""
装饰器补充
"""


def checkuser(fun):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    def check(*args):
        name = input('用户名')
        if name == 'xcy':
            fun(*args)
        else:
            print('无权限')
    return check


# @checkuser
def showlist():
    for i in range(10):
        print(i)





# @checkuser
def showdetail(num):
    print('当前页', num)


# @checkuser
def showmany():
    print('钱')


# result = checkuser(showlist)
# result()


showlist = checkuser(showlist)
showlist()

# showlist()
# showdetail(10)
