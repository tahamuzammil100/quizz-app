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
    """
    Loads questions for quizz from JSON file. First it will attempts to load
    data file from the package resources, if falls than load from local file path.

    Returns:
        dict: A dictionary with difficulty levels as keys ('easy', 'medium',
            'hard') and lists of question dictionaries as values. Each question
            contains 'question', 'options', and 'answer' key-value pairs.
    """

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
    """
    Displays a multiple-choice question with four options (a, b, c, d) and
    repeatedly prompts the user for input until a valid answer out of (a, b, c, d)
    is not provided.

    Args:
        q (dict): A question dictionary containing:
            - 'question' (str): The question text to display
            - 'options' (list): A list of four answer options
            - 'answer' (str): The correct answer ('a', 'b', 'c', or 'd')

    Returns:
        str: The user's answer as a single character ('a', 'b', 'c', or 'd').
    """
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
    """
    The user is presented with three difficulty options (easy, medium and hard).
    If an invalid selection is made out of hese, application will pick default and
    set difficulty to 'easy'. If no questions are found for the selected difficulty,
    the application exits with an error.

    Returns:
        None

    """

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
