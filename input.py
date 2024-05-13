import readchar
from threading import Thread, Lock


class MatrixUserInput(object):
    input_running = True
    input_dict = {}
    
    def __init__(self):
        self.start_thread()

    def start_thread(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.input_running:
            pressed = readchar.readkey()
            for key, function in self.input_dict.items():
                if pressed == key:
                    function()
            

    def attach_key(self, key, function):
        self.input_dict[key] = function
    
    def attach_keys(self, key_list, function):
        for key in key_list:
            self.attach_key(key, function)
    def test_print(self):
        print("printing!!!")

    def exit(self):
        self.input_running = False
