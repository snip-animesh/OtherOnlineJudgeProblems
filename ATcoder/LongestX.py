# It's might be sliding window technique. but it's easy . I don't know if my solution follow sliding window technique or not but it takes less time than others .


s=input()
k=int(input())
res, cnt, left, right= 0, 0, 0, 0
while right<len(s):
    if s[right] != "." and cnt <= k:
#       এখানে cnt<=k হওয়ার কারন হল , s[right] যেহেতু . না , তাই cnt এর মান k এর সমান হলেও সেটা রেজাল্ট এ ইনক্লুডেড । 
# XX...X.X.X. 
# এটা এনালাইসিস করলেই ক্লিয়ার হবে । 
        res=max(res, right - left + 1)
        right+=1
    elif s[right] == "." and cnt < k:
        cnt+=1
        res = max(res, right - left + 1)
        right+=1
    else:
        if s[left]== ".":
            cnt-=1
        left+=1
print(res)


# problem - https://atcoder.jp/contests/abc229/tasks/abc229_d
