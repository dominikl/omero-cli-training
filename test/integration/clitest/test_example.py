from example import ExampleControl
from test.integration.clitest.cli import CLITest
import pytest

arguments = ["test", "123", "bla"]


class TestExample(CLITest):

    def setup_method(self, method):
        super(TestExample, self).setup_method(method)
        self.cli.register("example", ExampleControl, "TEST")
        self.args += ["example"]

    @pytest.mark.parametrize("argument", arguments)
    def test_example(self, capsys, argument):
        self.args += ['%s' % argument]
        self.cli.invoke(self.args, strict=True)

        out, err = capsys.readouterr()
        assert argument in out
