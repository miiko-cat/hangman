import random

def hangman(word):
    y_str = word[random.randint(0, len(word) - 1)]
    wrong = 0
    stages = ["",
              "_________         ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              "|       / \       ",
              "|                 "
              ]
    rletters = list(y_str)
    board = ["_"] * len(y_str)
    win = False
    print("ハングマンへようこそ!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:]))
        print("あなたの負け!正解は{}".format(y_str))
        

form = ["google", "apple", "windows"]

hangman(form)
