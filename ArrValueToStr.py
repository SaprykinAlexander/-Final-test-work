def arr_edit(x=["hello", "2", "world", ".;)!@", "1595562656", "999", "опа опа о па па",
                "хоба", "Привет Сергею К.", "O_o", "ZZZ"]):
    """
    Функция принимает на вход массив, а возвращает остортированный массив
    где длина кажого элемента не более 3 символов. Есть возможность как не передавать
    аргумент функции (он задан по умолчанию) так и передать произвольный.

    :param x: Массив который мы передаем функции.
    """
    new_arr = []
    for value in x:
        if len(value) <= 3:
            new_arr.append(value)
    return new_arr

#print(arr_edit(["412", "][';s", "sos", "KYKy", ")()"]))#Тут проверка с передачей массива в виде аргумента
#print(arr_edit())#Здесь проверка со значенем аргумента по умолчанию
