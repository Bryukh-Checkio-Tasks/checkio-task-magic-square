"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
                [2, 7, 6],
                [9, 5, 1],
                [4, 3, 0]
            ],
            "answer": [
                [2, 7, 6],
                [9, 5, 1],
                [4, 3, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 0, 0],
                [0, 5, 0],
                [0, 0, 0]
            ],
            "answer": [
                [0, 0, 0],
                [0, 5, 0],
                [0, 0, 0]
            ],
            "explanation": ""

        },
        {
            "input": [
                [2, 0, 4],
                [0, 5, 0],
                [0, 0, 0]
            ],
            "answer": [
                [2, 0, 4],
                [0, 5, 0],
                [0, 0, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 9, 0],
                [3, 0, 7],
                [0, 1, 0]
            ],
            "answer": [
                [0, 9, 0],
                [3, 0, 7],
                [0, 1, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "answer": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "explanation": ""
        },

        {
            "input": [
                [0, 0, 0, 0],
                [15, 14, 3, 2],
                [10, 11, 6, 7],
                [0, 0, 0, 0]
            ],
            "answer": [
                [0, 0, 0, 0],
                [15, 14, 3, 2],
                [10, 11, 6, 7],
                [0, 0, 0, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [1, 15, 14, 4],
                [12, 0, 0, 9],
                [8, 0, 0, 5],
                [13, 3, 2, 16]
            ],
            "answer": [
                [1, 15, 14, 4],
                [12, 0, 0, 9],
                [8, 0, 0, 5],
                [13, 3, 2, 16]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 0, 0, 0],
                [0, 14, 3, 0],
                [0, 11, 6, 0],
                [0, 0, 0, 0]
            ],
            "answer": [
                [0, 0, 0, 0],
                [0, 14, 3, 0],
                [0, 11, 6, 0],
                [0, 0, 0, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [2, 0, 0, 7],
                [0, 0, 6, 0],
                [0, 10, 0, 0],
                [11, 0, 0, 14]
            ],
            "answer": [
                [2, 0, 0, 7],
                [0, 0, 6, 0],
                [0, 10, 0, 0],
                [11, 0, 0, 14]
            ],
            "explanation": ""
        },

        {
            "input": [
                [3, 7, 14, 16, 25],
                [11, 0, 0, 0, 9],
                [22, 0, 0, 0, 18],
                [10, 0, 0, 0, 1],
                [19, 21, 5, 8, 12]
            ],
            "answer": [
                [3, 7, 14, 16, 25],
                [11, 0, 0, 0, 9],
                [22, 0, 0, 0, 18],
                [10, 0, 0, 0, 1],
                [19, 21, 5, 8, 12]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 7, 0, 16, 0],
                [11, 0, 23, 0, 9],
                [0, 4, 0, 15, 0],
                [10, 0, 17, 0, 1],
                [0, 21, 0, 8, 0]
            ],
            "answer": [
                [0, 7, 0, 16, 0],
                [11, 0, 23, 0, 9],
                [0, 4, 0, 15, 0],
                [10, 0, 17, 0, 1],
                [0, 21, 0, 8, 0]
            ],
            "explanation": ""
        }
    ],
    "Extra": [
        {
            "input": [
                [2, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "answer": [
                [2, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 0, 4],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "answer": [
                [0, 0, 4],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 0, 0, 0],
                [15, 14, 0, 0],
                [10, 11, 0, 0],
                [0, 0, 0, 0]
            ],
            "answer": [
                [0, 0, 0, 0],
                [15, 14, 0, 0],
                [10, 11, 0, 0],
                [0, 0, 0, 0]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 0, 14, 4],
                [0, 0, 0, 9],
                [0, 0, 0, 5],
                [0, 3, 0, 16]
            ],
            "answer": [
                [0, 0, 14, 4],
                [0, 0, 0, 9],
                [0, 0, 0, 5],
                [0, 3, 0, 16]
            ],
            "explanation": ""
        },
        {
            "input": [
                [0, 7, 0, 16, 0],
                [0, 0, 23, 0, 0],
                [0, 4, 0, 15, 0],
                [0, 0, 17, 0, 0],
                [0, 21, 0, 8, 0]
            ],
            "answer": [
                [0, 7, 0, 16, 0],
                [0, 0, 23, 0, 0],
                [0, 4, 0, 15, 0],
                [0, 0, 17, 0, 0],
                [0, 21, 0, 8, 0]
            ],
            "explanation": ""
        }
    ]
}