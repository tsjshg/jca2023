import random
import datetime as dt

# 今日の日付を取得
today = dt.datetime.today()
# シードを固定して同一の日は同じ結果が返るようにする
random.seed(today.toordinal())
# 今日の運勢を占う
todays_fortune = random.random()

if todays_fortune > 0.9:
    print("今日は、すごいラッキーな一日です。")
elif todays_fortune > 0.2:
    print("今日は普通の1日です。")
else:
    print("今日はとんでもない不運に見舞われます。")

print("よい1日を。")
