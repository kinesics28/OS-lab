# Best fit allocation

n,m = map(int, input('Enter number of blocks and processes: ').split())

block_size = []
process_size = []
allocated = [0]*m
block = []

print()

for x in range(1,n+1):
    print('Enter size of',x, end = ' ')
    b = int(input('block: '))
    block_size.append([b,x])
    block.append(b)

print()

for y in range(1,m+1):
    print('Enter size of',y, end = ' ')
    p = int(input('process: '))
    process_size.append([p,y])

block_size.sort()
block.sort()

for i in range(m):
    for j in range(n):
        if process_size[i][0] <= block_size[j][0]:
            block_size[j][0] = block_size[j][0] - process_size[i][0]
            allocated[i] = allocated[i] + 1
            print('\nProcess',process_size[i][1],'of size',process_size[i][0],'is allocated in',block_size[j][1],'block and space remaining',block_size[j][0])
            break

for a in range(m):
    if allocated[a] == 0:
        print('\nProcess',a+1,'is not allocated.')

external_frag = 0

for b in range(n):
    if block_size[b][0] != block[b]:
        external_frag = external_frag + block_size[b][0]
    
print('\nExternal fragmentation is:',external_frag)

