import argparse

# add_help=False; to turn off the "-h" feature
# prefix_chars='/': change the prefix character for a flag
# to a different value

parser = argparse.ArgumentParser(allow_abbrev=True,
                                 fromfile_prefix_chars='@')
# python snowwhite.py @madlib_snow.txt
parser.add_argument('item')
parser.add_argument('place')
parser.add_argument('description')
parser.add_argument('count')
parser.add_argument('--upper', action='store_true')

args = parser.parse_args()

text = f"""Magic {args.item} on the {args.place}, who is the
{args.description} {args.count} of all?"""

if args.upper:
    text = text.upper()

print(text)
