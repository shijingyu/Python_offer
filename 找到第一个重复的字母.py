def firstDoubleStr(s):
    result = 'abcdefghijklmnopqrstuvwxyz'
    new_list =  [s.index(i) for i in result if s.count(i) >=2]
    return min(new_list) if len(new_list) >0 else -1