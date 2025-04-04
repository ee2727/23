import random
def play():
start = 1
end = 100
ans= random.randint(start, end)

guess_count = 0
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
        
    guess_count += 1
    
    if guess==ans:
         print('恭喜你答對了'）
         break
    
    if guess< ans
         start = guess+1
    else:
         end = guess -1
    if start == end:
         print(f'答案是｛ans}')
         guess_count += 1
         break
        

    print(f'你花了{guess_count}次猜到正確答案'）
    


while True:
    play()
    
    again = input('你是否要再玩一次？請輸入Y繼續遊戲:')
    if again.upoer() != 'Y':
        break 
 