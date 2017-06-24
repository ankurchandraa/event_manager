from models.plan_template import PlanTemplate


class EventRule(object):
    def __init__(self):
        self.session_list = []
        self.add_new_session(PlanTemplate(name="Morning", start_time=0, end_time=180, is_talk_allowed=True))
        self.add_new_session(PlanTemplate(name="Lunch", start_time=180, end_time=240, is_talk_allowed=False))
        self.add_new_session(PlanTemplate(name="Evening", start_time=240, end_time=480, is_talk_allowed=True))
        self.add_new_session(PlanTemplate(name="Networking", start_time=480, end_time=1440, is_talk_allowed=False))

    def add_new_session(self, plan_template):
        self.session_list.append(plan_template)

    def get_session_list(self):
        return self.session_list