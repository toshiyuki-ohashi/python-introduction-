l = {"1st": "マンドリン", "2nd": "マンドリン", "Dola": "マンドラ", "Cello": "マンドロンチェロ", "Guitar": "クラシックギター", "Bass": "コントラバス"}

for k, v in l.items():
    if k != 'Cello':
        continue;
    print (k+':'+v)