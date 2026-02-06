import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text(value="Olá Mundo!!!"),
        ft.ElevatedButton("Clique aqui")
    )

ft.run(main)