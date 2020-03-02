cat1 = ['1','2','3','4']
cat2 = ['5','6','7','8']
cat3 = ['9','10','11','12']
cat4 = ['13','14','15','16']
cats = [cat1, cat2, cat3, cat4]

def dfs(cand, indx, size, cats, res):
    if len(cand) == size:
        res.append(cand[:])
        return;

    for cat in cats[indx]:
        cand.append(cat)
        dfs(cand, indx + 1, size, cats, res)
        cand.pop()

indx = 0;
res = []
for w in cats[indx]:
    cand = []
    cand.append(w)
    dfs(cand, indx + 1, len(cats), cats, res)

print(res);
