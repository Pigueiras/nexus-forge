import pytest
from pytest_bdd import given, scenario, then

from kgforge.core.resources import Resource, Resources


def _resources():
    r1 = Resource(index=0)
    r2 = Resource(index=1)
    return [r1, r2]


@pytest.mark.parametrize("collection", [
    pytest.param(_resources(), id="list"),
    pytest.param(iter(_resources()), id="iterator")])
@scenario(
    "resources.feature",
    "Create a Resources object from a collection of resources.")
def test_creation(collection):
    pass


@given("I create a Resources object from a collection of resources.")
def resources(collection):
    return Resources(collection)


@then("I should be able to count the number of resources with len().")
def count_resources(resources):
    assert len(resources) == 2


@then("The Resource objects should be in the same order as inserted.")
def check_order(resources):
    assert resources[0].index == 0
    assert resources[1].index == 1
