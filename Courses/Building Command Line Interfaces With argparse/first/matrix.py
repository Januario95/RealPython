import string
import random
import argparse

TEXT = string.ascii_letters + string.digits + string.punctuation

parser = argparse.ArgumentParser(
    prog='matrix',
    usage='whoa, use: %(prog)s [options] number',
    description='Prints random columns of characters',
    epilog='If it were green it would be like that matrix'
)
parser.add_argument('num', type=int)

args = parser.parse_args()

for _ in range(args.num):
    content = [random.choice(TEXT) for _ in range(20)]
    print('  '.join(content))

