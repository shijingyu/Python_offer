def maopao_sort(lists):
    ll = len(lists)
    for i in range(ll):
        for j in range(i+1,ll):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

if __name__ == '__main__':
    lists=[-2,2,4,-2,-2,-1,4,6]
    print (maopao_sort(lists))