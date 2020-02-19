#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = -1
    for recipe_key in recipe:
        if recipe_key not in ingredients:
            return 0
        if ingredients[recipe_key] - recipe[recipe_key] >= 0:
            how_many_batches = int(
                ingredients[recipe_key]/recipe[recipe_key])
            if max_batches == -1:
                max_batches = how_many_batches
            elif how_many_batches < max_batches:
                max_batches = how_many_batches
        else:
            max_batches = 0
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
