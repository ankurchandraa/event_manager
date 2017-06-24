class DayPlan(object):

    def __init__(self, session_list):
        self.sessions = session_list

    def get_recent_session(self):
        if self.sessions:
            return self.sessions[-1]
        else:
            return None

    def can_schedule_talk(self, talk):

        for session in self.sessions:
            if session.get_remaining_duration() <= talk.get_duration():
                return True

        return False

    def schedule_talk(self, talk):

        for session in self.sessions:
            if session.get_remaining_duration() <= talk.get_duration():
                session.add_talk(talk)

