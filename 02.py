def combine_str(s1, s2):
    return "".join([i + j for i, j in zip(s1, s2)])


def main():
    s1 = "パトカー"
    s2 = "タクシー"

    print(combine_str(s1, s2))


if __name__ == '__main__':
    main()
