import time
import datetime
import os
import shutil
import config

time.sleep(1)
print('\n===== オートバックアップくんを起動します =====')
print('コピー元ディレクトリ：' + config.from_path)
print('コピー先ディレクトリ：' + config.to_path)

time.sleep(1)
print('\n===== プログラム実行日の日付を取得します =====')
dt_now = datetime.datetime.now()
print('現在日時 整形前：' + str(dt_now))
dt_now_fmt = dt_now.strftime('%Y%m%d')
print('現在日時 整形後：' + dt_now_fmt)

time.sleep(1)
print('\n===== バックアップを開始します =====')
# コピー元から当日作成分のデータを抽出して格納
for f in os.listdir(config.from_path):
    if dt_now_fmt in f:
        shutil.copy2(config.from_path + '/' + f, config.to_path)
        print('--- ' + f + ' をコピーしました ---')
        time.sleep(.5)
time.sleep(.5)
print('\n===== バックアップが完了しました =====')

time.sleep(1)
print('\n===== オートバックアップくんを終了します =====')