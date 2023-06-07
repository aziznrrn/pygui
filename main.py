from tkinter import Tk, ttk, messagebox, END
import sv_ttk

root = Tk()

sv_ttk.set_theme("light")

class User:
    instances = []
    highest_id = 0
    current_user = None

    def __init__(self, username, password, name, email, major, byear):
        self.id = self.highest_id + 1
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.major = major
        self.byear = byear
        User.instances.append(self)
        User.highest_id += 1

class Teacher:
    instances = []
    highest_id = 0

    def __init__(self, name, subject, popularity, rating):
        self.id = self.highest_id + 1
        self.name = name
        self.subject = subject
        self.popularity = popularity
        self.rating = rating
        Teacher.instances.append(self)
        Teacher.highest_id += 1

User("admin", "admin", "Administrator", "admin@evil.org", "Computer Science", "2021")
Teacher("Russel",    "Math",       5, 5.0)
Teacher("Lacan",     "Philosophy", 4, 4.0)
Teacher("Heidegger", "Philosophy", 2, 3.0)
Teacher("Marx",      "Economics",  1, 5.0)
Teacher("Lock",      "Politics",   3, 4.5)
Teacher("smith",     "Economics",  5, 3.5)
Teacher("White",     "Chemistry",  5, 5.0)
Teacher("Pinkman",   "Chemistry",  4, 3.5)
Teacher("Goodman",   "Law",        3, 4.0)
Teacher("Gustavo",   "Business",   2, 3.0)

def setupWindow(title):
    for child in root.winfo_children():
        child.destroy()

    root.title(title)

    f = ttk.Frame(root)
    f.pack(padx=30, pady=30)

    return f

def login(username_e, password_e):
    username = username_e.get()
    password = password_e.get()

    password_e.delete(0, END)

    if username == "" or password == "":
        messagebox.showerror("Error", "Username or password cannot be empty!")
    else:
        exist = False
        for user in User.instances:
            if user.username == username and user.password == password:
                exist = True
                User.current_user = user
                messagebox.showinfo("Success", "Login success!")
                mainMenu()
        if not exist:
            messagebox.showerror("Error", "Username or password is incorrect!")


def register(username_e, password_e, name_e, email_e, major_e, byear_e):
    username = username_e.get()
    password = password_e.get()
    name = name_e.get()
    email = email_e.get()
    major = major_e.get()
    byear = byear_e.get()

    password_e.delete(0, END)

    if username == "" or password == "":
        messagebox.showerror("Error", "Username or password cannot be empty!")
    elif len(username) < 3 or len(username) > 20:
        messagebox.showerror("Error", "Username length must be between 3 and 20!")
    elif len(password) < 8 or len(password) > 20:
        messagebox.showerror("Error", "Password length must be between 8 and 20!")
    elif not username.isalnum():
        messagebox.showerror("Error", "Username must be alphanumeric!")
    else:
        exist = False
        for user in User.instances:
            if user.username == username:
                exist = True
                messagebox.showerror("Error", "Username already exists!")
        if not exist:
            User(username, password, name, email, major, byear)
            messagebox.showinfo("Success", "Register success!")
            loginMenu()

def logout():
    User.current_user = None
    loginMenu()

