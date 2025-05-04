n = int(input())

found = False
# 2kg 봉지 개수 (0개 부터 하나씩 늘려가기)
for i in range(n // 2 + 1):
    # n에서 2kg * i 빼고 5kg 나눈 나머지가 0이면 완벽한 조합임

    if (n - 2 * i) % 5 == 0:

        # i는 2kg 개수
        # (n - 2 * i) -> 2kg i개 쓰고 남은 무게
        # (n - 2 * i) // 5 -> 남은 무게를 5kg 나눈 개수
        # i + (n - 2 * i) // 5 -> 총 봉지수수
        print(i + (n - 2 * i) // 5)
        
        # 가능한 조합이니 True 할당 후 탈출
        found = True
        break

# 조합을 못 찾았다 그럼 -1 출력력
if not found:
    print(-1)