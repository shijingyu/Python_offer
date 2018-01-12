def brackets_matched(brackets):
    if (len(brackets) % 2) > 0:
        return False
    dic = {'(':')', '[':']', '{':'}'}
    lists = []
    for i in brackets:
        if i in dic.keys():
            lists.append(dic[i])
        elif len(lists) > 0 and i == lists[-1]:
            lists.pop()
        else:
            return False
    return len(lists) == 0

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        result = input().strip()
        brackets = brackets_matched(result)
        print("YES") if brackets else print("NO")

 # 一个空list， 把键对应的值放到list里，检测和它匹配的值出现在list里即删除 代表匹配。
 
