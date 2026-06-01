#!/usr/bin/env python3
from argparse import ArgumentParser
from pygensuggestions import __version__, lib, suggest
from sys import stderr
parser = ArgumentParser(prog='pygensuggestions', description='A basic command-line entry point to the pygensuggestions library.', add_help=False, fromfile_prefix_chars='@')
parser.add_argument('target', help='The incorrect string for which suggestions are to be given.')
parser.add_argument('candidates', nargs='*', help='No more than 750 candidate strings to compare against the target.')
parser.add_argument('-o', '--outfile', help='Write the output to a file instead of stdout.')
parser.add_argument('-s', '--strict', action='store_true', help='Always exit with status 2 if the target string exceeds 40 characters, or status 3 if there are over 750 candidates, instead of emitting a warning and adapting. To silence the warnings, redirect stderr to null.')
parser.add_argument('-?', '-h', '--help', action='help', help='Print this help message to stdout and exit.')
parser.add_argument('-v', '--version', action='version', version='pygensuggestions v'+__version__, help='Print the version number to stdout and exit.')
def main():
    a, m, i = parser.parse_args(), lib.MAX_STRING_SIZE, lib.MAX_CANDIDATE_ITEMS
    t, c, s = a.target, a.candidates, a.strict
    d, n = len(t), len(c)
    if d > m:
        if s: parser.exit(2, f'Target string too long ({d} > {m})\n')
        stderr.write(f'Warning: Target string too long ({d} > {m}); adjusting\n')
        lib.MAX_STRING_SIZE = d
    if n > i:
        if s: parser.exit(3, f'Too many candidate strings ({n} > {i})\n')
        stderr.write(f'Warning: Too many candidate strings ({n} > {i}); adjusting\n')
        lib.MAX_CANDIDATE_ITEMS = n
    r, o = suggest(a.candidates, a.target), a.outfile
    if r is None: parser.exit(1, 'No suitable suggestion found!\n')
    if o is None: print(r)
    else: __import__('pathlib').Path(o).write_text(r)
if __name__ == '__main__': main()