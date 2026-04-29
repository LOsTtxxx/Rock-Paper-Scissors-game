import random
game_over = False
choices = ["剪刀", "石頭" , "布"]

# 電腦、玩家計分
player_score = 0
computer_score = 0

# 輸入
while True:
    player_choices = input("請輸入: ")
    
    if player_choices == "結束":
        break
    
    if player_choices not in choices:
        print("輸入錯誤，請輸入 剪刀 / 石頭 / 布")
        continue

    computer = random.choice(choices)

    print(f"電腦出: {computer} ")

    if player_choices == computer:
        print("平手")

    elif (player_choices == "剪刀" and computer == "布") or \
         (player_choices == "布" and computer == "石頭") or \
         (player_choices == "石頭" and computer == "剪刀"):
        print("恭喜您贏了")
        player_score += 1      
    else:
        computer_score += 1
        print("您輸了")

    print(f"目前比分 您: {player_score} : 電腦: {computer_score}" )

    # 先拿下5分者獲勝
    if player_score == 5 or computer_score == 5:
        game_over = True
        break

if game_over:
    print("您已棄賽")
    if player_score > computer_score:
        print("恭喜您贏得比賽!")
    elif player_score < computer_score:
        print("非常可惜您輸了")
    else:
        print("本場遊戲平手")

    

    