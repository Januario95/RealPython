import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-w', '--word', action='store', nargs=3)
# nargs: use to input three words sequentially
# python harry.py -w first second third

args = parser.parse_args()

print(f"You've got to ask yourself {args.word[0]} question:")
print(f"Do I {args.word[1]} lucky? Well, do ya, {args.word[2]}")
