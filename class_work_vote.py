questions = set()
counter = {}

# questions = {
#     'social_question': [],
#     'economic_question': []
# }


# counter = {
#     '2 + 2': {
#             '1': 2,
#             '2': 0,
#             '3': 1,
#             'total': 3
#         },
#     '3 + 3': {
#             '1': 10,
#             '2': 2,
#             '3': 0,
#             'total': 12
#         },
#     }

agree_vote = 'agree'
disagree_vote = 'disagree'
neitral_vote = 'neitral'

while True:
    action = input("""
    Press 1 to add question
    Press 2 to answer question
    Press 3 to quit
                   """)

    if action == '1':
        client_question = input('Enter your question: ')
        questions.add(client_question)
        if not counter.get(client_question):
            counter[client_question] = {
                agree_vote: 0,
                disagree_vote: 0,
                neitral_vote: 0,
                'total': 0
            }
        print('Your question added! Thanks for using our platform!')
    elif action == '2':
        for question in questions:
            # print(question)
            vote = input(f"""
            {question}

            Press 1 if you agree
            Press 2 if you disagree
            Press 3 if you neitral
                         """)

            if vote == '1':
                counter[question][agree_vote] += 1
            elif vote == '2':
                counter[question][disagree_vote] += 1
            elif vote == '3':
                counter[question][neitral_vote] += 1
            else:
                print('Inccorect vote!')
                continue
            counter[question]['total'] += 1
    elif action == '3':
        for question, count in counter.items():
            print(question, count)
        print('Goodbye see you!')
        break

