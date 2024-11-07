import tkinter as tk
import random
import hashlib

hash_list = []  

def generate():
    card = []
    for i in range(5):
        tate = random.sample(range(i * 15 + 1, i * 15 + 16), 5)
        card.append(tate)
    card[2][2] = "FREE"  
    return card

#ビンゴカードの内容をSTRにしてハッシュ値に変換
def hash_card(card):
    card_str = ""
    for n in card:
        for x in n:
            if card_str != "":  
                card_str += ","
            card_str += str(x)

    return hashlib.md5(card_str.encode()).hexdigest()

#カードを生成してハッシュ値がかぶっていないかを確認し、かぶっていた場合再生成することにより重複を防ぐ
def check_hush():
    while True:
        card = generate()
        hash_num = hash_card(card)
        if hash_num not in hash_list:
            hash_list.append(hash_num)
            return card

#ボタンが押された場合に選択、非選択を切り替える
def select(btn):
    if btn['bg'] == "yellow":
        btn.config(bg="white")
    else:
        btn.config(bg="yellow")
    cheak_bingo()

#縦、横、斜めを背景色により選択、非選択を確認しリーチとビンゴを判定
def cheak_bingo():
    bingo = False
    reach = False

    for i in range(5):
        count = 0
        for j in range(5):
            if btn_cheak[i][j]['bg'] == "yellow":
                count += 1
        if count == 5:
            bingo = True
        elif count == 4:
            reach = True

    for i in range(5):
        count = 0
        for j in range(5):
            if btn_cheak[j][i]['bg'] == "yellow":
                count += 1
        if count == 5:
            bingo = True
        elif count == 4:
            reach = True

    count = 0
    for i in range(5):
        if btn_cheak[i][i]['bg'] == "yellow":
            count += 1
        if count == 5:
            bingo = True
        elif count == 4:
            reach = True

    count = 0
    for i in range(5):
        if btn_cheak[i][4-i]['bg'] == "yellow":
            count += 1
        if count == 5:
            bingo = True
        elif count == 4:
            reach = True
        

    if bingo:
        bingo_message.config(text="ビンゴ")
    elif reach:
        bingo_message.config(text="リーチ")
    else:
        bingo_message.config(text="")

# ウィンドウ設定
root = tk.Tk()
root.title("ビンゴカード生成システム")

# ウィジェット
bingo_message = tk.Label(root, text="", font=("Helvetica", 16), fg="red")
bingo_message.pack(pady=10)
btn_cheak = []
bingo_card = check_hush()

card_frame = tk.Frame(root)
card_frame.pack()

for yoko in range(5):
    btn_tate = []
    for tate in range(5):
        btn = tk.Button(card_frame, text=str(bingo_card[tate][yoko]), width=6, height=3)
        btn.config(command=lambda n=btn: select(n))
        btn.grid(row=yoko, column=tate)
        btn_tate.append(btn)
    btn_cheak.append(btn_tate)

root.mainloop()
