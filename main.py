def input_validation(input_context: str) -> float:
    while True:
        print(input_context)
        try:
            return float(input())
        except ValueError as exc:
            print(f"Введеная строка не является числов. Попробуйте снова. \nПодробнее: {exc}")


def get_input() -> tuple:
    a = input_validation("Введите a: ")
    b = input_validation("Введите b: ")
    c = input_validation("Введите c: ")
    return a, b, c


def solution(a, b, c) -> float:
    if (a+b) > c and (a+c) > b and (c+b) > a:
        print("Треугольник построить можно")
        if a != b and a != c and b != c:
            print("Разносторонний")
        elif a == b == c:
            print("Равносторонний")
        else:
            print("Равнобедренный")
    else:
        print("Треугольник построить нельзя")


def show_result(value: float):
    pass


def main():
    input_result = get_input()
    expression_result = solution(*input_result)
    show_result(expression_result)


if __name__ == "__main__":
    main()