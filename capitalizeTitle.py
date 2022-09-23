def capitalizeTitle(title):
    """capitalizes any word bigger than 2 letters"""
    fixed_title = ""
    list_title = title.split(" ")
    for word in list_title:
        if len(word) > 2:
            fixed_title = f"{fixed_title} {word.title()}"
        else:
            fixed_title = f"{fixed_title} {word.lower()}"
    return fixed_title

test = ["capiTalIze tHe titLe","First leTTeR of EACH Word","i lOve leetcode"]
for data in test:
    print(capitalizeTitle(data))
