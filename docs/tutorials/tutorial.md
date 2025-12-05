   # Quiz App Tutorial

   ## What is this app?

   This is a simple command line quiz game about Machine Learning and Deep Learning. You answer
    multiple choice questions and get a score at the end. Pretty straightforward!

   ## Installation & Setup

   ### Before you start
   Make sure you have Python 3.8+ installed on your computer.

   ### Steps

   1. **Clone the project** (if you haven't already)
      ```bash
      git clone https://github.com/tahamuzammil100/quizz-app.git
      cd quizz-app
      ```

   2. **Install dependencies**
      The project uses Poetry for managing dependencies. If you don't have Poetry installed:
      ```bash
      curl -sSL https://install.python-poetry.org | python3 -
      ```

   3. **Install the project**
      ```bash
      poetry install
      ```

   ## Running the Quiz

   It's super easy! Just run:

   ```bash
   poetry run python -m quizapp.cli
   ```

   That's it! The quiz will start.

   ## How to Use the Quiz

   When you run the app, here's what happens:

   1. **Pick a difficulty level** - The app will ask you to choose:
      - Type `1` for Easy
      - Type `2` for Medium
      - Type `3` for Hard

   2. **Answer the questions** - For each question:
      - You'll see the question text
      - Read all 4 options (a, b, c, d)
      - Type your answer (a, b, c, or d)
      - Press Enter

   3. **Get instant feedback** - The app tells you if you're right or wrong

   4. **See your score** - After all questions, you get a final score!

   ## Example Session

   ```
   === ML/DL Quiz ===
   Pick difficulty: (1=Easy, 2=Medium, 3=Hard)
   > 1

   Question 1: What does ML stand for?
   a) Machine Learning
   b) Media Library
   c) Manual Labor
   d) Metal League

   Your answer: a
   ✓ Correct!

   Question 2: What is a neural network?
   ...
   ```

   ## Tips

   - Don't worry if you get questions wrong - it's a learning tool!
   - Easy mode is good if you're new to ML
   - Hard mode is for people who know their stuff
   - Your answers get logged, so you can check your progress later

   ## Running Tests

   Want to make sure everything is working? Run the tests:

   ```bash
   poetry run pytest
   ```
