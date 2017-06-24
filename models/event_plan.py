class EventPlan(object):

    def __init__(self, name):
        self.name = name
        self.days = []

    def add_day(self, day_obj):
        self.days.append(day_obj)
