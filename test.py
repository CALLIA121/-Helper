q = int(input())
box = []
for i in range(q):
    cmd = input().strip().split()
    if cmd[0] == "push":
        box.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        box.pop()
    elif cmd[0] == 'max':
        print(max(box))
