from collections import defaultdict

def _getop(mem,pc,mode,num):
  op = mem[pc+num]
  if mode[num]: return op
  return mem[op]

def _getops(mem,pc,mode,num):
  ops = []
  for n in range(num):
    ops.append(_getop(mem,pc,mode,n+1))
  if num==1: return ops[0]
  return tuple(ops)

def step(pc,mem,input,output):
  instr = mem[pc]%100
  mode=[0]
  modev = mem[pc]//100
  while modev:
    mode.append(modev%10)
    modev//=10
  mode+=[0,0,0,0,0]

  if instr==99:  # HALT
    return None
  if instr==1:  # ADD
    op1,op2=_getops(mem,pc,mode,2)
    assert not mode[3]
    mem[mem[pc+3]]=op1 + op2
    return pc+4
  if instr==2:  # MUL
    op1,op2=_getops(mem,pc,mode,2)
    assert not mode[3]
    mem[mem[pc+3]]=op1 * op2
    return pc+4
  if instr==3:  # IN
    assert not mode[1]
    mem[mem[pc+1]] = input.popleft()
    return pc+2
  if instr==4:  # OUT
    op1=_getops(mem,pc,mode,1)
    output.append(op1)
    return pc+2
  if instr==5:  # jump-if-true
    op1,op2=_getops(mem,pc,mode,2)
    if op1!=0: return op2
    return pc+3
  if instr==6:  # jump-if-false
    op1,op2=_getops(mem,pc,mode,2)
    if op1==0: return op2
    return pc+3
  if instr==7:  # less-than
    op1,op2=_getops(mem,pc,mode,2)
    assert not mode[3]
    mem[mem[pc+3]]=(0,1)[op1<op2]
    return pc+4
  if instr==8:  # equals
    op1,op2=_getops(mem,pc,mode,2)
    assert not mode[3]
    mem[mem[pc+3]]=(0,1)[op1==op2]
    return pc+4

  raise ValueError(f'unknown instruction at {pc=} : {mem[pc]=}')

def run(pc,mem,input=None,output=None):
  while True:
    pc = step(pc,mem,input,output)
    if pc == None: break
  return pc

def load(p):
  mem=defaultdict(int)
  for i,v in enumerate(p):
    mem[i]=v
  return mem

