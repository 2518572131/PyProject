#多层循环中，break代表内层循环结束，不影响外层循环
#continue代表这个循环结束，从开始本层循环


for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()