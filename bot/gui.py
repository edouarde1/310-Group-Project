import sys
import tkinter as tk
import botbot


# Class for the Bot GUI
class BotGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomeScreen)
        self.title("Atlantis Explorer")

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
# TODO: Potentially increase starting size of this window so it's less awkward
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
    # The function which handles user input.
    def retrieve_user_message(self, inputField):
        # Retrieve user input and save it
        userInput = inputField.get("1.0", tk.END)
        # Clear input box
        inputField.delete("1.0", tk.END)
        # Remove unnecessary punctuation
        punctuation = '!()-[]{};:\,<>./?@#$%^&*_~'
        for char in punctuation:
            userInput = userInput.replace(char,' ')
        # Pass input through spell checking module
        input = botbot.spell_check(userInput)
        print(input)
        # Get response from bot & update response label
        self.response = botbot.get_response(input)
        print("Response", self.response)
        self.responseLabel["text"] = self.response

    def show_help_popup(self):
        self.responseLabel["text"] = "Welcome, Adventurer! Please enter your question below.\n When you are done, " \
                                     "please end your question with a '?' and hit the 'Send' button below!"

    def __init__(self, master):
        self.response = "Welcome, Adventurer! Please enter your question below.\n When you are done, please end your " \
                        "question with a '?' and hit the 'Send' button below!"
        tk.Frame.__init__(self, master)
        # Response label is what the bot response will be output to
        self.responseLabel = tk.Label(self, text=self.response)
        self.responseLabel.pack(side="top", fill="x", pady=10)
        userInputField = tk.Text(self)
        userInputField.pack(side="top", fill="x", pady=10)
        # Bottom row of buttons
        tk.Button(self, text="Send",
                  command=lambda: self.retrieve_user_message(userInputField)).pack(side="left")
        tk.Button(self, text="Help",
                  command=lambda: self.show_help_popup()).pack(side="left")
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(HomeScreen)).pack(side="left")


botInterface = BotGUI()
botInterface.mainloop()
