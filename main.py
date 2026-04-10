import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro app flet"
    page.bgcolor = "#38beb9"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Olá Mundo!!!"),
        ft.ElevatedButton("Clique aqui")
    )

ft.run(main)