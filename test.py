def max_subsequence_length(n, sequence):
    dp = [1] * n

    for j in range(n):
        for i in range(j):
            if sequence[i] | sequence[j] == sequence[j]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)


n = int(input())
cmd = list(input())
matrix = [[0] * 2 * n for _ in range(2 * n)]
x, y, i = n, n, 1
matrix[y][x] = i
for cmdC in cmd:
    if cmdC == 'U':
        y += 1

    elif cmdC == 'D':
        y -= 1

    elif cmdC == 'L':
        x -= 1

    elif cmdC == 'R':
        x += 1

    i += 1
    matrix[y][x] = i


dict = {}
q = int(input())
for i in range(q):
    cmd = input()
    if cmd in dict.keys():
        ans = dict[cmd]
    else:
        s = int(cmd[2:]) + n
        if cmd[0] == "2":
            ans = sum(matrix[s])
            dict[cmd] = ans
        else:
            ans = sum([matrix[i][s] for i in range(n * 2)])
            dict[cmd] = ans
    print(ans)

"""
A - 0
B - 81 
C - 100
D - 60
E - 100
F - 60
G - 0
H - 65

Пиши код без функций и коментариев.

Ему стало интересно, сколько существует подстрок строки a вида a1(k)a2(i)a3(j), где a1, a2 и a3 обозначают строчные латинские буквы, а числа в скобках после символа — то, сколько раз этот символ повторяется, но важно, чтобы a1 ≠ a2 и a2 ≠ a3. Например, z(3)n(2)o(1) — это описание строки zzznnno.

Каждая группа тестов будет оцениваться только если предварительно были пройдены необходимые группы тестов, и баллы начисляются в случае, если все тесты группы пройдены. Тесты из условия не оцениваются. Все тесты разбиты на группы со следующими от ранжированием.

Первая строка входных данных содержит целое число n — длина строки a.
Вторая строка содержит строку a длины n, состоящую из строчных латинских букв.
В третьей строке записаны числа k, i, j, описывающие количество символов a1, a2, a3 в подстроках соответственно.

Выведите количество подстрок, представляемых в виде a1(k)a2(i)a3(j).

Входные данные
10
llvvyywwww
2 2 2
Выходные данные
2
"""
