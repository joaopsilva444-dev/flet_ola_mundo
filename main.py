import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro app Flet"
    page.bgcolor = "#47c3fc"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Mambo"),
        ft.ElevatedButton("Clique Aqui")
    )

ft.run(main)


