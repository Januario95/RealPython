import argparse
SENTENCES = ['Listen to them.', 'Children of the night.',
             'What music they make.']

parser = argparse.ArgumentParser()
parser.add_argument('noise')
parser.add_argument('extra', action='store', nargs=argparse.REMAINDER)

args = parser.parse_args()

for sentence in SENTENCES:
    print(sentence, f'*{args.noise}* ', end='')

print()

print('  '.join(args.extra))