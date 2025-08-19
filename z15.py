def main():
    K = int(input())
    match K:
        case 1:
            print("плохо")
        case 2:
            print("неудовлетворительно")
        case 3:
            print("удовлетворительно")
        case 4:
            print("хорошо")
        case 5:
            print("отлично")
        case _:
            print("ошибка")


if __name__ == "__main__":
    main()