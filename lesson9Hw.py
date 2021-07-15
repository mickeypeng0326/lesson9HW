查詢貨號=1
離開系統=2

dictionary={'A001':'小熊軟糖  20','A002':'冰棒  25','A004':'王子麵  10','A006':'汽水  30'}


print('=======功能選單=======')
print('查詢貨號 1')
print('離開系統 2')
print('=====================')
t=int(input('請選擇功能:'))


while 0<t<2:
    if t==1:
        貨號=input('請輸入貨號:')
        x=貨號 in dictionary
        if x==True:
            v=dictionary[貨號]
            print('')
            print('商品:',v,'元')
        if x==False:
            k=貨號
            價錢=0
            print('')
            print('您查詢的物品不存在')
            商品=input('請輸入新商品名稱:')
            價錢=int(input('請輸入新商品價錢:'))
            print('')
            dictionary[k]=商品+'  '+str(價錢)
            print(dictionary)
    print('=======功能選單=======')
    print('查詢貨號 1')
    print('離開系統 2')
    print('=====================')
    t=int(input('請選擇功能:'))
