for y in range(1,11):
    for x in range(1,11):
        print(f'{x*y:4}',end='')
        if x==1:
            print(' |',end='')
    if y==1:
        print()
        print('-----+------------------------------------',end='')  
    print()  