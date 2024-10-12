from collections import Counter

if __name__ == '__main__':
    c = Counter()
    c['a'] += 1
    c['g'] += 1
    c['a'] += 1
    c['a'] += 1


    print(c)