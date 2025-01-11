import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as ai

# Configure API key
ai.configure(api_key="API_KEY")

# Initialize the Generative Model
model = ai.GenerativeModel()

# Function to get a response from the AI
def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

# Function to handle the sending of messages
def send_message():
    user_message = user_input.get()
    if user_message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {user_message}\n", 'user')
        chat_window.config(state=tk.DISABLED)
        user_input.delete(0, tk.END)
        
        # Get AI response
        ai_response = get_ai_response(user_message)
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"AI: {ai_response}\n", 'ai')
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)

# Set up the main window
root = tk.Tk()
root.title("TkiTalkie")
root.geometry("500x600")
root.configure(bg="#f5f5f5")

# Create and pack widgets
chat_window = scrolledtext.ScrolledText(
    root, state=tk.DISABLED, wrap=tk.WORD, height=20, width=60, bg="#ffffff", fg="#000000", font=("Helvetica", 12)
)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(padx=10, pady=10, fill=tk.X)

user_input = tk.Entry(frame, width=50, font=("Helvetica", 12), bg="#e0e0e0", fg="#000000")
user_input.pack(side=tk.LEFT, padx=(0, 10), pady=10, fill=tk.X, expand=True)

send_button = tk.Button(frame, text="Send", command=send_message, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
send_button.pack(side=tk.RIGHT, padx=(10, 0), pady=10)

# Configure tags for text styles
chat_window.tag_configure('user', foreground='#606060', font=("Helvetica", 12, "bold"))  # User messages in gray
chat_window.tag_configure('ai', foreground='#000000', font=("Helvetica", 12))  # AI messages in black

# Run the application
root.mainloop()
