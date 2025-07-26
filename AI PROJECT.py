# AI Career Advisor Project
def ask_questions():
    print("Welcome to the AI Career Advisor!\nAnswer the following questions with Y/N:")

    q1 = input("Do you enjoy solving math problems? (Y/N): ").strip().lower()
    q2 = input("Do you like coding or building software? (Y/N): ").strip().lower()
    q3 = input("Are you interested in human anatomy or biology? (Y/N): ").strip().lower()
    q4 = input("Do you like drawing, designing, or creating visuals? (Y/N): ").strip().lower()
    q5 = input("Are you good at communicating and leading people? (Y/N): ").strip().lower()

    return q1, q2, q3, q4, q5

def suggest_career(answers):
    score = {
        "Engineer": 0,
        "Doctor": 0,
        "Artist": 0,
        "Manager": 0
    }

    q1, q2, q3, q4, q5 = answers

    if q1 == 'y':
        score["Engineer"] += 1
        score["Doctor"] += 1
    if q2 == 'y':
        score["Engineer"] += 2
    if q3 == 'y':
        score["Doctor"] += 2
    if q4 == 'y':
        score["Artist"] += 2
    if q5 == 'y':
        score["Manager"] += 2

    best_fit = max(score, key=score.get)
    return best_fit

def main():
    answers = ask_questions()
    career = suggest_career(answers)
    print(f"\n🔍 Based on your answers, a suitable career path for you is: **{career}**")

if __name__ == "__main__":
    main()
    print("\nRudra Vaja\n240905041036")
