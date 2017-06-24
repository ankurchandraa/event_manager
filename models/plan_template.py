class PlanTemplate(object):

    def __init__(self, name, start_time, is_talk_allowed, end_time=None):
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        self.is_talk_allowed = is_talk_allowed
        self.remaining_duration = self.end_time - self.start_time
        self.talks = []

    def get_duration(self):
        return self.end_time - self.start_time

    def get_remaining_duration(self):
        return self.remaining_duration

    def decr_remaining_time(self, time):
        self.remaining_duration -= time

    def add_talk(self, talk_obj):
        self.talks.append(talk_obj)
        self.decr_remaining_time(talk_obj.get_duration())
