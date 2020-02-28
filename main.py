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


class ListOfReminders():

    def __init__(self):
        self.reminders = []

    def addReminder(self, reminder):
        self.reminders.insert(0, reminder)
        print(f"Reminder added. id # = {reminder.id}")

    def showReminders(self):
        for reminder in self.reminders:
            print(reminder.getRem())

    def modReminder(self, id, tags, text):
        select = self.reminders[-id].getRem()
        print(select)

    def exportRems(self):
        pass

    def importRems(self):
        pass


class remindersComp():
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

    @classmethod
    def runComp(cls):
        remList = ListOfReminders()
        
        exit = False
        while not exit:
            userInput = int(input(cls.menu))
            print(userInput)
            if (userInput == 3):
                rem1 = Reminder(1, ['911','family'], "hello world 1")
                remList.addReminder(rem1)
                remList.showReminders()
            exit = True



remindersComp.runComp()