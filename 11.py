lst = list(map(int, input().split()))
command = input().strip()
direction = command[0]
shift = int(command[1:])
if len(lst) > 0:
    shift = shift % len(lst)
if shift > 0 and len(lst) > 0:
    if direction == 'R':
        lst = lst[-shift:] + lst[:-shift]
    elif direction == 'L':
        lst = lst[shift:] + lst[:shift]
print(lst)
