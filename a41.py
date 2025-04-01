import random

start = 1
end = 100
ans= random.randint(start, end)

while True :
    guess = input(f'請輸入你要猜的數字，介於｛start}與{end｝之間：'）

    try:
         guess = int（guess)
    except valueError:
         print('你輸入的不是一個數字'）
         continue
        
    print('是合法的'）
    

 