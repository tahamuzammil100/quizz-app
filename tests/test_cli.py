from unittest.mock import patch

from quizapp.cli import ask_question, load_questions


def test_load_questions():
    """Test that questions load successfully."""
    questions = load_questions()
    assert isinstance(questions, dict)
    assert "easy" in questions
    assert "medium" in questions
    assert "hard" in questions


def test_question_structure():
    """Test that questions have correct structure."""
    questions = load_questions()
    for difficulty in ["easy", "medium", "hard"]:
        assert len(questions[difficulty]) > 0
        for q in questions[difficulty]:
            assert "question" in q
            assert "options" in q
            assert "answer" in q
            assert len(q["options"]) == 4


def test_valid_answers():
    """Test that all answers are valid (a, b, c, or d)."""
    questions = load_questions()
    for difficulty in questions:
        for q in questions[difficulty]:
            assert q["answer"] in ["a", "b", "c", "d"]


@patch("builtins.input", return_value="a")
@patch("builtins.print")
def test_ask_question(mock_print, mock_input):
    """Test asking a question."""
    q = {"question": "Test?", "options": ["A", "B", "C", "D"], "answer": "a"}
    result = ask_question(q)
    assert result == "a"


@patch("builtins.input", side_effect=["x", "b"])
@patch("builtins.print")
def test_invalid_then_valid_input(mock_print, mock_input):
    """Test that invalid input is rejected."""
    q = {"question": "Test?", "options": ["A", "B", "C", "D"], "answer": "b"}
    result = ask_question(q)
    assert result == "b"
