import readchar
from threading import Thread, Lock

MatrixUserInput.start_thread()

class MatrixUserInput(object):
    '''
    True -- waiting for the next pressed key; thread is running
    False -- not waiting for any input; no thread
    '''
    input_running = True

    '''

    '''
    input_dict = {}
    
    def start_thread(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.input_running:
            pressed = readchar.readkey()
            for key, function in input_dict.items():
                if pressed == key:
                    function()
            

    def attach_key(self, key, function):
        self.input_dict[key] = function
    
    def attach_keys(self, key_list, function):
        for key in key_list:
            self.attach_key(key, function)

    def exit(self):
        input_running = False
