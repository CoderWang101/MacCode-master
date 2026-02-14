grid = ['VLPWJVVNNZSWFGHSFRBCOIJTPYNEURPIGKQGPSXUGNELGRVZAG',
        'SDLLOVGRTWEYZKKXNKIRWGZWXWRHKXFASATDWZAPZRNHTNNGQF',
        'ZGUGXVQDQAEAHOQEADMWWXFBXECKAVIGPTKTTQFWSWPKRPSMGA',
        'BDGMGYHAOPPRRHKYZCMFZEDELCALTBSWNTAODXYVHQNDASUFRL',
        'YVYWQZUTEPFSFXLTZBMBQETXGXFUEBHGMJKBPNIHMYOELYZIKH',
        'ZYZHSLTCGNANNXTUJGBYKUOJMGOGRDPKEUGVHNZJZHDUNRERBU',
        'XFPTZKTPVQPJEMBHNTUBSMIYEGXNWQSBZMHMDRZZMJPZQTCWLR',
        'ZNXOKBITTPSHEXWHZXFLWEMPZTBVNKNYSHCIQRIKQHFRAYWOPG',
        'MHJKFYYBQSDPOVJICWWGGCOZSBGLSOXOFDAADZYEOBKDDTMQPA',
        'VIDPIGELBYMEVQLASLQRUKMXSEWGHRSFVXOMHSJWWXHIBCGVIF',
        'GWRFRFLHAMYWYZOIQODBIHHRIIMWJWJGYPFAHZZWJKRGOISUJC',
        'EKQKKPNEYCBWOQHTYFHHQZRLFNDOVXTWASSQWXKBIVTKTUIASK',
        'PEKNJFIVBKOZUEPPHIWLUBFUDWPIDRJKAZVJKPBRHCRMGNMFWW',
        'CGZAXHXPDELTACGUWBXWNNZNDQYYCIQRJCULIEBQBLLMJEUSZP',
        'RWHHQMBIJWTQPUFNAESPZHAQARNIDUCRYQAZMNVRVZUJOZUDGS',
        'PFGAYBDEECHUXFUZIKAXYDFWJNSAOPJYWUIEJSCORRBVQHCHMR',
        'JNVIPVEMQSHCCAXMWEFSYIGFPIXNIDXOTXTNBCHSHUZGKXFECL',
        'YZBAIIOTWLREPZISBGJLQDALKZUKEQMKLDIPXJEPENEIPWFDLP',
        'HBQKWJFLSEXVILKYPNSWUZLDCRTAYUUPEITQJEITZRQMMAQNLN',
        'DQDJGOWMBFKAIGWEAJOISPFPLULIWVVALLIIHBGEZLGRHRCKGF',
        'LXYPCVPNUKSWCCGXEYTEBAWRLWDWNHHNNNWQNIIBUCGUJYMRYW',
        'CZDKISKUSBPFHVGSAVJBDMNPSDKFRXVVPLVAQUGVUJEXSZFGFQ',
        'IYIJGISUANRAXTGQLAVFMQTICKQAHLEBGHAVOVVPEXIMLFWIYI',
        'ZIIFSOPCMAWCBPKWZBUQPQLGSNIBFADUUJJHPAIUVVNWNWKDZB',
        'HGTEEIISFGIUEUOWXVTPJDVACYQYFQUCXOXOSSMXLZDQESHXKP',
        'FEBZHJAGIFGXSMRDKGONGELOALLSYDVILRWAPXXBPOOSWZNEAS',
        'VJGMAOFLGYIFLJTEKDNIWHJAABCASFMAKIENSYIZZSLRSUIPCJ',
        'BMQGMPDRCPGWKTPLOTAINXZAAJWCPUJHPOUYWNWHZAKCDMZDSR',
        'RRARTVHZYYCEDXJQNQAINQVDJCZCZLCQWQQIKUYMYMOVMNCBVY',
        'ABTCRRUXVGYLZILFLOFYVWFFBZNFWDZOADRDCLIRFKBFBHMAXX', ]

# row=len(list)#行
# col=len(list[0])#列
# print(row)
# print(col)

# ans=0

# def large(m,n):
#     if m>n:
#         return m
#     else:
#         return n
    
# for i in range(row):
#     for j in range(col):
#         m=i#行
#         n=j#列
#         cur=0
#         pre=1#动态规划指针
#         length=0
#         for w in range(n,50):#从单行找
#             if ord(list[m][w])<=ord(list[m][w+1]):
#                 pre=pre+1
#                 length=length+1
#             else:
#                 if(length!=0):
#                     ans+=1
#                     cur=0,pre=1
#                     length=0
#         for w in range(n,30):#从单列找
#             if ord(list[w][n])<=ord(list[w+1][n]):
#                 pre=pre+1
#                 length=length+1
#             else:
#                 if(length!=0):
#                     ans+=1
#                     cur=0,pre=1
#                     length=0
                    
#         #对角线
#         for w in range(n,30):
#             if ord(list[m][w])<=ord(list[m+1][w+1]):
#                 pre=pre+1
#                 length=length+1
#             else:
#                 if(length!=0):
#                     ans+=1
#                     cur=0,pre=1
#                     length=0
                
ans = 0

for i in range(30):  # 行数
    for j in range(50):  # 列数
        current_char = grid[i][j]
        
        # 向右检查
        length = 1
        for k in range(j + 1, 50):
            if ord(grid[i][k-1]) < ord(grid[i][k]):
                length += 1
                if length >= 2:
                    ans += 1
            else:
                break  # 一旦不递增，立即终止
        
        # 向下检查
        length = 1
        for k in range(i + 1, 30):
            if ord(grid[k-1][j]) < ord(grid[k][j]):
                length += 1
                if length >= 2:
                    ans += 1
            else:
                break
        
        # 右下对角线检查
        length = 1
        step = 1
        while i + step < 30 and j + step < 50:
            if ord(grid[i + step - 1][j + step - 1]) < ord(grid[i + step][j + step]):
                length += 1
                if length >= 2:
                    ans += 1
                step += 1
            else:
                break

print(ans)

