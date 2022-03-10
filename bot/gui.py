import sys
import tkinter as tk


# Class for the Bot GUI
class BotGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomeScreen)

    # Destroy active window and replace with desired
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            # Delete old frame if it exists
            self._frame.destroy()
        # Set active frame as the new frame & pack it
        self._frame = new_frame
        self._frame.pack()

    # Shut down application
    def quit(self):
        self.destroy()


# Main title screen shown when loading app
class HomeScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome, Adventurer!").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Start Conversation",
                  command=lambda: master.switch_frame(ChatScreen)).pack()
        tk.Button(self, text="Exit ",
                  command=lambda: master.quit()).pack()


# The screen where inputs are entered
class ChatScreen(tk.Frame):
    def send_message(self, message):
        return message

    def __init__(self, master):
        self.response = "Welcome, Adventurer! Please enter your questions below."
        tk.Frame.__init__(self, master)
        tk.Label(self, text=self.response).pack(side="top", fill="x", pady=10)
        userInput = tk.Text(self)
        userInput.pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Send",
                  command=lambda: master.switch_frame(ChatScreen)).pack()
        tk.Button(self, text="Back ",
                  command=lambda: master.switch_frame(HomeScreen)).pack()


bot = BotGUI()
bot.mainloop()
