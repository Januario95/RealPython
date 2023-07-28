from argparse import ArgumentParser

parser = ArgumentParser()

print(parser.add_argument('site'))

print(parser.add_argument('-c', '--connect', action='store_true'))

args = parser.parse_args(['Real Python', '-c'])
print(args)
print(args.site)
print(args.connect)
