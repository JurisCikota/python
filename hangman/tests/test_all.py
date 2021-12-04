from model.scripts.word_weight import Score


def test_Score_attribute_exists():
    score = Score("word")
    assert hasattr(score, "word")

def test_syllables_score():
    score = Score("syllables")
    syll_score = score.syllables_score()
    assert syll_score == 30

def test_unique_score():
    score = Score("unique")
    uniq_score = score.unique_score()
    assert uniq_score == 10