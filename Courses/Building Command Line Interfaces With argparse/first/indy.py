import argparse

# Actions
def raiders(args):
    print(f"{args.animal.capitalize()}. Why'd it have to be {args.animal}?")

def doom(args):
    for _ in range(args.repeat):
        print("Kali ma...")

    print("Shakthi deh!")

def crusade(args):
    print(f"Sallah, I said 'no' camels. That's {args.count} camels")
    print("Can't you count?")


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   dest='command')
subparsers.required = True

sub = subparsers.add_parser('raiders')
sub.add_argument('animal')
sub.set_defaults(func=raiders)

sub = subparsers.add_parser('doom')
sub.add_argument('-r', dest='repeat', default=3, type=int, metavar='NUM')
sub.set_defaults(func=doom)

sub = subparsers.add_parser('crusade')
sub.add_argument('count')
sub.set_defaults(func=crusade)

args = parser.parse_args()
args.func(args)

