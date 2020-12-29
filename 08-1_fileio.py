### practice
# 演習１：ファイルを読み込んで、読み込んだ内容に何か追記してファイルに書き込んでみよう！
# ファイル読み込み
path_p = 'tmp/practice.txt'
str_practice = ''
with open(path_p) as f:
    str_practice = f.read()
    print(str_practice)

# 文字列を追記
str_practice = str_practice + 'fgh'

# ファイル書き込み
with open(path_p, mode='w') as f:
    f.write(str_practice)

# 確認
with open(path_p) as f:
    str_practice = f.read()
    print(str_practice)