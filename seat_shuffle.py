"""
席替えアプリ
・members.txt というファイルに参加者の名前が格納されている
・これを利用してランダムにテーブルを割り振るアプリを実装してください

ちなみに！
・Table1 は 6人
・Table2 は 5人
・Table3 は 4人

こんな感じになれば良い！
Table1: 横川 中川 鹿糠 美香子 大江 内田
Table2: 吉田 則也 中俣 川合 三村
Table3: 高橋 工藤 松本 杉村

[x] members.txt から全員の名前を取得して表示する
    - [X] members.txt から全員の名前を取得して random に 表示する

[x] Table1 に 全員入れる
    - [x] Table1 に 6人 あとは Table2 にいれる
    - [x] Table2 に 5人 あとは Table3 にいれる

[x] Table を 全て print する

"""

import random


def main():
    with open("members.txt", mode="r") as f:
        members_csv = ",".join(f.read().splitlines())

        members = random.sample(members_csv.split(","), 15)

        # 15回繰り返す
        # members から 名前を取ってくる
        # 名前を取ってきたら Table にいれる
        # Table1 は 6人
        # Table2 は 5人
        # Table3 は 4人

        table1 = []
        table2 = []
        table3 = []

        count = 0

        for member in members:

            count += 1

            if count <= 6:
                table1.append(member)
            elif count <= 11:
                table2.append(member)
            else:
                table3.append(member)

        table1_result = " ".join(table1)
        table2_result = " ".join(table2)
        table3_result = " ".join(table3)

        print(f"Table1: {table1_result}")
        print(f"Table2: {table2_result}")
        print(f"Table3: {table3_result}")

    f.closed


if __name__ == "__main__":
    main()
