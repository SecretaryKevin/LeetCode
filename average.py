def average(salary):
    """returns average"""
    total = 0
    for number in salary:
        total = total + number
    return total / len(salary)


print(average([8000,9000,2000,3000,6000,1000]))
