from input import I
import intcode

mem=intcode.load(I[0])
mem[1]=12
mem[2]=2

intcode.run(0,mem)

#print(mem)
print('A:', mem[0])

for noun in range(100):
  for verb in range(100):
    mem=intcode.load(I[0])
    mem[1]=noun
    mem[2]=verb
    intcode.run(0,mem)
    print(noun,verb,mem[0])
    if mem[0]==19690720: break
  if mem[0]==19690720: break

print('B:', 100*noun+verb)
