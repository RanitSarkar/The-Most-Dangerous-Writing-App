import tkinter as tk


class WritingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("The Most Dangerous Writing App")

        self.text = tk.Text(self.master, height=20, width=50)
        self.text.pack()

        self.timer_interval = 10000  # Time interval in milliseconds (e.g., 1000 = 1 second)
        self.timer = None

        self.start_timer()
        self.master.bind("<Key>", self.reset_timer)


    def start_timer(self):
        self.timer = self.master.after(self.timer_interval, self.delete_text)

    def reset_timer(self, event):
        if self.timer:
            self.master.after_cancel(self.timer)
        self.start_timer()


    def delete_text(self):
        if self.text.get("1.0", "end-1c"):
            self.text.delete("1.0", "end-1c")
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    app = WritingApp(root)
    root.mainloop()
