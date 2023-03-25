w=int(input())
print("YES"if any((w-i)%2==0 for i in range(2,w,2))else"NO")
