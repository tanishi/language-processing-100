import re


def split_pi(s):
    return [len(x) for x in re.sub(r",|\.", "", s).split()]


def main():
    s = '''Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.'''

    print(split_pi(s))


if __name__ == '__main__':
    main()
