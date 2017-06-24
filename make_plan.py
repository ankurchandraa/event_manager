from event_list import event_list
from event_scheduler.scheduler import EventScheduler
from models.event_rule import EventRule

if __name__ == '__main__':

    event_rule = EventRule()
    scheduler = EventScheduler(event_list, event_rule)

    scheduler.make_plan()