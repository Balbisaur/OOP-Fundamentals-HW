class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0  

        def add_participant(self):
            self.participant_count += 1

        def get_participant_count(self):
            return self.participant_count




event = Event("Myrons Party", "Nov-13-2024")

    
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()

print("Participant Count:", event.get_participant_count())