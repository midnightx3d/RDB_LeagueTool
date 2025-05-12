import customtkinter as ctk
import requests

# Set the appearance mode and default color theme
ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("dark-blue")

class MainMenuPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text="Main Menu", font=("Segoe UI", 20, "bold"))
        self.label.pack(pady=20)

        # Fetch README content
        readme_url = "https://raw.githubusercontent.com/midnightx3d/RDB_LeagueTool/main/README.md"
        try:
            response = requests.get(readme_url)
            response.raise_for_status()
            readme_content = response.text
        except requests.RequestException as e:
            readme_content = f"Error fetching README: {e}"

        # Display README content
        self.readme_text = ctk.CTkTextbox(self, wrap="word")
        self.readme_text.insert("0.0", readme_content)
        self.readme_text.pack(fill="both", expand=True, padx=20, pady=20)
        self.readme_text.configure(state="disabled")  # Make the textbox read-only



class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="⚙ Settings", font=("Segoe UI", 20, "bold"))
        label.pack(pady=20)

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Racing League Manager")
        self.geometry("1600x900") 
        self.resizable(False, False) # need to be unlocked!!! I use hyprland so I use it 

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Topbar (still using pack because it spans full width)
        self.topbar = ctk.CTkFrame(self.main_frame, height=50, fg_color="#1f1f1f" , corner_radius=0)
        self.topbar.pack(fill="x", side="top")

        self.title_label = ctk.CTkLabel(self.topbar, text="RacingDashboard LeagueTool", font=("Segoe UI", 15, "bold"))
        self.title_label.pack(side="right", padx=20)

        # Content area using grid layout
        self.content = ctk.CTkFrame(self.main_frame, fg_color="#2a2a2a", corner_radius=0)
        self.content.pack(fill="both", expand=True, padx=0, pady=0)

        # Use grid inside the content frame
        self.content.grid_columnconfigure((0, 1, 2), weight=1)  # Make 3 columns expandable
        self.content.grid_rowconfigure(0, weight=1)

        #sidebar
        self.sidebar = ctk.CTkFrame(self.content, width=200, fg_color="#262626", corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        #lowbar
        self.lowbar = ctk.CTkFrame(self.sidebar, width=200, height=250 , fg_color="#363636",corner_radius=0)
        self.lowbar.pack(side="bottom")

        #menu button
        self.menu_btn = ctk.CTkButton(self.sidebar, text="Menu", fg_color="transparent" , corner_radius=0, font=("Segoe UI", 16, "bold"),command=self.show_main_menu)
        self.menu_btn.pack(pady=5,fill="x")

        # User button
        self.user_btn = ctk.CTkButton(self.sidebar, text="Drivers", fg_color="transparent" , corner_radius=0, font=("Segoe UI", 16, "bold"))
        self.user_btn.pack(pady=5,fill="x")

        #settings button
        self.settings_btn = ctk.CTkButton(self.lowbar , text="Settings ⚙", fg_color="transparent" , corner_radius= 0, font=("Segoe UI", 16, "bold"),command=self.show_settings)
        self.settings_btn.pack(pady = 5 , fill = "x")
        #database button
        self.database_btn = ctk.CTkButton(self.lowbar , text="Database", fg_color="transparent" , corner_radius= 0, font=("Segoe UI", 16, "bold"))
        self.database_btn.pack(pady = 5 ,fill="x")

        self.page_container = ctk.CTkFrame(self.content, fg_color="#161616", corner_radius=0)
        self.page_container.pack(side="right", fill="both", expand=True)

        

        # Create pages
        self.pages = {
            "menu": MainMenuPage(self.page_container),
            "settings": SettingsPage(self.page_container)
        }
        
        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)  # stack all pages

        self.show_page("menu")


    def show_page(self, name):
        for key, page in self.pages.items():
            if key == name:
                page.lift()

    def show_main_menu(self):
        self.show_page("menu")

    def show_settings(self):
        self.show_page("settings")



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()