import sys
import omero
from omero.cli import BaseControl, CLI

HELP = """List datasets, projects, screens and plates for the logged in user."""


class ListControl(BaseControl):
    """
    Example OMERO CLI Plugin
    """

    def _configure(self, parser):
        parser.add_login_arguments()
        parser.add_argument(
            "type",
            help="The type of objects to list: 'Dataset', 'Project', 'Screen' or 'Plate'")
        parser.set_defaults(func=self.__call__)

    def __call__(self, args):
        self.c = self.ctx.conn(args)
        self.list(args.type)

    def list(self, klass):
        if klass == 'Project' \
                or klass == 'Dataset' \
                or klass == 'Screen' \
                or klass == 'Plate':
            p = omero.sys.ParametersI()
            p.leaves()

            objs = self.c.sf.getContainerService().loadContainerHierarchy(klass,
                                                                          None, p)
            for obj in objs:
                self.ctx.out("%s (id = %s)." % (obj.name.val, obj.id.val))
        else:
            self.ctx.err("%s not supported." % objectType)


try:
    register("list", ListControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("list", ListControl, HELP)
        cli.invoke(sys.argv[1:])
