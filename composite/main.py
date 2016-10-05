#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Menu import Menu
from MenuItem import MenuItem
from Waitress import Waitress

if __name__ == '__main__':
    pancakeHouseMenu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    dinerMenu = Menu('DINER MENU', 'Lunch')
    cafeMenu = Menu('CAFE MENU', 'Dinner')
    dessertMenu = Menu("DESSERT MENU", "Dessert of course!")

    allMenus = Menu("ALL MENUS", "All menus combined")

    allMenus.add(pancakeHouseMenu)
    allMenus.add(dinerMenu)
    allMenus.add(cafeMenu)

    pancakeHouseMenu.add(MenuItem(
                        "K&B's Pancake Breakfast",
                        "Pancakes with scrambled eggs, and toast",
                        True, 2.99))

    pancakeHouseMenu.add(MenuItem(
                        "Regular Pancake Breakfast",
                        "Pancakes with fried eggs, sausage",
                        False, 2.99))

    dinerMenu.add(MenuItem("Pasta",
                            "Spaghetti with Marinara Sauce,and a slice of sourdough bread",
                            True, 3.89))

    dinerMenu.add(dessertMenu)

    dessertMenu.add(MenuItem("Apple Pie",
                    "Apple pie with a flakey crust, topped with vanilla icecream",
                    True, 1.59))

    cafeMenu.add(MenuItem(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,3.99))

    waitress = Waitress(allMenus)

    waitress.printMenu()
