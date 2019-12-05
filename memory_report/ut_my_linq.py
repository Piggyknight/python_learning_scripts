# -*- coding:utf-8 -*-

from my_linq import *


test_result = {
    "select-list": {
        "expected": linq([1, 2, 3, 4, 5, 6]).where(lambda x: x % 2 == 0).select(lambda x: x * 2).tolist(),
        "actual": [4, 8, 12]
    },
    "sum": {
        "expected": linq([1, 2, 3, 4, 5, 6]).where(lambda x: x % 2 == 0).sum(),
        "actual": 12
    },
    "max": {
        "expected": linq([1, 2, 3, 4, 5, 6]).max(),
        "actual": 6
    },
    "min": {
        "expected": linq([1, 2, 3, 4, 5, 6]).min(),
        "actual": 1
    },
    "all": {
        "expected": [linq([1, 2, 3, 4, 5, 6]).all(lambda x: x < 3),
                        linq([1, 2, 3, 4, 5, 6]).all(lambda x: x > 0), ],
        "actual": [False, True]
    },
    "any": {
        "expected": [linq([1, 2, 3, 4, 5, 6]).any(lambda x: x > 3),
                        linq([1, 2, 3, 4, 5, 6]).any(lambda x: x < 0), ],
        "actual": [True, False]
    },
    "average": {
        "expected": linq([1, 2, 3, 4, 5, 6]).average(),
        "actual": 3.5
    },
    "union": {
        "expected": linq([1, 2, 3, 4, 5, 6]).union([8, 9, 10]).tolist(),
        "actual": [1, 2, 3, 4, 5, 6, 8, 9, 10]
    },
    "count": {
        "expected": linq([1, 2, 3, 4, 5, 6]).where(lambda x: x > 1).count(),
        "actual": 5
    },
    "first": {
        "expected": linq([1, 2, 3, 4, 5, 6]).where(lambda x: x > 1).first(),
        "actual": 2
    },
    "last": {
        "expected": linq([1, 2, 3, 4, 5, 6]).where(lambda x: x < 4).last(),
        "actual": 3
    },
}

for name, result in test_result.items():
    expected = result["expected"]
    actual = result["actual"]
    if expected == actual:
        print('%s test success!' % name)
    else:
        print('%s test failed!\n    correct: %s\n    actually: %s' % (name, actual, expected))
