import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('num', type=int)

args = parser.parse_args()

for _ in range(args.num):
    print(f"I'm sorry {args.name}, I'm afraid I can't do that")

# name = sys.argv[1]
# num = int(sys.argv[2])

# for _ in range(num):
#     print(f"I'm sorry {name}, I'm afraid I can't do that")