from pytest import fixture

from model.skills.skill import Skill


@fixture
def skill():
    return Skill(name='Demolition Expert', cost=1)


def test_skill_has_correct_attributes(skill):
    assert skill._name == 'Demolition Expert'
    assert skill._cost == 1


def test_skill_name_returns_correct_value(skill):
    assert skill.name == skill._name


def test_skill_cost_returns_correct_value(skill):
    assert skill.cost == skill._cost
