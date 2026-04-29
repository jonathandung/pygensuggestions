# Support Guidelines

Thank you for using pygensuggestions! This document outlines how to get help with this project.

Before jumping to seek support, please read through **[README.md](https://github.com/jonathandung/pygensuggestions/blob/main/README.md)**.

## Bug Reports

If you've found a bug, please:

1. Check if it's already reported in [Issues](https://github.com/jonathandung/pygensuggestions/issues)
2. If not, create a new issue

## 🔧 Common Issues & Solutions

### Installation Problems

Update your package installer, then try the following fixes:

```bash
# Upgrade
pip install -U pygensuggestions

# Check for dependency shenanigans
pip check
echo $? # Should be 0

# Clean install
pip uninstall pygensuggestions
pip install pygensuggestions

# If using pipx

pip install -U pipx
pipx ensurepath

# If using uv
uv pip install -U pygensuggestions
```

### Import Errors

Check if pygensuggestions is installed:

```bash
pip list | grep pygensuggestions
```

If the package is not working with python, perform the steps below:

```bash
# Check sys.path
python -c "print(*__import__('sys').path, sep='\n')"
# Check for package naming conflicts
python -c "print(*dir(__import__('pygensuggestions')), sep='\n')"
# If not loading site, repeat the above steps w/ python -Sc
```

## Version Compatibility

- Python 3.9+ required
- No dependencies outside development, which we're proud of
- This project is under active development (patch version is frequently bumped) that can have breaking changes

## Response Times

As fast as I can; that is:

- Bug reports: 3 days
- Feature requests: Reviewed biweekly
- General questions: Hopefully community-driven

## Closing remarks

Don't:

- Bump issues with +1 or "me too"
- Email maintainers unless urgent
- Ask about ETA of features/fixes

Instead:

- React to issues
- Open discussions or issues, or a pull request if the problem is easily fixable
- Be patient

Once again, thank you for supporting this small project. Happy programming!
