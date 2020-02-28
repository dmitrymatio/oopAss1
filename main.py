menu = """
Reminders menu:

1. show all reminders
2. search reminders
3. add reminders
4. modify reminders
5. export reminders
6. import reminders
7. quit
"""

class Reminder():
    def __init__(self, id, tags, text):
        self.id = id
        self.text = text
        self.tags = tags
    
    def getRem(self):
        return f"""
        Reminder {self.id}, 
        Tags: {self.tags},
                        '{self.text}''   
        """

class ReminderList():
    def __init__(self):
        self.reminders = []
    def addReminder(self,reminder):
        self.reminders.insert(0,reminder)
        print(f"Reminder added. id # = {reminder.id}")
    def showReminders(self):
        for reminder in self.reminders:
            print(reminder.getRem())
    def modReminder(self, id, tags, text):
        select = self.reminders[-id].getRem()
        print(select)


reminder1 = Reminder(1,911,"Hello world")
reminder2 = Reminder(2,911,"Hello world")
reminder3 = Reminder(3,911,"Hello world")

list = ReminderList()

list.addReminder(reminder1)
list.addReminder(reminder2)
list.addReminder(reminder3)
list.showReminders()
list.modReminder(1,1,1)
list.modReminder(2,1,1)
list.modReminder(3,1,1)


