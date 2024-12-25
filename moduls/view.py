

from controller import controller_save
# controller_save_data('Nurbek', 'Salam')


def main():
    a = int(input("Введите число"))
    b = int(input("Введите число"))
    result = controller_save(a,b)
    print(f'{result}, результат')

if __name__ == '__main__':
    main()