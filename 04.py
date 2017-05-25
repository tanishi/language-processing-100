
def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
        New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    s = s.split()

    d = {};
    single = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    for element in s:
        if s.index(element) + 1 in single:
            d[element[:1]] = s.index(element) + 1
        else:
            d[element[:2]] = s.index(element) + 1

    for k, v in sorted(d.items(), key=lambda x:x[1]):
        print(k, v)

if __name__ == '__main__':
    main()
