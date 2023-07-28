import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--try', dest='Try', action=argparse.BooleanOptionalAction)

args = parser.parse_args()

if args.Try:
    print(f"Do or do not. There is no try")
else:
    print(f"That is why you fail")

