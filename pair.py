def pair(list_a, list_b):
    if len(list_a) >= len(list_b):
        for i in list_a:
            print("{0}, {1}".format(i, list_b[list_a.index(i)]))


fruits = ["Apple", "Orange", "Tomato", "Banana"]
vegetables = ["Zucchini", "Tomato", "Celery", "Broccoli"]
pair(fruits, vegetables)
