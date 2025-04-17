import sys
from collections import Counter
data_in = sys.stdin.readline
N = int(data_in())
res = [0] * 4
nums = sorted(int(data_in()) for _ in range(N))
res[0] = round(sum(nums) / N)
res[1] = nums[N//2]
nums_cnt = Counter(nums).most_common()
nums_most_arr = [v for v, c in nums_cnt if c == nums_cnt[0][1]]
nums_most_arr.sort()
res[2] = nums_most_arr[1] if len(nums_most_arr) > 1 else nums_most_arr[0]
res[3] = max(nums) - min(nums)
for r in res:
    print(r)
