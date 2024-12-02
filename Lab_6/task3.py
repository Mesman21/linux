import random


def reverse(lst: list[int]):
    lst.reverse()
    return lst


def iter_swap(lst: list[int], index1: int, index2: int):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
    else:
        print("Невірні індекси для обміну")


if __name__ == "__main__":
    size = int(input("Введіть кількість елементів у списку: "))
    linked_list = [random.randint(1, 10) for _ in range(size)]
    print("Початковий список:", linked_list)

    print("\nОберіть дію:")
    print("1 - Підрахувати кількість входжень елемента")
    print("2 - Перевернути список")
    print("3 - Обміняти елементи за індексами")
    print("4 - Вийти з програми")

    while True:

        choice = input("Ваш вибір: ")

        if choice == "1":
            value_to_count = int(input("Введіть значення для підрахунку: "))
            first = int(input("Введіть індекс з якого починається пошук: "))
            last = int(input("Введіть індекс на якому закінчується пошук: "))
            count_result = linked_list[first : last + 1].count(value_to_count)
            print(f"Кількість входжень числа {value_to_count}:", count_result)

        elif choice == "2":
            first = int(input("Введіть індекс з якого починати перевертати список: "))
            last = int(
                input("Введіть індекс на якому закінчувати перевертати список: ")
            )
            linked_list = (
                linked_list[0:first]
                + reverse(linked_list[first : last + 1])
                + linked_list[last + 1 :]
            )
            print("Список після реверсу:", linked_list)

        elif choice == "3":
            try:
                index1 = int(input("Введіть перший індекс для обміну: "))
                index2 = int(input("Введіть другий індекс для обміну: "))
                iter_swap(linked_list, index1, index2)
                print("Список після обміну:", linked_list)
            except ValueError:
                print("Введено неправильне значення індексу!")

        elif choice == "4":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
