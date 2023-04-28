import sys
sys.path.insert(1,"Model")
import ClassNote
import Writer
import json
import datetime

def Get():
    title = input("Введите заголовок заметки: ")
    note_text = input("Введите тело заметки: ")
    data = {"title": title, "text": note_text}
    return data

def GetNote(data):
    note = ClassNote.Note(data["text"])
    return note

def read(namefile):
    with open(f"Notes/{namefile}.json","r",encoding='utf-8') as file:
        text = json.load(file)
    return text
    
def change(namefile):
    default = read(namefile)
    default["text"] = input("Введите новый текст: ")
    note = GetNote(default)
    writer = Writer.WorkOnJSON(note)
    writer.save_data_in_file(namefile)
    print("Заметка успешно изменена")

def write():
    data = Get()
    note = GetNote(data)
    writer = Writer.WorkOnJSON(note)
    writer.save_data_in_file(data["title"])
    print("Заметка успешно сохранена")

def sort(arr_txt):
    notes = []
    for i in arr_txt:
        notes.append(read(i[:-5]))
    sortedList = sorted(notes, key=lambda x: notes[0]["date"])
    for i in sortedList:
        printJSOn(i)
        print("------")

def printJSOn(json):
    for k,b in json.items():
        print(f"{k} - {b}")