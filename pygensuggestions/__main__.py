#!/usr/bin/env python3
from argparse import ArgumentParser
from pygensuggestions import __version__, suggest
parser = ArgumentParser(prog='pygensuggestions', description='A basic command-line entry point to the pygensuggestions library.', add_help=False, fromfile_prefix_chars='@')
parser.add_argument('target', help='The incorrect string for which suggestions are to be given.')
parser.add_argument('candidates', nargs='*', help='No more than 750 candidate strings to compare against the target.')
parser.add_argument('-o', '--outfile', help='Write the output to a file instead of stdout.')
parser.add_argument('-?', '-h', '--help', action='help', help='Print this help message to stdout and exit.')
parser.add_argument('-v', '--version', action='version', version='pygensuggestions v'+__version__, help='Print the version number to stdout and exit.')
def main():
    a = parser.parse_args()
    r, o = suggest(a.candidates, a.target), a.outfile
    if r is None: parser.exit(1, 'No suitable suggestion found!\n')
    if o is None: print(r)
    else: __import__('pathlib').Path(o).write_text(r)
if __name__ == '__main__': main()