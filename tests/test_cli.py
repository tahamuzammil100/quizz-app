from unittest.mock import patch

from quizapp.cli import ask_question, load_questions


def test_load_questions():
    """
    Verifies that the load_questions function returns a dictionary with
    all required difficulty levels (easy, medium, hard).

    Returns:
        None

    Raises:
        AssertionError: If any difficulty level is missing.
    """
    questions = load_questions()
    assert isinstance(questions, dict)
    assert "easy" in questions
    assert "medium" in questions
    assert "hard" in questions


def test_question_structure():
    """
    Check that each question in all difficulty levels contains the required
    fields like question, options, and answer and that each question should
    have exact four options.

    Returns:
        None

    Raises:
        AssertionError: If any question is missing required fields or has
        incorrect number of options.
    """
    questions = load_questions()
    for difficulty in ["easy", "medium", "hard"]:
        assert len(questions[difficulty]) > 0
        for q in questions[difficulty]:
            assert "question" in q
            assert "options" in q
            assert "answer" in q
            assert len(q["options"]) == 4


def test_valid_answers():
    """
    Check that for every answer in every question across all difficulty levels
    is one of the valid answer choices of a, b, c, or d.

    Returns:
        None

    Raises:
        AssertionError: If any question has an invalid answer value.
    """
    questions = load_questions()
    for difficulty in questions:
        for q in questions[difficulty]:
            assert q["answer"] in ["a", "b", "c", "d"]


@patch("builtins.input", return_value="a")
@patch("builtins.print")
def test_ask_question(mock_print, mock_input):
    """
    Verifies that the ask_question function correctly handles valid user input
    and returns the answer provided by the user.

    Returns:
        None

    Raises:
        AssertionError: If the returned answer does not match the mocked input.
    """
    q = {"question": "Test?", "options": ["A", "B", "C", "D"], "answer": "a"}
    result = ask_question(q)
    assert result == "a"


@patch("builtins.input", side_effect=["x", "b"])
@patch("builtins.print")
def test_invalid_then_valid_input(mock_print, mock_input):
    """
    Verifies that the ask_question function rejects invalid input ('x') and
    continues to prompt until valid input is provided ('b'). This tests the
    input validation loop.

    Returns:
        None

    Raises:
        AssertionError: If the function does not return the valid answer after
        rejecting the invalid input.
    """
    q = {"question": "Test?", "options": ["A", "B", "C", "D"], "answer": "b"}
    result = ask_question(q)
    assert result == "b"
