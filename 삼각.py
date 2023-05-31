def myfunction():   #함수선언
    for i1 in range(5, 0, -1):    # 5부터 1까지 1씩 작아지게 5줄
        for i2 in range(5-i1):    # 공백의 개수는 0부터 4까지
            print(' ', end='')
        for i3 in range(i1):    # 별의 개수는 5부터 1까지
            print('*', end='')
        print("") #줄바꿈

myfunction()    #함수호출
