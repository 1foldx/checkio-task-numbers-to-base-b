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
            "input": [77777, 16],
            "answer": '7FFF',
         }
        ,
        {
            "input": [9999, 16],
            "answer": '270F',
         }
    ]
}
