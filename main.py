import tkinter as tk


class WritingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("The Most Dangerous Writing App")

        self.text = tk.Text(self.master, height=20, width=50)
        self.text.pack()

        self.timer_interval2 = 8000
        self.timer_interval1=5000
        self.timer_interval = 10000  # Time interval in milliseconds (e.g., 1000 = 1 second)
        self.timer = None
        self.new_color8 = 'red'
        self.new_color5 = 'green'

        self.warn1()
        self.warn2()
        self.start_timer()
        self.master.bind("<Key>", self.reset_timer)

    def warn1(self):
        self.text.after(self.timer_interval2, self.change_text_color2)
    def warn2(self):
        self.text.after(self.timer_interval1, self.change_text_color1)

    def change_text_color2(self):
        self.text.config(fg=self.new_color8)  # Change the text color

    def change_text_color1(self):
        self.text.config(fg=self.new_color5)  # Change the text color

    def start_timer(self):
        self.timer = self.master.after(self.timer_interval, self.delete_text)

    def reset_timer(self, event):
        if self.timer:
            self.master.after_cancel(self.timer)
        self.start_timer()
        self.warn1()
        self.warn2()


    def delete_text(self):
        if self.text.get("1.0", "end-1c"):
            self.text.delete("1.0", "end-1c")
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    app = WritingApp(root)
    root.mainloop()
