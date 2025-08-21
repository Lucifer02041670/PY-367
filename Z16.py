def next_date(D, M):
    dey = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    if D < 1 or D > dey[M]:
        return "error"

    D += 1

    if D > dey[M]:
        D = 1
        M += 1

        if M > 12:
            M = 1

    return D, M

def main():
    D = int(input("Введите день D: "))
    M = int(input("Введите месяц M: "))
    next_D = next_date(D, M)
    print(next_D)

if __name__ == "__main__":
    main()