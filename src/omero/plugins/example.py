import sys
from omero.cli import BaseControl, CLI
from omero.gateway import BlitzGateway

HELP = """This is just an example CLI plugin."""


class ExampleControl(BaseControl):
    """
    Example OMERO CLI Plugin
    """

    def _configure(self, parser):
        # add the default login arguments to the command line parser
        parser.add_login_arguments()

        # add some arguments
        parser.add_argument(
            "test",
            help="This is a mandatory, positional argument")
        parser.add_argument(
            "--flag", action="store_true",
            help="This is an optional flag")

        # set the entry method which is called when this
        # plugin is executed
        parser.set_defaults(func=self.__call__)

    def __call__(self, args):
        try:
            # connect to the OMERO server
            client = self.ctx.conn(args)

            # use the BlitzGateway to interact with the server
            gateway = BlitzGateway(client_obj=client)
            userId = gateway.getUserId()

            self.ctx.out("test was %s" % args.test)
            self.ctx.out("--flag was %s" % args.flag)
            self.ctx.out("And my user ID is %s" % userId)
        except Exception, e:
            self.ctx.err('ERROR: %s' % e)
            self.ctx.die(1, "Connection failed")


try:
    register("example", ExampleControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("list", ExampleControl, HELP)
        cli.invoke(sys.argv[1:])