def loginMenu():
    window = setupWindow("Login Menu")

    input_f = ttk.Frame(window)
    input_f.pack(pady=(0, 10))

    username_l = ttk.Label(input_f, text="Username")
    username_l.grid(row=0, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    username_e = ttk.Entry(input_f, width=36, font=("courier new", 10))
    username_e.grid(row=0, column=1, sticky="w", pady=(0, 10), ipady=2)

    password_l = ttk.Label(input_f, text="Password")
    password_l.grid(row=1, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    password_e = ttk.Entry(input_f, show="*", width=36, font=("courier new", 10))
    password_e.grid(row=1, column=1, sticky="w", pady=(0, 10), ipady=2)

    button_f = ttk.Frame(window)
    button_f.pack()

    login_b = ttk.Button(button_f, text="Login", command=lambda: login(username_e, password_e))
    login_b.grid(row=0, column=0, columnspan=2, padx=(0, 16))

    register_l = ttk.Label(button_f, text="Don't have an account?")
    register_l.grid(row=1, column=0, padx=(0, 10))
    register_b = ttk.Button(button_f, text="Register", command=lambda: registerMenu())
    register_b.grid(row=1, column=1)

    root.mainloop()

def registerMenu():
    window = setupWindow("Register Menu")

    input_f = ttk.Frame(window)
    input_f.pack(pady=(0, 10))

    username_l = ttk.Label(input_f, text="Username")
    username_l.grid(row=0, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    username_e = ttk.Entry(input_f, width=42)
    username_e.grid(row=0, column=1, sticky="w", pady=(0, 10), ipady=4)

    password_l = ttk.Label(input_f, text="Password")
    password_l.grid(row=1, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    password_e = ttk.Entry(input_f, show="*", width=42)
    password_e.grid(row=1, column=1, sticky="w", pady=(0, 10), ipady=4)

    name_l = ttk.Label(input_f, text="Name")
    name_l.grid(row=2, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    name_e = ttk.Entry(input_f, width=42)
    name_e.grid(row=2, column=1, sticky="w", pady=(0, 10), ipady=4)

    email_l = ttk.Label(input_f, text="Email")
    email_l.grid(row=3, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    email_e = ttk.Entry(input_f, width=42)
    email_e.grid(row=3, column=1, sticky="w", pady=(0, 10), ipady=4)

    major_l = ttk.Label(input_f, text="Major")
    major_l.grid(row=4, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    major_e = ttk.Entry(input_f, width=42)
    major_e.grid(row=4, column=1, sticky="w", pady=(0, 10), ipady=4)

    byear_l = ttk.Label(input_f, text="Birth Year")
    byear_l.grid(row=5, column=0, sticky="w", pady=(0, 10), padx=(0, 10))
    byear_e = ttk.Entry(input_f, width=42)
    byear_e.grid(row=5, column=1, sticky="w", pady=(0, 10), ipady=4)

    button_f = ttk.Frame(window)
    button_f.pack(side="right")

    register_b = ttk.Button(button_f, text="Register", command=lambda: register(username_e, password_e, name_e, email_e, major_e, byear_e))
    register_b.grid(row=0, column=0, padx=(0, 10))

    cancel_b = ttk.Button(button_f, text="Cancel", command=lambda: loginMenu())
    cancel_b.grid(row=0, column=1,)

    root.mainloop()

def teachersSection(container, search):
    search = search.strip().lower()
    filter = None
    sort = None

    for child in container.winfo_children():
        child.destroy()

    teachers_l = ttk.Label(container, text="List of Teachers")
    teachers_l.configure(font=("Sans", 12, "bold"))
    teachers_l.pack(pady=(0, 10))

    function_buttons = ttk.Frame(container)
    function_buttons.pack(pady=(0, 20))

    teachers_f = ttk.Frame(container)
    teachers_f.pack(pady=(0, 20))

    # on click set filter & sort to none
    ttk.Button(function_buttons, text="All", command=lambda: teacherListSection(teachers_f, search)).pack(side="left", padx=(0, 10))
    ttk.Button(function_buttons, text="Popularity>=4", command=lambda: teacherListSection(teachers_f, search, "popular")).pack(side="left", padx=(0, 10))
    ttk.Button(function_buttons, text="Rating>=4", command=lambda: teacherListSection(teachers_f, search, "rating")).pack(side="left", padx=(0, 10))
    ttk.Button(function_buttons, text="Sort by Popularity", command=lambda: teacherListSection(teachers_f, search, sort="popular")).pack(side="left", padx=(0, 10))
    ttk.Button(function_buttons, text="Sort by Rating", command=lambda: teacherListSection(teachers_f, search, sort="rating")).pack(side="left", padx=(0, 10))

    teacherListSection(teachers_f, search, filter, sort)


def teacherListSection(container, search, filter = None, sort = None):
    for child in container.winfo_children():
        child.destroy()

    ttk.Label(container, text="Name", font=("Sans", 10, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10), padx=(0, 50))
    ttk.Label(container, text="Subject", font=("Sans", 10, "bold")).grid(row=0, column=1, sticky="w", pady=(0, 10), padx=(0, 50))
    ttk.Label(container, text="Popularity", font=("Sans", 10, "bold")).grid(row=0, column=2, sticky="w", pady=(0, 10), padx=(0, 50))
    ttk.Label(container, text="Rating", font=("Sans", 10, "bold")).grid(row=0, column=3, sticky="w", pady=(0, 10))

    teachers = Teacher.instances
    if filter == "popular":
        teachers = sorted(teachers, key=lambda teacher: teacher.popularity, reverse=True)
        teachers = [teacher for teacher in teachers if teacher.popularity >= 4]
    elif filter == "rating":
        teachers = sorted(teachers, key=lambda teacher: teacher.rating, reverse=True)
        teachers = [teacher for teacher in teachers if teacher.rating >= 4]
    elif sort == "popular":
        teachers = sorted(teachers, key=lambda teacher: teacher.popularity, reverse=True)
    elif sort == "rating":
        teachers = sorted(teachers, key=lambda teacher: teacher.rating, reverse=True)

    for id in range(len(teachers)):
        has_padding = id != len(teachers) - 1
        if teachers[id].name.lower().find(search) != -1 if search != "" else True:
            ttk.Label(container, text=teachers[id].name).grid(row=id+1, column=0, sticky="w", pady=(0, 10) if has_padding else 0, padx=(0, 50))
            ttk.Label(container, text=teachers[id].subject).grid(row=id+1, column=1, sticky="w", pady=(0, 10) if has_padding else 0, padx=(0, 50))
            ttk.Label(container, text=teachers[id].popularity).grid(row=id+1, column=2, sticky="w", pady=(0, 10) if has_padding else 0, padx=(0, 50))
            ttk.Label(container, text=teachers[id].rating).grid(row=id+1, column=3, sticky="w", pady=(0, 10) if has_padding else 0)

    if len(container.winfo_children()) <= 4:
        for child in container.winfo_children():
            child.destroy()

        ttk.Label(container, text="No teachers found").grid(row=0, column=0, sticky="w", columnspan=4)

def sessionsSection(container):
    session_f = ttk.Frame(container)
    session_f.pack()

    session_l = ttk.Label(session_f, text="Logged in as " + User.current_user.username)
    session_l.pack(side="left", padx=(0, 260))

    profile_b = ttk.Button(session_f, text="Profile", command=lambda: profileWindow())
    profile_b.pack(side="left", padx=(0, 10))

    logout_b = ttk.Button(session_f, text="Logout", command=lambda: logout())
    logout_b.pack(side="left")

    ttk.Separator(container, orient="horizontal").pack(fill="x", pady=(10, 60))

def profileWindow():
    window = setupWindow("Profile")

    sessionsSection(window)

    profile_f = ttk.Frame(window)
    profile_f.pack()

    profile_l = ttk.Label(profile_f, text="Profile", font=("Sans", 32, "bold"))
    profile_l.pack(pady=(0, 20))

    profile_name_l = ttk.Label(profile_f, text="Name: " + User.current_user.name)
    profile_name_l.pack(pady=(0, 10))

    profile_username_l = ttk.Label(profile_f, text="Username: " + User.current_user.username)
    profile_username_l.pack(pady=(0, 10))

    profile_email_l = ttk.Label(profile_f, text="Email: " + User.current_user.email)
    profile_email_l.pack(pady=(0, 10))

    profile_major_l = ttk.Label(profile_f, text="Major: " + User.current_user.major)
    profile_major_l.pack(pady=(0, 10))

    profile_byear_l = ttk.Label(profile_f, text="Birth Year: " + User.current_user.byear)
    profile_byear_l.pack(pady=(0, 10))

    back_to_main_b = ttk.Button(profile_f, text="Back to Main Menu", command=lambda: mainMenu())
    back_to_main_b.pack(pady=(20, 0))


def mainMenu():
    window = setupWindow('Main Menu')

    sessionsSection(window)

    search_f = ttk.Frame(window)
    search_f.pack(pady=(0, 40))

    search_l = ttk.Label(search_f, text="Search for teachers", font=("Sans", 32, "bold"))
    search_l.pack(pady=(0, 10))

    search_e = ttk.Entry(search_f, width=40, font=("courier new", 12))
    search_e.pack(side="left", ipady=2)
    search_b = ttk.Button(search_f, text="Search", command=lambda: teachersSection(teachers_f, search_e.get()))
    search_b.pack(side="left", padx=(10, 0), ipady=2)

    teachers_f = ttk.Frame(window)
    teachers_f.pack()
    teachersSection(teachers_f, "")

    root.mainloop()

if __name__ == "__main__":
    loginMenu()
