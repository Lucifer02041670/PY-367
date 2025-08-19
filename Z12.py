import logging
import random

logging.basicConfig( filename='Z12_log.log', filemode='w', format='%(levelname)s - %(message)s')

def read_bounds():
    while True:
        try:
            a = int(input("нижняя граница: "))
            b = int(input("верхняя граница: "))

        except ValueError:
            print("Ошибка: не целые числа")
            logging.error("Incorrect input")
            continue

        if a < 0 or b < 0:
            print("Ошибка: границы диапазона должны быть неотрицательными")
            logging.error(f"Invalid range(boundaries are negative): {a}, {b}")
            continue

        if a > b:

            print("Ошибка: нижняя граница не может быть больше верхней")
            logging.error(f"Invalid range(lower border larger than upper): {a}, {b}")
            continue

        return a, b

def main():
    a, b = read_bounds()
    value = random.randint(a, b)
    print(value)


if __name__ == "__main__":
    main()