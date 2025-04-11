key = str(input())
code = str(input())
key_len, code_len = len(key), len(code)
ck_len = code_len // key_len
sort_key = sorted(key)
visited = [False] * key_len
code_pattern, res = [], []
for i in range(0, code_len, ck_len):
    code_pattern.append([sort_key[i//ck_len], code[i:i+ck_len]])
for k in key:
    for i in range(key_len):
        if code_pattern[i][0] == k and not visited[i]:
            visited[i] = True
            res.append(code_pattern[i][1])
            break
for i in range(ck_len):
    for j in range(key_len):
        print(res[j][i], end='')
