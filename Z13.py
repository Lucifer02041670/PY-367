import ast
import logging

logging.basicConfig( filename='Z13_log.log', filemode='w', format='%(levelname)s - %(message)s')

def average_of_numbers(nums):
    if not isinstance(nums, list):
        logging.error("Incorrect type of input data")
        raise TypeError(f"Ожидался список чисел (list)")

    if len(nums) == 0:
        logging.error("Empty list")
        raise ValueError("Список пуст")

    total = 0.0
    for i, v in enumerate(nums):
        if not isinstance(v, (int, float)):
            logging.error("The element is not a number")
            raise TypeError(f"Элемент по индексу {i} не является числом")
        total += v

    return total / len(nums)

def read_numbers_from_input():
    input_str = input("Введите список чисел как [1, 2, 3]").strip()

    try:
        data = ast.literal_eval(input_str)
    except Exception:
        logging.exception("Error parsing the input string")
        print("Ошибка формата ввода")
        return None

    if not isinstance(data, list):
        logging.error("The analysis did not provide a list")
        print("введен не список чисел")
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