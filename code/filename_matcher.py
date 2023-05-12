import re

MATCHER = re.compile('\d{4}[A-Z]-[a-z]+\.md')

def filename_acceptor(candidate : str):
    return bool(MATCHER.match(candidate))

if __name__ == "__main__":
    while True:
        print(filename_acceptor(input(": ")))
