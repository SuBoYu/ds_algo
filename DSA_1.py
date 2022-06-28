# step 1

# binary search
# cards is in descending order

def location_test(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if cards[mid-1] == query and mid-1 >= 0:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


def locate_card(cards, query):
    lo= 0
    hi = len(cards)-1

    while lo <= hi:
        mid = (lo + hi)//2
        mid_number = cards[mid]

        print("lo:", lo, "hi", hi, "mid", mid, "mid_number", mid_number)
        result = location_test(cards, query, mid)

        if result == "right":
            lo = mid + 1
        elif result == "left":
            hi = mid - 1
        else:
            return mid

    return -1



# step 2
# cards = [13, 11, 10, 7, 4, 3, 1, 0]
# query = 7
# output = 3

test = {
    "input": {
        "cards": [13, 11, 10, 7, 4, 3, 1, 0],
        "query": 7
    },
    "output": 3
}

locate_card(**test["input"]) == test["output"]

# thinking about edge cases

tests = []
tests.append(test)
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    "input": {
        "cards": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        "query": 6
    },
    "output": 2

})

for test in tests:
    print(locate_card(test["input"]["cards"], test["input"]["query"]))

# 發現第三組測資有錯，修正
# When we find that cards[mid] is equal to query, we need to check whether it is the first occurrence of query in the list i.e the number that comes before it.
#
# [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
#
# To make it easier, we'll define a helper function called test_location, which will take the list cards, the query and mid as inputs.

