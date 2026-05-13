# Love Calculator
from itertools import count


def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    combined_name = combined_name.upper()
    score_TRUE = calculate_TRUE(combined_name)
    score_LOVE = calculate_LOVE(combined_name)
    love_score = int(str(score_TRUE) + str(score_LOVE))
    print(love_score)


def calculate_TRUE(name):
    string_TRUE = "TRUE"
    score = 0
    for ch in string_TRUE:
        ch_count = name.count(ch)
        score += ch_count
        if ch_count == 1:
            print(f"{ch} occurs {ch_count} time")
        else:
            print(f"{ch} occurs {ch_count} times")
    return score



def calculate_LOVE(name):
    string_LOVE = "LOVE"
    score = 0
    for ch in string_LOVE:
        ch_count = name.count(ch)
        score += ch_count
        if ch_count == 1:
            print(f"{ch} occurs {ch_count} time")
        else:
            print(f"{ch} occurs {ch_count} times")
    return score



calculate_love_score(name1="Kanye West", name2="Kim Kardashian")

# name1 = input("Please enter the first name -->")
# name2 = input("Please enter the second name -->")
#
# calculate_love_score(name1=name1, name2=name2)
