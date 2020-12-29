# 1
kokugo = 80
sugaku = 80
# # 2
# kokugo = 20
# sugaku = 20
# # 3
# kokugo = 80
# sugaku = 79
# # 4
# kokugo = 79
# sugaku = 80
# # 5
# kokugo = 60
# sugaku = 70

if kokugo >= 80 and sugaku >= 80:
    print ('君天才！')
elif kokugo <= 20 and sugaku <= 20:
    print ('君！ちゃんと勉強しなさい！')
elif kokugo >= 80 and sugaku <= 79:
    print ('君国語できるね！')
elif kokugo <= 79 and sugaku >= 80:
    print ('君数学できるね！')
else:
    print('君普通だね！')