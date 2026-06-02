# [pygensuggestions](https://pypi.org/p/pygensuggestions)

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

A backport of the `_suggestions` module, native to CPython since 3.12, to other versions of Python.

## Quickstart

```bash
pip install pygensuggestions==2.0.0 # pip
pip install git+https://github.com/jonathandung/pygensuggestions.git # directly from repo
uv pip install pygensuggestions==2.0.0 # uv
conda install -c conda-forge pygensuggestions==2.0.0 # conda: method 1
```

Less common pathways:

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install pygensuggestions==2.0.0 # conda: method 2
pipx install pygensuggestions==2.0.0 # pipx
poetry add pygensuggestions@2.0.0 # poetry
pdm add pygensuggestions==2.0.0 # pdm
pipenv install pygensuggestions=2.0.0 # pipenv
```

## Usage

```pycon
>>> import pygensuggestions # the module
>>> pygensuggestions.suggest( # the primary function
... ('foo', 'bar', 'baz'), # arg 1: the sized iterable over words from which suggestions are taken
... 'bar' # arg 2: the wrong word
... ) # notice that the exact word, if present in the sequence, is not returned by default
'baz'
>>> pygensuggestions.suggest(['abcd', 'efgh'], 'zyxd') # Returns None, because the target is too far from the candidates\
... # No output is produced
>>> pygensuggestions.suggest({b'red', b'blue', b'yellow'}, b'blew') # all bytes are also OK, as long as data is homogeneous
b'blue'
```

## Command line usage

```console
$ echo "thousand
> hundred" > moreopts.txt
$ pygensuggestions tousand million atousend @moreopts.txt --outfile res.out # read candidates from arguments and optionally a newline-delimited file
$ echo $? # check exit code
0
$ cat res.out # print the result
thousand
```

### Interpretation of exit codes

- 0: a suggestion was successfully found
- 1: no suggestion was close enough
- 2: incorrect (combination of) command-line arguments, including if there isn't at least 1 target and 1 candidate (returned by
  `argparse.ArgumentParser.error`)
- 3: the target string exceeds 40 characters and `--strict` or `-s` was passed
- 4: the number of candidates is greater than 750 and `--strict` or `-s` was passed

## Background

The `_suggestions` module was implemented in C, at `Modules/_suggestions.c`, as part of an attempt to improve user experience by enriching the
traceback dump of some errors regarding nonexistent attribute or module names closely resembling a known module or attribute, as well as apparently
mistyped keywords. It contains a helper internal to the Python interpreter, as signified by the underscore-prefixed name, called
`_generate_suggestions`, which takes an exact instance of a list as the first argument and a string as the second, and returns the string most
similar to the target in the list, or `None` if a certain threshold determined by a Levenshtein distance-based metric with weighted move and case
costs is not reached, or there are too many strings in the list.

## What does this library do?

This library provides a faithful translation of that sophisticated deterministic engine to pure Python, along with a simple command-line interface to
call this core function from the shell. It is incredibly simple and custom wrappers should be built upon it for it to really shine. In this context,
"deterministic" is sensitive to the order in which items appear in the sequence.

It also boasts maximum portability. It supports Python 3.8 and above out-of-the-box, and is implementation-agnostic. It also can take any sized
iterable of candidates, which can be `str` or `bytes` as long as it is consistent with the type of the target, as opposed to typical implementations
that only accept sequences.

Since this is not exactly a long-running algorithm, I decided against writing it in C, which would boil down to blatant copying of the Python
source, probably fail in alternate Python realizations and suffer the same pitfalls described in the next section.

The two functions used to assist in the implementation, `lev_dist` and `sub_cost`, are also exposed in the `lib` submodule. One may find this
unorthodox procedure derived from the well-known 'edit distance' recipe accounting for case and storing only one row of the traditional 2D dynamic
programming style array to avoid the memory overhead, albeit slight, particularly valuable.

## Why this module?

Indeed, alternatives to this module exist. Their shortfalls are detailed below.

The `_suggestions` module itself is, of course, a contender. However, it only accepts strict instances of `list` for the first argument, and both
arguments cannot have `bytes`. Though it is the fastest because it is written in C, it is not public and not available on older Python versions.

While the `traceback` module does implement this in pure Python as a fallback, it is again in the form of an unstable, private function, and is
not available on all versions of Python. Worse still, it is difficult to separate out the logic because the helper function in question is made to
handle an exception traceback. After all, it is the _traceback_ module!

I have yet to find modules on the Python Package Index providing comparable functionality to this module. It is not to say they are too simple; in
fact, the algorithms used may be overkill for some, or wrapped in unrelated logic. The routine actually used by CPython, the reference implementation
of Python, is likely only accessible with such transparency here.

## Situations in which `suggest` returns `None`

1. When you pass too many candidates (>750), since this library mirrors the Python source. If you must bypass this, set `lib.MAX_CANDIDATE_ITEMS` to
   `float('inf')`, suppressing type checker complaints, or pass `respect_bounds=False`.
2. When the length of the target string exceeds 40 characters, for the same reason. Set `lib.MAX_STRING_SIZE` to `float('inf')` or pass
   `respect_bounds=False` to alter this behaviour.
3. More than one-third of characters require modification for any candidate chosen.

## License

[MIT](https://github.com/jonathandung/pygensuggestions/blob/main/LICENSE) © 2026 Jonathan Dung
