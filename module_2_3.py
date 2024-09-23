my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
beginning = 0
while beginning <= len(my_list):
    if my_list[beginning] > 0:
        print(my_list[beginning])
        beginning += 1
    elif my_list[beginning] < 0:
        break
    else:
        beginning += 1
        continue

