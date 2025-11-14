"""Simple CLI for the quiz app."""
import json
import sys
from importlib import resources


def load_questions():
    """Load quiz questions from package JSON data."""
    try:
        data_text = resources.read_text('quizapp', 'quiz_data.json')
    except Exception:
        # Fallback: attempt to open relative file (development)
        with open('./quiz_data.json', 'r', encoding='utf-8') as fh:
            data_text = fh.read()
    return json.loads(data_text)


def ask_question(q):
    print('\n' + q['question'])
    choices = q['options']
    labels = ['a', 'b', 'c', 'd']
    for label, choice in zip(labels, choices):
        print(f"  {label}) {choice}")

    while True:
        ans = input('Your answer (a/b/c/d): ').strip().lower()
        if ans in labels:
            return ans
        print('Please enter a, b, c or d')


def main():
    print('Welcome to the ML / Deep Learning quiz!')
    questions = load_questions()
    levels = list(questions.keys())
    print('Select difficulty:')
    for i, lvl in enumerate(levels, start=1):
        print(f"  {i}) {lvl}")

    choice = input('Enter 1/2/3: ').strip()
    try:
        idx = int(choice) - 1
        difficulty = levels[idx]
    except Exception:
        print('Invalid selection, defaulting to easy')
        difficulty = 'easy'

    quiz = questions.get(difficulty, [])
    if not quiz:
        print('No questions found.')
        sys.exit(1)

    score = 0
    for q in quiz:
        ans = ask_question(q)
        # correct answer stored as a single character: 'a'..'d'
        if ans == q.get('answer'):
            print('Correct!')
            score += 1
        else:
            correct_index = ord(q.get('answer')) - ord('a')
            correct_text = q['options'][correct_index]
            print(f"Wrong. Correct answer: {q.get('answer')}) {correct_text}")

    print(f"\nYou scored {score} out of {len(quiz)}")


if __name__ == '__main__':
    main()
