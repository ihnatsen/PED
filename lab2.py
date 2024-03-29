# 13.03.2024
import matplotlib.pyplot as plt
from collections import Counter
from pandas import *


df = read_csv('titanic.csv')


def task_one():
    print('task №1')
    print(f'The number of all passengers is {len(df)}.')


def task_two():
    print('task №2')
    survived_rec = df[df['Survived'] == 1]
    print(f'The number of survivors is {len(survived_rec)} people.')


def task_three():
    print('task №3')
    dead = df[df['Survived'] == 0]
    print(f'The number of survivors is {len(dead)} people.')


def task_four():
    print('task №4')
    presents = list(df.groupby(['Pclass'])["Survived"].mean())
    # or
    presents = [df[df['Pclass'] == name_class]["Survived"].mean() for name_class in range(1, 4)]

    presents = [f'{present * 100:_.2f}%' for present in presents]
    sorted_by_classes_for_survived = dict(zip([*range(1, 4)], presents))
    print(sorted_by_classes_for_survived)


def task_five():
    print('task №5')
    presents_for_sex = dict(df.groupby(['Sex'])['Survived'].mean())
    values = [f'{present * 100:_.2f}%' for present in presents_for_sex.values()]

    presents_for_sex = {name: value for name, value in zip(presents_for_sex, values)}

    print(presents_for_sex)


def task_six():
    print('task №6')
    ages = list(df['Age'])
    plt.hist(ages, bins=[*range(0, 81, 2)], edgecolor='black')
    plt.title('Rozkład wieku pasżerów')
    plt.xlabel('Wiek')
    plt.ylabel('Licba pasażerów')
    plt.show()


def task_seven():
    print(f'The mean fare is ${df['Fare'].mean():_.2f}.')


def task_eight():
    tickets = dict(Counter(list(df['Pclass']))).values()
    plt.barh(['1', '2', '3'], tickets)
    plt.title('Licbza pasażerów w każdej klasie bilietu.')
    plt.xlabel('Ilość')
    plt.ylabel('Klas')
    plt.show()


def main():
    task_one()
    task_two()
    task_three()
    task_four()
    task_five()
    task_six()
    task_seven()
    task_eight()


if __name__ == '__main__':
    main()
