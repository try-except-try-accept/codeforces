n=int(input())
words=[input()for _ in range(n)]
[print(f"{w[0]}{len(w)-2}{w[-1]}"if len(w)>10 else w) for w in words]
