n=int(input())
liste=[int(i) for i in input().split()]
liste.sort()
print(" ".join([str(c) for c in liste]))