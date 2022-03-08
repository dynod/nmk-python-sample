from pytest_multilog import TestHelper

from mymodule.sample import my_sample_function


class TestMyThing(TestHelper):
    def test_foo(self):
        assert my_sample_function(12) == 12
