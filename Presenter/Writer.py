import sys
sys.path.insert(1,"Model")
import ClassNote
import json

class WriterOnJSON:
    global data
    data = {}
    def __init__(self, data: ClassNote.Note):
        self.data = {'date': data.date, 'text': data.text, 'id': id(data)}
        pass
    
    def save_data_in_file(self,name):
        with open(f'Notes/{name}.json','w') as file:
            json.dump(self.data,file)