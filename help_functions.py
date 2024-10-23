def test_dictionary(dictionary, start, end,):
    for i, (key, value) in enumerate(dictionary.items()):
        if i in range(start,end):  # Stop after the first 5 entries
            print(f"{key}: {value}")
        elif i == end:
            break


def get_next_qtr(quarter_string):
    qtr_digit = int(quarter_string[1])
    year = int(quarter_string[-4:])

    if qtr_digit in (1,2,3):
        qtr_digit += 1
        return('Q'+str(qtr_digit)+" "+str(year))

    elif qtr_digit == 4:
            qtr_digit = 1
            year += 1
            return('Q'+str(qtr_digit)+" "+str(year))


