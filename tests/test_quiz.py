import builtins
import io
import json
from importlib import resources

from src.quizapp import __version__
from src.quizapp import cli


def test_version():
    assert __version__ == "0.1.0"


def test_load_questions_structure():
    data = cli.load_questions()
    # should have three difficulty levels
    assert set(data.keys()) == {"easy", "medium", "hard"}
    # each level should have at least one question
    for lvl in data:
        assert isinstance(data[lvl], list)
        assert len(data[lvl]) >= 1


def test_each_question_has_expected_fields():
    data = cli.load_questions()
    for lvl, questions in data.items():
        for q in questions:
            assert 'question' in q
            assert 'options' in q and isinstance(q['options'], list)
            assert len(q['options']) == 4
            assert 'answer' in q
            assert q['answer'] in ('a', 'b', 'c', 'd')


def test_ask_question_accepts_valid_input(monkeypatch, capsys):
    data = cli.load_questions()
    q = data['easy'][0]

    # simulate user entering 'b'
    monkeypatch.setattr('builtins.input', lambda prompt='': 'b')
    ans = cli.ask_question(q)
    assert ans == 'b'


def test_main_flow_with_mocked_inputs(monkeypatch, capsys):
    # simulate selecting 'easy' (1) and answering each question with 'a'
    data = cli.load_questions()
    num_questions = len(data['easy'])
    inputs = iter(['1'] + ['a'] * num_questions)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))

    # run main (should not raise)
    cli.main()
    captured = capsys.readouterr()
    # ensure score line is printed
    assert 'You scored' in captured.out
