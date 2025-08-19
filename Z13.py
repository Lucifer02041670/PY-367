import ast
import logging

logging.basicConfig( filename='Z13_log.log', filemode='w', format='%(levelname)s - %(message)s')

def average_of_numbers(nums):
    if not isinstance(nums, list):
        logging.error("Некорректный тип входных данных: ожидается список чисел (list)")
        raise TypeError(f"Ожидался список чисел (list)")

    if len(nums) == 0:
        logging.error("Пустой списоr")
        raise ValueError("Список пуст")

    total = 0.0
    for i, v in enumerate(nums):
        if not isinstance(v, (int, float)):
            logging.error("Элемент по индексу %d не является числом: %r (тип %s)", i, v, type(v).__name__)
            raise TypeError(f"Элемент по индексу {i} не является числом: {v!r}")
        total += v

    return total / len(nums)

def read_numbers_from_input():
    input_str = input("Введите список чисел как [1, 2, 3] (или нажмите Enter для выхода): ").strip()

    try:
        data = ast.literal_eval(input_str)
    except Exception:
        logging.exception("Ошибка разбора входной строки")
        print("Ошибка формата ввода: ожидался список чисел в виде [a, b, c].")
        return None

    if not isinstance(data, list):
        logging.error("Разбор не дал список")
        print("Ошибка: введено не список чисел. Ожидался список, например: [1, 2, 3].")
        return None

    return data

def main():
    nums = read_numbers_from_input()
    if nums is None:
        return

    try:
        mean = average_of_numbers(nums)
    except Exception as exc:
        print(f"Не удалось вычислить среднее: {exc}")
        return

    print(f"Среднее арифметическое: {mean}")

if __name__ == "__main__":
    main()