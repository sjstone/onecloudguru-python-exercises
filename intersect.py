def intersect(list_a, list_b):
    list_intersect = []
    for i in list_a:
        if i in list_b:
            list_intersect.append(i)
    return list_intersect


fruits = ["Apple", "Orange", "Tomato", "Banana"]
vegetables = ["Zucchini", "Tomato", "Celery", "Broccoli"]
print(intersect(fruits, vegetables))
