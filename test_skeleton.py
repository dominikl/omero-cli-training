from xyz import XYZControl
from test.integration.clitest.cli import CLITest
import pytest

# some parameter values to test
test_arguments = ["argument0_value0", "argument0_value1", "argument0_value2"]


class XYZList(CLITest):

    def setup_method(self, method):
        super(XYZList, self).setup_method(method)
        self.cli.register("xyz", XYZControl, "TEST")
        self.args += ["xyz"]
    
    @pytest.mark.parametrize("test_arguments", arg)
    def test_xyz(self, capsys, arg):
        
        # assemble the arguments and invoke CLI
        self.args += ['%s' % object_type]
        self.cli.invoke(self.args, strict=True)

        # capture and check the output
        out, err = capsys.readouterr()
        assert out is not None
