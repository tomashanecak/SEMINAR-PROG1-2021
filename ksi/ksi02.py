def lists(a, b, c, d):
    first_list = list(range(0,a+1))
    second_list = list(range(0,a+1))
    third_list = first_list[0:c]

    
    for i in range(len(second_list)):
        second_list[i] += 10
    
    second_list[len(second_list) -1] = "KSI"

    if b in second_list:
        second_list.remove(b)
    else:
        print("Not here")

    second_list += third_list

    third_list.reverse()

    first_list[1] = d
    first_list.sort()

    return (first_list, second_list, third_list)


# def lists(a, b, c, d):
#     first_list = [x for x in range(0, a + 1)]
#     second_list = []
#     for prvok in first_list:
#         second_list.append(prvok + 10)
#     second_list[-1] = 'KSI'
#     if b in second_list:
#         second_list.remove(b)
#     else:
#         print("Not here")
#     third_list = first_list[:c]
#     second_list.extend(third_list)
#     third_list.reverse()
#     first_list[1] = d
#     first_list.sort()
#     return (first_list, second_list, third_list)


# print(lists(5, 12, 3, 20))
# print(lists(10, 3, 2, 11))
# print(lists(3, 15, 3, 3))
# print(lists(15, 25, 2, 2))

