res=0
for x in range(146810,612564+1):
  s=list(map(int,str(x)))
  good = False
  for i in range(len(s)-1):
    if s[i]>s[i+1]:
      good=False
      break
    if s[i]==s[i+1]: good=True
  if good: res+=1

print('A:',res)

#########################

res=0
for x in range(146810,612564+1):
  s=list(map(int,str(x)))
  s.append(-9999)
  good = False
  for i in range(len(s)-2):
    if s[i]>s[i+1]:
      good=False
      break
    if s[i]==s[i+1] and s[i-1]!=s[i] and s[i+1]!=s[i+2]: good=True
  if good: res+=1

print('B:',res)
