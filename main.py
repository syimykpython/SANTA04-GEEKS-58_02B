import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    
    greeting_history = []
    history_text = ft.Text(value='История приветствий:')

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            now = datetime.now().strftime("%H:%M:%S")
            greeting_text.value = f"Hello {name}!"
            name_input.value = ""

            greeting_history.append(f"{now} - {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Ошибка! Вы не ввели имя" 
        
        print(greeting_text.value)
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    greet_button = ft.ElevatedButton("send", on_click=on_button_click)

    page.add(greeting_text, name_input, greet_button, history_text)


ft.app(target=main)