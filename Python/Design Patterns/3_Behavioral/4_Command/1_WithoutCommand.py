class Light:
    def on(self):
        print("Light turned ON")

    def off(self):
            print("Light turned OFF")

class AC:
    def on(self):
            print("AC turned ON")

    def off(self):
            print("AC turned OFF")

# Invoker
class RemoteControl:
    def __init__(self, light, ac):
        self.light = light
        self.ac = ac
        self.last_action = ""

    # Command methods
    def press_light_on(self):
        self.light.on()
        self.last_action = "LIGHT_ON"

    def press_light_off(self):
        self.light.off()
        self.last_action = "LIGHT_OFF"

    def press_ac_on(self):
        self.ac.on()
        self.last_action = "AC_ON"

    def press_ac_off(self):
        self.ac.off()
        self.last_action = "AC_OFF"

    def press_undo(self):
        if self.last_action == "LIGHT_ON":
            self.light.off()
            self.last_action = "LIGHT_OFF"
        elif self.last_action == "LIGHT_OFF":
            self.light.on()
            self.last_action = "LIGHT_ON"
        elif self.last_action == "AC_ON":
            self.ac.off()
            self.last_action = "AC_OFF"
        elif self.last_action == "AC_OFF":
            self.ac.on()
            self.last_action = "AC_ON"
        else:
            print("No action to undo")

remote = RemoteControl(Light(), AC())

remote.press_light_on()
remote.press_light_off()
remote.press_undo()
remote.press_ac_on()
remote.press_ac_off()
remote.press_undo()