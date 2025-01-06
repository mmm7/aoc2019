from collections import defaultdict

def step(pc,mem):
  instr = mem[pc]
  if instr==99:  # HALT
    return None
  if instr==1:  # ADD
    mem[mem[pc+3]]=mem[mem[pc+1]] + mem[mem[pc+2]]
    return pc+4
  if instr==2:  # MUL
    mem[mem[pc+3]]=mem[mem[pc+1]] * mem[mem[pc+2]]
    return pc+4
  raise ValueError(f'unknown instruction at {pc=} : {mem[pc]=}')

def run(pc,mem):
  while True:
    pc = step(pc,mem)
    if pc == None: break
  return pc

def load(p):
  mem=defaultdict(int)
  for i,v in enumerate(p):
    mem[i]=v
  return mem

