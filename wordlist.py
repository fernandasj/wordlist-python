#! /usr/bin/env python3

from itertools import combinations, permutations


def generate(elements):
    wordlist = []

    for element in elements:
        wordlist.extend([''.join(i) for i in permutations(element)])

    return wordlist


def save(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')


def count(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    return len(lines)


if __name__ == '__main__':
    filename = 'wordlist.txt'
    a = '01234567'
    b = 'abc'

    wordlist = generate([''.join(x) + ''.join(y) for x in combinations(a, 5) for y in combinations(b, 2)])
    save(wordlist, filename)
    print('{size} words possibles.'.format(size=count(filename)))
