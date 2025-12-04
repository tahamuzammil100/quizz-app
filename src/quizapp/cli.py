import json
import logging
import sys
from importlib.resources import files

# Simple logging setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", filename="quizapp.log")

# Add console handler for screen output
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logging.getLogger().addHandler(console_handler)

logger = logging.getLogger(__name__)


def load_questions():
    """Load quiz questions from package JSON data."""
    logger.info("Loading quiz questions")
    try:
        data_text = files("quizapp").joinpath("quiz_data.json").read_text(encoding="utf-8")
    except Exception:
        logger.warning("Could not load from package, using fallback")
        # Fallback: attempt to open relative file (development)
        with open("./quiz_data.json", encoding="utf-8") as fh:
            data_text = fh.read()
    return json.loads(data_text)


def ask_question(q):
    """Ask a single question and return the user's answer."""
    print("\n" + q["question"])
    choices = q["options"]
    labels = ["a", "b", "c", "d"]
    for label, choice in zip(labels, choices):
        print(f"  {label}) {choice}")

    while True:
        ans = input("Your answer (a/b/c/d): ").strip().lower()
        if ans in labels:
            return ans
        print("Please enter a, b, c or d")


def main():
    """Main entry point for the quiz application."""

    logger.info("Welcome to the ML / Deep Learning quiz!")
    questions = load_questions()
    levels = list(questions.keys())
    print("Select difficulty:")
    for i, lvl in enumerate(levels, start=1):
        print(f"  {i}) {lvl}")

    choice = input("Enter 1/2/3: ").strip()
    try:
        idx = int(choice) - 1
        difficulty = levels[idx]
        logger.info(f"Selected difficulty: {difficulty}")
    except Exception:
        logger.warning("Invalid selection, using default")
        logger.warning("Mode: Easy")
        difficulty = "easy"

    quiz = questions.get(difficulty, [])
    if not quiz:
        logger.error("No questions found!")
        sys.exit(1)

    score = 0
    for q in quiz:
        ans = ask_question(q)
        # correct answer stored as a single character: 'a'..'d'
        if ans == q.get("answer"):
            print("Correct!")
            score += 1
        else:
            correct_index = ord(q.get("answer")) - ord("a")
            correct_text = q["options"][correct_index]
            print(f"Wrong. Correct answer: {q.get('answer')}) {correct_text}")

    logger.info(f"Quiz completed - Score: {score}/{len(quiz)}")


if __name__ == "__main__":
    main()
