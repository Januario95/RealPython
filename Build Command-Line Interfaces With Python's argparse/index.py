import sys
import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('path')

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
	print('The target directory does not exist')
	raise SystemExit(1)


for entry in target_dir.iterdir():
	print(entry.name)








# if (args_count := len(sys.argv)) > 2:
# 	print(f'One argument expected, got {args_count - 1}')
# 	raise SystemExit(2)
# elif args_count < 2:
# 	print('You must specify the target directory')
# 	raise SystemExit(2)

# target_dir = Path(sys.argv[1])

# if not target_dir.is_dir():
# 	print('The target directory does not exist')
# 	raise SystemExit(1)

# for entry in target_dir.iterdir():
# 	print(entry.name)


# >>>python ls_argv.py sample/
# hello.txt
# lorem.md
# realpython.md

# >>>python ls_argv.py
# You must specify the target directory

# >>>python ls_argv.py sample/ other_dir/
# One argument expected, got 2

# >>>python ls_argv.py non_existing/
# The target directory doesn't exist

