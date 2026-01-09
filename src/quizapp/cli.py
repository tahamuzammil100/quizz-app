import json
import logging
import os
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

# Redis connection
redis_client = None


def init_redis():
    """Initialize Redis connection if available."""
    global redis_client
    try:
        import redis

        redis_host = os.getenv("REDIS_HOST", "localhost")
        redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)
        redis_client.ping()
        logger.info(f"Connected to Redis at {redis_host}")
        return True
    except Exception as e:
        logger.warning(f"Redis not available: {e}")
        return False


def save_score(player_name, difficulty, score, total):
    """Save score to Redis."""
    if redis_client:
        try:
            key = f"scores:{difficulty}"
            redis_client.zadd(key, {player_name: score})
            redis_client.lpush("recent_scores", f"{player_name}: {score}/{total} ({difficulty})")
            redis_client.ltrim("recent_scores", 0, 9)  # Keep last 10
            logger.info("Score saved to Redis!")
        except Exception as e:
            logger.warning(f"Could not save score: {e}")


def show_leaderboard(difficulty):
    """Show top scores for difficulty level."""
    if redis_client:
        try:
            key = f"scores:{difficulty}"
            top_scores = redis_client.zrevrange(key, 0, 4, withscores=True)
            if top_scores:
                print(f"\n🏆 Leaderboard ({difficulty}):")
                for i, (name, score) in enumerate(top_scores, 1):
                    print(f"  {i}. {name}: {int(score)} points")
            else:
                print(f"\nNo scores yet for {difficulty} difficulty.")
        except Exception as e:
            logger.warning(f"Could not fetch leaderboard: {e}")


def load_questions():
    """Load questions from JSON file."""
    logger.info("Loading quiz questions")
    try:
        data_text = files("quizapp").joinpath("quiz_data.json").read_text(encoding="utf-8")
    except Exception:
        logger.warning("Could not load from package, using fallback")
        with open("./quiz_data.json", encoding="utf-8") as fh:
            data_text = fh.read()
    return json.loads(data_text)


def ask_question(q):
    """Display question and get user answer."""
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
    """Main quiz function."""
    logger.info("Welcome to the ML / Deep Learning quiz!")

    # Try to connect to Redis
    redis_available = init_redis()

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

    # Show leaderboard before starting
    if redis_available:
        show_leaderboard(difficulty)

    quiz = questions.get(difficulty, [])
    if not quiz:
        logger.error("No questions found!")
        sys.exit(1)

    score = 0
    for q in quiz:
        ans = ask_question(q)
        if ans == q.get("answer"):
            print("Correct!")
            score += 1
        else:
            correct_index = ord(q.get("answer")) - ord("a")
            correct_text = q["options"][correct_index]
            print(f"Wrong. Correct answer: {q.get('answer')}) {correct_text}")

    logger.info(f"Quiz completed - Score: {score}/{len(quiz)}")

    # Save score to Redis
    if redis_available:
        player_name = input("\nEnter your name for the leaderboard: ").strip()
        if player_name:
            save_score(player_name, difficulty, score, len(quiz))
            show_leaderboard(difficulty)


if __name__ == "__main__":
    main()
