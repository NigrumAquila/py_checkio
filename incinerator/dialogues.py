VOWELS = "aeiouAEIOU"

class Chat:
    
    def __init__(self):
        self.human_dialogue = []
        self.robot_dialogue = []
    
    def connect_human(self, human):
        human.chat = self
        
    def connect_robot(self, robot):
        robot.chat = self
        
    def show_human_dialogue(self):
        print("\n".join(self.human_dialogue))
        return "\n".join(self.human_dialogue)
        
    def show_robot_dialogue(self):
        print("\n".join(self.robot_dialogue))
        return "\n".join(self.robot_dialogue)
        

class Human:
    
    def __init__(self, name):
        self.name = name
        
    def send(self, message):
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(self.name + " said: " + robot_message)
        self.chat.human_dialogue.append(self.name + " said: " + message)

class Robot:
    
    def __init__(self, serial_number):
        self.serial_number = serial_number
        
    def send(self, message):
        self.chat.human_dialogue.append(self.serial_number + " said: " + message)
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(self.serial_number + " said: " + robot_message)