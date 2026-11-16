#НА ОДНОЙ СТРОКЕ С РАЗДЕЛИТЕЛЕМ
nums = list(map(int, input().split()))
#
nums = [int(x) for x in input().split()]



#КАЖДОЕ ЧИСЛО В НОВОЙ СТРОКЕ. ИЗВЕСТНО КОЛ-ВО
n = int(input())
nums = [int(input()) for _ in range(n)]
#
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))



#КАЖДОЕ ЧИСЛО В НОВОЙ СТРОКЕ. КОЛВО НЕ ЗАДАНО
#до спец слова для остановки
nums = []
while (line := input()) != 'СПЕЦ СЛОВО':
    nums.append(int(line))
