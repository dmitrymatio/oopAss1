import csv
import ast


class Reminder():

    def __init__(self, id, tags, text):
        self.__id = id
        self.__text = text
        self.__tags = tags

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if type(id) == int:
            self.__id = id
        else:
            print('Error: Id must be an integer')

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if type(text) == str:
            self.__text = text
        else:
            print('Error: text must be a string')

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, tags):
        if type(tags) == list:
            self.__tags = tags
        else:
            print('Error: tags must be a list')

    def getRem(self):
        return f'''
        Reminder {self.id},
        Tags: {self.tags},
                        '{self.text}'
        '''


class ListOfReminders():

    def __init__(self):
        self.reminders = []

    def addReminder(self, reminder):
        self.reminders.insert(0, reminder)
        print(f'Reminder added. id # = {reminder.id}')

    def showReminders(self):
        for reminder in self.reminders:
            print(reminder.getRem())

    def modReminder(self, id, tags, text):
        rem = Reminder(id, tags, text)
        self.reminders[-id] = rem

    def searchReminders(self, term):
        for reminder in self.reminders:
            if term in reminder.tags or term in reminder.text:
                print(reminder.getRem())
            else:
                print('No reminder found')

    def exportRems(self, fileName):
        exports = []
        for rem in self.reminders:
            exports.append([rem.tags,rem.text])
        with open(f'{fileName}.csv', mode='w') as exportFile:
            remWriter = csv.writer(exportFile, delimiter=',')
            for rem in exports:
                remWriter.writerow(rem)

    def importRems(self, fileName):
        imports = []
        try:
            file = open(f'{fileName}.csv', 'r')
        except IOError:
            print('File doesnt exist')
            return
        with open(f'{fileName}.csv', mode='r') as importFile:
            remReader = csv.reader(importFile, delimiter=',')
            for rem in remReader:
                imports.append(rem)
        print(imports)
        return imports
        


class Comp():

    menu = '''
    Reminders menu:

    1. show all reminders
    2. search reminders
    3. add reminders
    4. modify reminders
    5. export reminders
    6. import reminders
    7. quit

    Select option by number:
    '''
    @classmethod
    def boot(cls):
        remList = ListOfReminders()
        exit = False
        while not exit:
            userInput = int(input(cls.menu))
            if (userInput == 1):
                remList.showReminders()
            elif (userInput == 2):
                searchInput = input('Search for:')
                remList.searchReminders(searchInput)
            elif (userInput == 3):
                id = len(remList.reminders) + 1
                tagsInput = input('Tags separated by comma:')
                if ' ' in tagsInput:
                    print('Error: tags must be separated by commas')
                else:
                    textInput = input('Reminder text:')
                    tags = tagsInput.split(',')
                    if (textInput != ''):
                        rem = Reminder(id, tags, textInput)
                        remList.addReminder(rem)
                    else:
                        print('Error: Reminder must have text')
            elif (userInput == 4):
                idInput = int(input('Select reminder by id:'))
                if (len(remList.reminders) >= idInput):
                    oldRem = remList.reminders[-idInput]
                    print(oldRem.getRem())
                    tagsInput = input(
                        'Tags edit comma separated, "delete", or "no edit":')
                    if(tagsInput == 'delete'):
                        tags = []
                    elif(tagsInput == 'no edit' or tagsInput == ''):
                        tags = oldRem.tags
                    else:
                        tags = tagsInput.split(',')
                    textInput = input('Text edit, "delete", or "no edit":')                
                    if(textInput == 'no edit' or textInput == ''):
                        text = oldRem.text
                    else:
                        text = textInput
                    remList.modReminder(idInput, tags, text)
                    print(remList.reminders[-idInput].getRem())
                else:
                    print('Error: id doesnt exist')
            elif(userInput == 5):
                fileName = input('File Name:')
                remList.exportRems(fileName)
            elif(userInput == 6):
                fileName = input('File Name:')
                imports = remList.importRems(fileName)
                for rem in imports:
                    tags = ast.literal_eval(rem[0])
                    text = rem[1]
                    id = len(remList.reminders) + 1
                    importRem = Reminder(id, tags, text)
                    remList.addReminder(importRem)
            elif(userInput == 7):
                exit = True
            else:
                print('Option doesnt exist')
