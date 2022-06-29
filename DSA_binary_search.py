import time

# step 1

# binary search
# cards is in descending order

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)

        if result == "right":
            lo = mid + 1
        elif result == "left":
            hi = mid - 1
        else:
            return mid
    return -1


def locate_card(cards, query):
    def condition(mid):
        mid_number = cards[mid]
        if mid_number == query:
            if cards[mid - 1] == query and mid - 1 >= 0:
                return "left"
            else:
                return "found"
        elif mid_number < query:
            return "left"
        else:
            return "right"

    return binary_search(0, len(cards) - 1, condition)


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

tests.append({
    "input": {
        "cards": list(range(10000000, 0, -1)),
        "query": 2
    },
    "output": 9999998
})

for test in tests:
    start = time.process_time()
    result = locate_card(test["input"]["cards"], test["input"]["query"])
    end = time.process_time()
    print("algorithm executing time: %f sec" % (end-start))
    if test["output"] == result:
        print("correct")
    else:
        print("false")

# 發現第三組測資有錯，修正
# When we find that cards[mid] is equal to query, we need to check whether it is the first occurrence of query in the list i.e the number that comes before it.
#
# [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
#
# To make it easier, we'll define a helper function called test_location, which will take the list cards, the query and mid as inputs.
