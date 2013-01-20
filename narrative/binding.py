class EntrySupport(object):
    mixin = 'Entry'

    class Reporter(object):
        def __init__(self, model, subject=None):
            if subject:
                subject = subject.strip(':')

            self.model = model
            self.subject = subject

        def __call__(self, tag, subject=None, entry=None, importance='normal', **aspects):
            if subject:
                subject = subject.strip(':')
                if self.subject:
                    subject = '%s:%s' % (self.subject, subject)
            elif self.subject:
                subject = self.subject
            else:
                raise ValueError(subject)

            return self.model.create(subject=subject, tag=tag, entry=entry,
                importance=importance, aspects=aspects)

    @classmethod
    def reporter(cls, subject=None):
        return cls.Reporter(cls, subject)
