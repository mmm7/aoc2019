from input import I

from itertools import islice

#    80871224585914546619083218645595 becomes 24176176.
#    19617804207202209144916044189917 becomes 73745418.
#    69317163492948606335995924319873 becomes 52432133.


def pattern(i,pat=(0,1,0,-1)):
  assert i>0
  while True:
    for p in pat:
      for ii in range(i):
        yield p

ttt=list(islice(pattern(1),9))
assert ttt == [0, 1, 0, -1,0,1,0,-1,0], ttt
ttt=list(islice(pattern(2),9))
assert ttt == [0, 0, 1, 1, 0, 0, -1,-1, 0], ttt
ttt=list(islice(pattern(1),1,9))
assert ttt == [1, 0, -1,0,1,0,-1,0], ttt

""" Apply pattern `p` on number `n`.
"""
def apply(n,p):
  s=0
  for nn,pp in zip(n,islice(p,1,len(n)+1)):
    #print(nn,pp)
    s += int(nn) * int(pp)
  return str(s)[-1]

ttt=apply('000', [1,2,3,4,5])
assert ttt=='0',ttt
ttt=apply('100', [1,2,3,4,5])
assert ttt=='2',ttt
ttt=apply('101', [1,2,3,4,5])
assert ttt=='6',ttt
ttt=apply('100', [1,-2,3,4,5])
assert ttt=='2',ttt

def iterate(n,step=1):
  for xx in range(step):
    print(xx)
    s=[]
    for i in range(len(n)):
      s.append(apply(n,pattern(i+1)))
    n=''.join(s)
  return n

ttt=iterate('12345678')
assert ttt=='48226158',ttt
ttt=iterate('48226158')
assert ttt=='34040438',ttt
ttt=iterate('34040438')
assert ttt=='03415518',ttt
ttt=iterate('03415518')
assert ttt=='01029498',ttt

ttt=iterate('12345678',4)
assert ttt=='01029498',ttt

ttt=iterate('80871224585914546619083218645595',100)
print(ttt)
assert ttt.startswith('24176176'),ttt

ttt=iterate('19617804207202209144916044189917',100)
print(ttt)
assert ttt.startswith('73745418'),ttt

for i in I:
  print(i)
  print(iterate(i,100))

# 94960436704993974372749486740689469965560349027332039364452245445306935215363055748697286434965127245264852756726099891748052551466152630537735720850849835637559827978519230220802672557250955852237871975350386268257875100487841070858957667586616370722657705465015547073976538323065868876943006290435697816423487493183232719077172568571705902936366423522834094950771893985899566847409037313469627238963412319079395511339731517454714784068241269096557552152475169502355478797812587653465940016086953622580313770996227198296599895417692704142060137709403119390589017075113133107829733916539184250777830227223101499962232095411499689702675521916160855397
