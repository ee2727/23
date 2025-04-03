import random

start = 1
end = 100
ans= random.randint(start, end)

guess_count
while True :
    guess = input(f'請輸入你要猜的數字，介於｛start}與{end｝之間：'）

    try:
         guess = int（guess)
    except valueError:
         print('你輸入的不是一個數字'）
         continue
    if not (start <= guess<= end):
       print (　'你輸入的數字不在合法範圍中')
       continue
    
    if guess==ans:
       print('恭喜你答對了'）
       break
    
    if guess< ans
       start = guess+1
    else:
       end = guess -1
    if start == end:
        print(f'答案是｛ans}')
        break
        

    print('是合法的'）
    

 