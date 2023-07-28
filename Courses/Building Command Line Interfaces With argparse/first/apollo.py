import argparse

parser = argparse.ArgumentParser()

parser.add_argument('tee', action='store', nargs='*', type=int)
# usage: python apollo.py 5 4

args = parser.parse_args()

for x in range(10, 0, -1):
    if x in args.tee:
        print('T-minus ', end='')

    print(x)

print('We have lifoff')
