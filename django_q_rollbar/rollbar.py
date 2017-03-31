import rollbar


class Rollbar(object):

    def __init__(self, **kwargs):
        rollbar.init(**kwargs)

    def report(self):
        rollbar.report_exc_info()
