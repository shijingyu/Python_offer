# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 3:16 PM
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : LNode.py
# @Describe:
# @Software: PyCharm

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


if __name__ == '__main__':
    llist1 = LNode(1)
    p = llist1

    for i in range(2, 11):
        p.next_ = LNode(i)
        p = p.next_

    p = llist1
    while p:
        print(p.elem)
        p = p.next_
