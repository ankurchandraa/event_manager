from models.day_plan import DayPlan
from models.plan_template import PlanTemplate
from models.talk_template import TalkTemplate


class EventScheduler(object):

    def __init__(self, event_list, event_rule_obj):
        self.event_list = event_list
        self.event_rule = event_rule_obj
        self.session_list = event_rule_obj.get_session_list()

    def make_plan(self):

        day_plan = DayPlan(self.event_rule.get_session_list())

        for event in self.event_list:
            talk = TalkTemplate(event['name'], event['duration'])
            is_schedulable = day_plan.can_schedule_talk(talk)
            if is_schedulable:
                day_plan.schedule_talk(talk)
            else:
                day_plan = DayPlan(self.event_rule.get_session_list())
                day_plan.schedule_talk(talk)


