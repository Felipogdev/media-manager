import threading
from backend import create_app
from gui.tkinter_app import run_tkinter

app = create_app()

def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    run_tkinter()
