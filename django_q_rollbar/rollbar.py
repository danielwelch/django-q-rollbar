import rollbar


class Rollbar(object):

    def __init__(self, **kwargs):
        if not rollbar._initialized:
            rollbar.init(**kwargs)

    def report(self):
        rollbar.report_exc_info()
