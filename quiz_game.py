def quiz():
    score = 0

    print("===== Welcome to Quiz Game =====\n")

    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "b"
        },
        {
            "question": "2. Who is known as Father of Computer?",
            "options": ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "b"
        },
        {
            "question": "3. 5 + 5 = ?",
            "options": ["A. 8", "B. 9", "C. 10", "D. 11"],
            "answer": "c"
        },
        {
            "question": "4. Which language is used for web development?",
            "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
            "answer": "c"
        },
        {
            "question": "5. National animal of India?",
            "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Deer"],
            "answer": "b"
        },
        {
            "question": "6. Who invented Python?",
            "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
            "answer": "c"
        },
        {
            "question": "7. 10 * 2 = ?",
            "options": ["A. 20", "B. 10", "C. 15", "D. 25"],
            "answer": "a"
        },
        {
            "question": "8. Which planet is known as Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "c"
        },
        {
            "question": "9. CPU stands for?",
            "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Control Processing Unit", "D. Central Program Unit"],
            "answer": "a"
        },
        {
            "question": "10. RAM stands for?",
            "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Access Memory", "D. Real Access Memory"],
            "answer": "b"
        }
    ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user = input("Enter your answer (A/B/C/D): ").lower()

        if user == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is:", q["answer"].upper(), "\n")

    print("===== Quiz Finished =====")
    print("Your Score:", score, "/10")

quiz()
