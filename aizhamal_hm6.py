def sums(numbers, desired_sum):
    for i in desired_sum:
        for a in desired_sum:
            if i + a ==numbers:
                print([desired_sum.index(i),desired_sum.index(a)])
sums(18,[2, 7, 11, 15])