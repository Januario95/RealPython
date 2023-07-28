import argparse

parser = argparse.ArgumentParser()
parser.version = '1945'

parser.add_argument('-w', '--word', action='append',
                    help='Pick the words that Terry says')
parser.add_argument('-?', action='help')
parser.add_argument('-v', action='version')

args = parser.parse_args()

print(f"You don't understand! I couldd had {args.word[0]}")
print(f"I could've been a {args.word[1]}. I could've been")
print(f"{args.word[2]}, instead of a bum, which is what I am")
