def common_elements():
    first_list = [_ for _ in range(100) if _ % 3 == 0]
    second_list = [_ for _ in range(100) if _ % 5 == 0]
    return set(first_list) & set(second_list)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

