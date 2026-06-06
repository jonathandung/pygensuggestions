#!/usr/bin/env python3
import pygensuggestions as _
parser = __import__('argparse').ArgumentParser(prog='pygensuggestions', description='A basic command-line entry point to the pygensuggestions library.', add_help=False, fromfile_prefix_chars='@')
'''The argument parser used by the libary.'''
a = parser.add_argument
a('target', help='The incorrect string for which suggestions are to be given.')
a('candidates', nargs='+', help='No more than 750 candidate strings to compare against the target.')
a('-o', '--outfile', help='Write the output to a file instead of stdout.')
a('-s', '--strict', action='store_true', help='Always exit with status 3 if the target string exceeds 40 characters, or status 4 if there are over 750 candidates, instead of emitting a warning to stderr and adaptin_.')
a('-a', '--allow-identical', action='store_true', help='Allow strings in the candidates list that are the same as the target to be matched.')
a('-q', '--quiet', action='store_true', help='Suppress all output to stderr. Has no effect if the exit code is 0.')
a('-h', '-?', '--help', action='help', help='Print this help message to stdout and exit.')
a('-v', '--version', action='version', version='pygensuggestions v'+_.__version__, help='Print the version number to stdout and exit.')
def main(argv=None, _=_):
    '''The main function for the command-line interface. Takes the arguments `argv` (a list of strings without the executable name as the first item),
    or `sys.argv[1:]` by default, and returns an integer exit code. See the README for the meaning of the exit codes.'''
    g = _.lib
    try: a = parser.parse_args(argv)
    except SystemExit as e: return e.code
    t, c, s, o, m, i, w = a.target, a.candidates, a.strict, a.outfile, g.MAX_STRING_SIZE, g.MAX_CANDIDATE_ITEMS, (lambda _: None) if a.quiet else __import__('sys').stderr.write
    d, n = len(t), len(c)
    if d > m:
        if s:
            w(f'Target string too long ({d} > {m})\n')
            return 3
        w(f'Warning: Target string too long ({d} > {m}); adjusting\n')
        g.MAX_STRING_SIZE = d
    if n > i:
        if s:
            w(f'Too many candidate strings ({n} > {i})\n')
            return 4
        w(f'Warning: Too many candidate strings ({n} > {i}); adjusting\n')
        g.MAX_CANDIDATE_ITEMS = n
    r = _.suggest(c, t, skip_identical=not a.allow_identical)
    if r is None:
        w('No suitable suggestion found!\n')
        return 1
    if o is None: print(r, flush=True)
    else: __import__('pathlib').Path(o).write_text(r)
    return 0
if __name__ == '__main__': parser.exit(main())
del a, _
