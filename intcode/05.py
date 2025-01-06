from input import I
import intcode

mem=intcode.load(I[0])

intcode.run(0,mem)

print(mem)
