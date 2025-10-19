import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("hello world")
    greeting_history = []
    history_text = ft.Text("История приветствий:")

    def get_time_based_greeting(name):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            greeting = "Доброе утро"
        elif 12 <= hour < 18:
            greeting = "Добрый день"
        elif 18 <= hour < 24:
            greeting = "Добрый вечер"
        else:
            greeting = "Доброй ночи"
        return greeting

    def on_button_click(_):
        name = name_input.value.strip()
        age = age_input.value.strip()

        if not name:
            greeting_text.value = "Пожалуйста, введите имя!"
        elif not age:
            greeting_text.value = "Введите возраст!"
        else:
            greeting = get_time_based_greeting(name)
            greeting_text.value = f"{greeting}, {name} тебе {age} лет."
            name_input.value = ""
            age_input.value = ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp} — {greeting_text.value}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

        page.update()

    name_input = ft.TextField(label="Введите имя:", on_submit=on_button_click)
    age_input = ft.TextField(label="Введите возраст:", on_submit=on_button_click, keyboard_type=ft.KeyboardType.NUMBER)
    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)

    page.add(greeting_text, name_input, age_input, name_button, history_text)

ft.app(target=main)
