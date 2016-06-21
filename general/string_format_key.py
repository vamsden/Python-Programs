def title_case(title, minor_words):
    """
    Program to format string.
    """
    list = []
    title = title.lower()
    minor_words = minor_words.lower()
    x = title.split(" ")
    y = minor_words.split(" ")
    for i in x:
        if i not in y:
            list.append(i.capitalize())
        else:
            list.append(i)
    list[0] = list[0].capitalize()
    final = (" ").join(list)
    return final
# title = (" ").join()


print(title_case("i am Coming home to eat", "Am to"))
print(title_case('I am the KINGS', 'am'))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox', 'fox'))
