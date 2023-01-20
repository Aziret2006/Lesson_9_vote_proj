
user_database = []
questions = set()
counter = {}
agree_vote = 'Agree'
disagree_vote = 'Disagree'
neutral_vote = 'Neutral'



while True:
    choose = input("""  
            For AUTHRATION  press 1
            For REGISTRATION press 2
            For EXIT press 3
                    """)

    is_valid = []
    if choose == '1':
            pass
    elif choose == '2':
        name = input('Enter name:').strip()
        if name.isalpha() and 15 > len(name) > 2:
            name = name.capitalize()
            is_valid.append(True)
        else:
            print("Incorrect name!")
        surname = input("Enter surname: ").strip()
        if surname.isalpha() and 15 > len(surname) >= 2:
            surname = surname.capitalize()
            is_valid.append(True)
        else:
            is_valid.append(False)
            print("Incorrect last name")
        age = input("Enter age: ").strip()
        if age.isdigit() and 150 > int(age) > 0:
            age = int(age)
            is_valid.append(True)
        else:
            is_valid.append(False)
            print('Age was entered incorrect!')
        phone_number = input("Enter phone number, Example (0558705070):  ").strip()
        if phone_number.isdigit() and 10 == len(phone_number):
            phone_number = phone_number[0] + '(' + phone_number[1:4] + ')' + phone_number[4:8] + '-' + phone_number
            is_valid.append(True)
        else:
            is_valid.append(False)
            print('Phone number was entered incorrect (Example:0558705070) ')
        if all(is_valid):
           types_quetions = input("""
                Press 1 if your Theme: Social
                Press 2 if your Theme: Public
                Press 3 if your Theme: Economic
           """)
#          Social Questions
           if types_quetions == '1':
                user_action = input(""" 
                Press 1 to do question
                Press 2 to answer question    
                Press 3 to quet 
                """)
                if user_action == '1':
                    client_question = input("Please enter your question: ")
                    questions.add(client_question)
                    if not counter.get(client_question):
                        counter[client_question] = {
                                agree_vote: 0,
                                disagree_vote: 0,
                                neutral_vote: 0,
                                'total': 0
                                }
                        print(f"Your question {client_question} was added! \nThank for using our platform")
                elif user_action == '2':
                    for question in questions:
                        vote = input(f"""
                        Question: {question}                            
                                
                        Press 1 if you agree
                        Press 2 if you disagree    
                        Press 3 if you neutral
                        """)
                        if vote == '1':
                            counter[question]['Social'][agree_vote] += 1
                        elif vote == '2':
                            counter[question]['Social'][disagree_vote] += 1
                        elif vote == '3':
                            counter[question]['Social'][neutral_vote] += 1
                        else:
                            print("Incorrect vote")
                            continue
                        counter[question]['social']['total'] += 1
                elif user_action == '3':
                    for question, count in counter.items():
                        print(f"-> {question}, {count}\a")
                    print("See you")
                    break

#               Public Questions
                elif types_quetions == '2':
                   if user_action == '1':
                       client_question = input("Please enter your question: ")
                       questions.add(client_question)
                       if not counter.get(client_question):
                           counter[client_question] = {
                               agree_vote: 0,
                               disagree_vote: 0,
                               neutral_vote: 0,
                               'total': 0
                           }
                       print(f"Your question {client_question} was added! \nThank for using our platform")
                   elif user_action == '2':
                       for question in questions:
                           vote = input(f"""
                           Question: {question}                            
    
                           Press 1 if you agree
                           Press 2 if you disagree    
                           Press 3 if you neutral
                           """)
                           if vote == '1':
                               counter[question]['Public'][agree_vote] += 1
                           elif vote == '2':
                               counter[question]['Public'][disagree_vote] += 1
                           elif vote == '3':
                               counter[question]['Public'][neutral_vote] += 1
                           else:
                               print("Incorrect vote")
                               continue
                           counter[question]['social']['total'] += 1
                   elif user_action == '3':
                       for question, count in counter.items():
                           print(f"-> {question}, {count}\a")
                       print("See you")
                       break

#               Economic Questions
                elif types_quetions == '3':
                    if user_action == '1':
                        client_question = input("Please enter your question: ")
                        questions.add(client_question)
                        if not counter.get(client_question):
                            counter[client_question] = {
                                agree_vote: 0,
                                disagree_vote: 0,
                                neutral_vote: 0,
                                'total': 0
                            }
                        print(f"Your question {client_question} was added! \nThank for using our platform")
                    elif user_action == '2':
                        for question in questions:
                            vote = input(f"""
                            Question: {question}                            

                            Press 1 if you agree
                            Press 2 if you disagree    
                            Press 3 if you neutral
                            """)
                            if vote == '1':
                                counter[question]['Economic'][agree_vote] += 1
                            elif vote == '2':
                                counter[question]['Economic'][disagree_vote] += 1
                            elif vote == '3':
                                counter[question]['Economic'][neutral_vote] += 1
                            else:
                                print("Incorrect vote")
                                continue
                            counter[question]['social']['total'] += 1
                    elif user_action == '3':
                        for question, count in counter.items():
                            print(f"-> {question}, {count}\a")
                        print("See you")
                        break

        else:
            print("Goodbye = (")
            break