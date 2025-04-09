def get_feedback():
    feedback = input("Enter your feedback: ")
    score = int(input("Enter your score (1-5): "))
    return {"feedback": feedback, "score": score}
