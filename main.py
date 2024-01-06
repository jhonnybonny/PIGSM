import flet as ft
import sqlite3
import time

def get_database_connection():
    HLR_DATABASE = "/usr/src/CalypsoBTS/hlr.sqlite3"
    return sqlite3.connect(HLR_DATABASE)

def main(page: ft.Page):
    while True:
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Displaying the SQLite data
        txt_header = ft.Text("ID\t\tIMSI\t\tMSISDN\n")
        page.add(txt_header)

        def update_subscribers():
            subscriber_count = 0  # Initialize subscriber count

            with get_database_connection() as db:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM Subscriber")

                while True:
                    subscriber = cursor.fetchone()
                    if not subscriber:
                        break

                    txt_subscriber = ft.Text("{0}\t{1}\t\t{2}".format(
                        subscriber[0],
                        subscriber[1],
                        subscriber[3]
                    ))
                    page.add(txt_subscriber)

                    subscriber_count += 1  # Increment subscriber count for each row

            txt_subscriber_count = ft.Text("Subscriber Count: {0}".format(subscriber_count), size=40)
            page.add(
                txt_subscriber_count,
                ft.Text("Press CTRL+S to toggle semantics debugger"),
            )

        update_subscribers()  # Initial data load

        time.sleep(30)  # Wait for 30 seconds before the next iteration
        page.clean()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
