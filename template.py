import sys
from omero.cli import BaseControl, CLI

HELP = """What this plugin does"""

class XYZControl(BaseControl):
    """
    Some documentation
    """

    def _configure(self, parser):
        parser.add_argument(
            "some_argument",
            help="What this argument does")
        parser.set_defaults(func=self.__call__)

    def __call__(self, args):
        # Dispatch to certain methods depending on args
        self.some_method(args.some_argument)

    def some_method(self, some_argument):
        print("Do something with "+some_argument)

try:
    register("xyz", ListControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("xyz", XYZControl, HELP)
        cli.invoke(sys.argv[1:])
