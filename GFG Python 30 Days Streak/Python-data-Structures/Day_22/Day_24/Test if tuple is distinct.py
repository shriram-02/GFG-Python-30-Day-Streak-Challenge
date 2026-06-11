arr = tuple(map(int, input().split()))

# code here
print("True" if len(arr) == len(set(arr)) else "False")
