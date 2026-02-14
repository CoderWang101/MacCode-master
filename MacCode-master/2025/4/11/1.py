# n,m,l,r=map(int,input().split())
hash=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
hash_num=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print(len(hash_num))
# h_sz=len(hash)
# print(h_sz)
input_str=input()
input_str_sz=len(input_str)
#ord
for i in range(input_str_sz):
    hash_num[ord(input_str[i])-97]+=1
max_num=0
for i in range(26):
    if hash_num[i]>max_num:
        max_num=hash_num[i]

print(max_num)