import random
game_over = False
choices = ["剪刀", "石頭" , "布"]

def judge(player , computer):
    if (player == "剪刀" and computer == "布") or \
       (player == "石頭" and computer == "剪刀") or \
       (player == "布" and computer == "石頭"):
        return "玩家贏"
    elif player == computer:
        return "平手"
    else:
        return "電腦贏"
    

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

    result = judge(player_choices , computer)

    if result == "玩家贏":
        print("此回合玩家勝利")
        player_score += 1
    elif result == "電腦贏":
        print("此回合電腦勝利")
        computer_score += 1
    else:
        print("平手")

    print(f"目前比分 您: {player_score} : 電腦: {computer_score}" )

    # 先拿下5分者獲勝
    if player_score == 5 or computer_score == 5:
        game_over = True
        break

if game_over:
    if player_score > computer_score:
        print("恭喜您贏得比賽!")
    elif player_score < computer_score:
        print("非常可惜您輸了")
    else:
        print("本場遊戲平手")

    

    