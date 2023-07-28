import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--shout', action='count', default=0)
# usage: python script_name.py -ssss (the s can be repeated)
words = "You can't handle the truth!".split()

args = parser.parse_args()

for count, word in enumerate(words, start=1):
    if count <= args.shout:
        print(word.upper() + ' ', end='')
    else:
        print(word + ' ', end='')
        
print()
