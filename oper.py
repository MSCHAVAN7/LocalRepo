def search_missing_number(list_num):
    n = len(list_num)
    # checks
    if(list_num[0] != 1):
        return 1
    if(list_num[n-1] != (n+1)):
        return n+1

    total = (n + 1)*(n + 2)/2
    sum_of_L = sum(list_num)
    return total - sum_of_L

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
print("The missing number is: ", search_missing_number(num_list))
