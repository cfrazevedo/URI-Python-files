n = int(input())
m = int(input())
album = set()
for _ in range(m):
    album.add(int(input()))
print(n - len(album))