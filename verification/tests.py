"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [3, 2],
            "answer": '11',
            "explanation": "bin(3)?"
        },
        {
            "input": [5, 7],
            "answer": '5',
            "explanation": "5%7=?"
        }
        ,
        {
            "input": [7, 7],
            "answer": '10',
            "explanation": "1*7 + 0 * 1 = 7"
        },
        {
            "input": [8, 7],
            "answer": '10',
            "explanation": "1*7 + 1 * 1 = 8"
        }
    ],
    "Extra": [
        {
            "input": [6, 10],
            "answer": '6',
         },
        {
            "input": [6, 16],
            "answer": '6',
         },
        {
            "input": [32767, 16],
            "answer": '7FFF',
         },
        {
            "input": [77777, 16],
            "answer": '12FD1',
        },
        {
            "input": [895210, 16],
            "answer": 'DA8EA',
         },
        {
            "input": [9999, 16],
            "answer": '270F',
         }, {
            "input": [8, 3],
            "answer": '22',
         },
        {
            "input": [0, 16],
            "answer": '0',
         }, {
            "input": [0, 3],
            "answer": '0',
         }
            ]
}
