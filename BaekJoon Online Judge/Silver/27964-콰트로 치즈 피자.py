import sys


def can_make_quatre_cheese_pizza(toppings):
    cheese = set()

    for topping in toppings:
        if topping.endswith('Cheese'):
            cheese.add(topping)

    if len(cheese) >= 4:
        return True
    else:
        return False


def print_answer_format(available):
    if (available):
        print('yummy')
    else:
        print('sad')


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    toppings = sys.stdin.readline().rstrip().split()
    result = can_make_quatre_cheese_pizza(toppings)
    print_answer_format(result)
