import sys

# arg
args = sys.argv[1:]
print (args)

# logic
result = 0
num_args = [int(s) for s in args]
for i in num_args:
    result += i

print(result)