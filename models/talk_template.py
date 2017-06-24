class TalkTemplate(object):

    def __init__(self, name, duration, is_active=True):
        self.name = name
        self.duration = duration
        self.is_active = is_active

    def get_duration(self):
        return self.duration

