from collections import deque,defaultdict

from input import I
import intcode

I = I[0]

maze={
  (0,0): '.',
}

def printmaze(maze,droidy,droidx):
  yyy=[y for y,_ in maze]
  xxx=[x for _,x in maze]
  for y in range(min(yyy),max(yyy)+1):
    l=[]
    for x in range(min(xxx),max(xxx)+1):
      if (y,x) not in maze:
        l.append(' ')
        continue
      if y==droidy and x==droidx:
        l.append('D')
        continue
      l.append(maze[(y,x)])
    print(''.join(l))

mem=intcode.load(I)
pc=0

def run_with_input(i):
  global pc,mem
  input=deque([i])
  output=[]
  pc=intcode.run_until_next_output(pc,mem,input,output)
  assert len(output)==1, output
  return pc, output[0]

def attempt(y,x,there,back):
  global pc,maze
  if (y,x) in maze: return
  pc,output=run_with_input(there)
  assert output in (0,1,2)
  if output == 0:
    maze[(y,x)]='#'
    return
  maze[(y,x)]='.O'[output==2]
  explore(y,x)
  pc,output=run_with_input(back)
  assert output in (1,2)

# north (1), south (2), west (3), and east (4)

def explore(y,x):
  attempt(y-1,x,1,2)
  attempt(y+1,x,2,1)
  attempt(y,x-1,3,4)
  attempt(y,x+1,4,3)

explore(0,0)
printmaze(maze,0,0)

"""
 ####### ############# ############# ### 
#.......#.............#.............#...#
#.#####.#.#.#.#######.#.#.#########.###.#
#O#.....#.#.#.#.....#.#.#.#.......#...#.#
 ##.###.#.#.###.###.###.#.#.###.#####.#.#
#...#...#.#...#.#.#.....#.#.#.#.......#.#
#.#######.###.#.#.#######.#.#.#########.#
#.#.......#.#.#...#.....#.#.#...#.......#
#.#.#######.#.###.#.###.#.#.#.#.#####.#.#
#.#.........#.....#...#...#...#.....#.#.#
#.#.#######.#########.#### ########.###.#
#...#...#.#.#.......#.#...#.......#...#.#
 ####.#.#.#.#.###.###.#.###.###.#####.#.#
#.....#.#.....#...#...#.......#.....#...#
#.#####.###### ####.###.#######.#.#####.#
#.#...#.......#...#...#.#.....#.#.....#.#
#.###.#######.#.#.#.#.###.###.#####.###.#
#...........#...#.#.#.....#...#.....#...#
 ##########.#####.#.#######.###.#####.## 
#.....#.#...#...#.#...#.....#.#.....#.#.#
#.###.#.#.#####.#.#####.#####.#.###.#.#.#
#.#.....#.......#.#..D#.....#...#.#...#.#
#.#####.#######.#.#.###.###.#.###.#####.#
#...#...#.....#.#...#...#...#...#...#...#
#.#.#.###.###.#.#########.#####.###.#.#.#
#.#.#.#...#...#.#.....#...#...#...#...#.#
#.#.#.#####.###.###.#.#.###.#.###.###.#.#
#.#.#.....#.#...#...#...#...#...#...#.#.#
#.#.#####.#.#.###.## ####.## ##.###.###.#
#.#.#...#.#.#.#...#.#.......#.....#...#.#
#.#.#.###.#.#.###.#.#.#######.###.###.#.#
#.#.#.....#.#.....#.......#...#.....#.#.#
 ##.#.#####.###########.###.###.#####.#.#
#...#.#.....#.........#.#...#.#...#...#.#
#.###.#.###.#.#######.###.###.#.###.###.#
#.#.....#.....#...#.......#...#.#...#...#
#.#.#### ####.#.#.#####.#####.#.#.###.#.#
#.#.#...#...#.#.#.....#.#...#...#.....#.#
#.###.#.#.#.###.#####.###.#.###########.#
#.....#...#.........#.....#.............#
 ##### ### ######### ##### ############# 
"""

vis=set()
bfs=deque([(0,(0,0))])

while bfs:
  n,pos = bfs.popleft()
  if pos in vis: continue
  vis.add(pos)
  if maze[pos]=='#': continue
  if maze[pos]=='O': break
  bfs.append((n+1,(pos[0]-1,pos[1])))
  bfs.append((n+1,(pos[0]+1,pos[1])))
  bfs.append((n+1,(pos[0],pos[1]-1)))
  bfs.append((n+1,(pos[0],pos[1]+1)))

print('A:',n,pos)

vis=set()
bfs=deque([(0,pos)])
highest=0

while bfs:
  n,pos = bfs.popleft()
  if pos in vis: continue
  vis.add(pos)
  if maze[pos]=='#': continue
  highest=n
  bfs.append((n+1,(pos[0]-1,pos[1])))
  bfs.append((n+1,(pos[0]+1,pos[1])))
  bfs.append((n+1,(pos[0],pos[1]-1)))
  bfs.append((n+1,(pos[0],pos[1]+1)))

print('B:',highest)
