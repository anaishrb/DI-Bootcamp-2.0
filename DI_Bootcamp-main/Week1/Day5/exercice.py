data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def star_quiz(data):
    for dict_question in data:
        print(dict_question['question'])
        u_answer = input('write your answer: ')
        if u_answer is dict_question['answer']:
            right += 1
        else:
            wrong += 1
    return wrong, right
print(star_quiz(data))



def score_board():
    pass

def final_leader():
    pass
