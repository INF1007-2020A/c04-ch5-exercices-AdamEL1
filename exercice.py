#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number >= 0:
        return number
    else:
        return number * -1


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    words = []
    for i in range(0, len(prefixes)):
        words.append(prefixes[i] + suffixe)
    return words


def prime_integer_summation() -> int:
    sum = 2
    number = 3
    count = 1
    is_prime = True
    while count < 100:
        for i in range(3, number, 2):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            sum += number
            count += 1
        is_prime = True
        number += 2
    return sum


def factorial(number: int) -> int:
    product = 1
    for i in range(1, number+1):
        product *= i
    return product


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    i = 0
    equipes_accepte = []
    for group in groups:
        if len(group) <= 3 or len(group) > 10:
            equipes_accepte.append(False)
            i += 1
            continue
        inter = i
        for ages in group:
            if ages == 25:
                equipes_accepte.append(True)
                i += 1
                break
        if inter != i:
            continue
        for ages in group:
            if ages < 18:
                equipes_accepte.append(False)
                i += 1
        if inter != i:
            continue
        for ages in group:
            if ages == 50:
                for ages2 in group:
                    if ages2 > 70:
                        equipes_accepte.append(False)
                        i += 1
        if inter != i:
            continue
        equipes_accepte.append(True)
    return equipes_accepte


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
