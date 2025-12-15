import tkinter as tk
from tkinter import simpledialog, messagebox
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def create_media():
    title = simpledialog.askstring("Create Media", "Enter media title:")
    if not title:
        return

    media_type = simpledialog.askstring("Create Media", "Enter media type:")
    if not media_type:
        return

    try:
        response = requests.post(BASE_URL + "/", json={"title": title, "type": media_type})
        if response.status_code == 201:
            messagebox.showinfo("Success", f"Media created with ID: {response.json()['id']}")
        else:
            messagebox.showerror("Error", response.json().get("error", "Unknown error"))
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to Flask: {e}")

def list_medias():
    try:
        response = requests.get(BASE_URL + "/")
        if response.status_code == 200:
            medias = response.json()
            if not medias:
                messagebox.showinfo("Media List", "No media found in the database.")
                return

            msg = "\n".join([f"ID: {m['id']}, Title: {m['title']}, Type: {m['type']}" for m in medias])
            messagebox.showinfo("Media List", msg)
        else:
            messagebox.showerror("Error", "Failed to fetch media")
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to Flask: {e}")

def run_tkinter():
    root = tk.Tk()
    root.title("Media Manager")

    tk.Label(root, text="Media Manager GUI").pack(pady=10)

    tk.Button(root, text="Create Media", command=create_media, width=20).pack(pady=5)
    tk.Button(root, text="List All Medias", command=list_medias, width=20).pack(pady=5)

    root.mainloop()
