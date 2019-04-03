"""
装饰器：在不改变原函数的情况下给函数增加功能
装饰器由闭包和语法糖组成
"""


def checkaccess(sg):
    def check():
        name = input('输入用户名')
        if name == 'zzy':
            sg()
        else:
            print('无权查看')
    return check


@checkaccess
def selectgoods():
    print('开始查询商品列表')


selectgoods()


