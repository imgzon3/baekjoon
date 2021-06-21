x, y, w, h = map(int, input().split())
tmp = [abs(x), abs(w-x), abs(y), abs(h-y)]
print(min(tmp))