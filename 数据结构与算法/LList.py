# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 3:47 PM
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : LList.py
# @Describe:
# @Software: PyCharm
from 数据结构与算法.LNode import LNode


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next_
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next_ is not None:
            p = p.next_
        p.next_ = LNode(elem)

    def pop_last(self):
        if self._head is None: #空表
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next_ is None: #只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next_.next_ is not None:
            p = p.next_
        e = p.next_.elem
        p.next_ = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next_

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next_ is not None:
                print(', ', end='')
            p = p.next_
        print('')

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next_

if __name__ == '__main__':
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()
