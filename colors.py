YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[0m'
RED = '\033[91m'

def green(str):
    return f'{GREEN}{str}{WHITE}'

def red(str):
    return f'{RED}{str}{WHITE}'

def yellow(str):
    return f'{YELLOW}{str}{WHITE}'