import logging
import math

logging.basicConfig(level=logging.INFO, filename="Z11_log.log", filemode="w", format="%(levelname)s %(message)s")

def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        logging.error(f"D = {D}. Error.")
        raise Exception("Дискриминант отрицателен")
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
        logging.info(f"Done: x1 = {x1}, x2 = {x2}")
        return x1, x2

def main():
    while True:

        a = float(input("a: "))
        if a == 0:
            print("a не может быть равен 0")
            continue
        b = float(input("b: "))
        c = float(input("c: "))
        try:
            x1, x2 = solve_quadratic(a, b, c)
            print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            print("Попробуйте еще раз")

if __name__ == "__main__":
    main()