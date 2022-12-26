l = list(input())
# l = list("baaabbacddc")
o = []
for c in l:
    if len(o)>0:
        if c==o[-1]:
            del o[-1]
            continue
    o.append(c)
print("".join(o))