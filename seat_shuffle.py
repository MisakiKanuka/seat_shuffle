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
    - [ ] members.txt から全員の名前を取得して random に 表示する

[ ] Table1 に 全員入れる
    - [ ] Table1 に 6人 あとは Table2 にいれる
    - [ ] Table2 に 5人 あとは Table3 にいれる

[ ] Table を 全て print する

"""


def main():
    with open("members.txt", mode="r") as f:
        members_list = f.read()
        print(members_list)

        members_csv = ",".join(members_list.splitlines())
        print(members_csv)

        members = members_csv.split(",")
        print(members)

    # random.choice(('xxx', 'yyy', 'zzz'))

    print(f.closed)


if __name__ == "__main__":
    main()
