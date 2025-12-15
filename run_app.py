import threading
import tkinter as tk
from backend.app import app

def run_flask():
    app.run(debug=True, use_reloader=False)

def run_tkinter():
    root = tk.Tk()
    root.title("Media Manager")
    tk.Label(root, text="Interface Tkinter da Media Manager").pack(padx=20, pady=20)

    import requests
    def get_media():
        try:
            response = requests.get("http://127.0.0.1:5000/media")
            print(response.json())
        except Exception as e:
            print("Erro ao acessar Flask:", e)

    tk.Button(root, text="Get Media", command=get_media).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    run_tkinter()
