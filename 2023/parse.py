"""
Assumes each line is one example of an input.
"""
def read_input(file):
    with open(file, 'r') as f:
        return f.read().splitlines()
