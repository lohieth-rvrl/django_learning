from operator import itemgetter
dic = {}
s = "swzrmtbttyyaymadobvwniwmozojggfbtsdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"
for i in range(len(s)):
    if(dic.get(s[i])):
        dic[s[i]] = dic[s[i]]+1
    else:
        dic[s[i]] = 1
# dic = dict(sorted(dic.items(), key=itemgetter(1,1), reverse=True))
dic = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])))
# dic = dict(sorted(dic.items()))
print(dic)
count = 0
# new_dic = {}
for i, j in dic.items():
    if(count == 3):
        break
    # new_dic[i] = j
    print(f"{i} {j}")
    count = count +1
# print(new_dic)
# # new_dic = dict(sorted(new_dic.items(), key=itemgetter(1), reverse=True))
# dic = dict(sorted(dic.items()))
# for i, j in new_dic.items():
#     print(f"{i} {j}")

def hello():
    print("hello")