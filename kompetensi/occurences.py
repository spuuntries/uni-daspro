_ = input()
inputs = map(int, input().split())
tosearch = int(input())
print(len(list(filter(lambda x: x == tosearch, inputs))))
