from list import ListControl
from test.integration.clitest.cli import CLITest
import pytest

object_types = ["Dataset", "Project", "Plate", "Screen"]


class TestList(CLITest):

    def setup_method(self, method):
        super(TestList, self).setup_method(method)
        self.cli.register("list", ListControl, "TEST")
        self.args += ["list"]

    @pytest.mark.parametrize("object_type", object_types)
    def test_list(self, capsys, object_type):
        name = self.uuid()
        oid = self.create_object(object_type, name=name)

        self.args += ['%s' % object_type]
        self.cli.invoke(self.args, strict=True)

        out, err = capsys.readouterr()
        assert 1 == len(out.splitlines())

        result = out.splitlines()[0]
        assert name in result
        assert str(oid) in result



