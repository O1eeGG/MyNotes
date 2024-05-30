import sys
from database import init_db, add_note, get_notes, update_note, delete_note

def display_menu():
    print("\nУправление заметками")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

def main():
    init_db()
    while True:
        display_menu()
        choice = input("Выберите опцию: ")
        if choice == '1':
            content = input("Введите текст заметки: ")
            add_note(content)
            print("Заметка добавлена!")
        elif choice == '2':
            notes = get_notes()
            print("\nСписок заметок:")
            for note in notes:
                print(f"{note[0]}. {note[1]} (создана: {note[2]})")
        elif choice == '3':
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_content = input("Введите новый текст заметки: ")
            update_note(note_id, new_content)
            print("Заметка обновлена!")
        elif choice == '4':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
            print("Заметка удалена!")
        elif choice == '5':
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == '__main__':
    main()
