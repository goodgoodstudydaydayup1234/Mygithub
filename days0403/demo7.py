"""
垃圾回收-分代收集
    对象刚被创建时，代数为0
    每执行标记清除后，存活的对象代数+1
    存活越久，代数越高
    进行标记删除的间隔【阀值】就越长
"""
