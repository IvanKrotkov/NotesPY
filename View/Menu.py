import os
import GetData
import glob
import sys
sys.path.insert(1, "Presenter")


def GetMenu():
    command = input("Выберите команду: \
                    \nadd - добавить новую заметку\
                    \nshow - показать список заметок\
                    \nesc - закрыть программу\n")
    if command == "add":
        GetData.write()
        GetMenu()
    elif command == "show":
        nextMenu()
    else:
        exit()


def nextMenu():
    arr_txt = [x for x in os.listdir("Notes") if x.endswith(".json")]
    print(arr_txt)
    command = input("Введите дальнейшее действие: \
                    \nremove - удалить заметку\
                    \nchange - изменить заметку\
                    \nshow - показать заметку \
                    \nsort - выборка по дате\n")
    if command == "remove":
        title = input("Введите заголовок заметки, которую хотите удалить: ")
        os.remove(f"Notes/{title}.json")
        print("Заметка успешно удалена")
        GetMenu()
    elif command == "change":
        title = input("Введите заголовок заметки, которую хотите изменить: ")
        GetData.change(title)
        GetMenu()
    elif command == "show":
        title = input("Введите заголовок заметки, которую хотите посмотреть: ")
        print(GetData.read(title))
        GetMenu()
    elif command == "sort":
        GetData.sort(arr_txt)
        GetMenu()
        
