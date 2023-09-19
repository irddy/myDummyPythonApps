# Add a dictionary to store questions and answers
# looping through a dictionary using key value pair
# variable to track score 
# display each question to user 
# allow them to answer 
# show the result and the correct answer 
# show complete player results 



quiz = { 
    "question1" : {
        "question": "Whats the captital of Albania?",
        "answer" :"Tirana"
    },
    "question2" : {
        "question" : "What is the capital of Spain?",
        "answer" : "Madrid"
    },
    "question3" : {
        "question": "What is the capital of Russia?",
        "answer" : "Moscow"
    },
    "question4" : {
        "question": "Whats the captital of Albania?",
        "answer" :"Tirana"
    },
    "question5" : {
        "question" : "What is the capital of Spain?",
        "answer" : "Madrid"
    },
    "question6" : {
        "question": "What is the capital of Russia?",
        "answer" : "Moscow"
    }
    
}

score = 0 

for key, value in quiz.items(): 
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower(): 
        print("Correct")
        score = score +1 
        print("Your Score is: " + str(score))
    else: 
        print("Wrong")
        print("The correct answer is: " + value['answer'])
        print("Your Score is: " + str(score))
















