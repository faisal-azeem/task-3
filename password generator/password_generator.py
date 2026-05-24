import random
import string
import customtkinter as ctk
import tkinter.messagebox as messagebox

# Set up appearance mode and default color theme
ctk.set_appearance_mode("System")  # Matches user's system theme (Light or Dark)
ctk.set_default_color_theme("blue")  # Modern blue theme

class PasswordGeneratorGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure the main window
        self.title("FAISAL SECURITY CORE")
        self.geometry("450x500")
        self.resizable(False, False)
        
        # App Title Header
        self.title_label = ctk.CTkLabel(
            self, 
            text="🔑 Password Generator", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(padx=20, pady=(30, 20))
        
        # Frame for password options
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Slider section for password length
        self.length_label = ctk.CTkLabel(
            self.options_frame, 
            text="Password Length: 12", 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.length_label.pack(padx=20, pady=(15, 5), anchor="w")
        
        self.length_slider = ctk.CTkSlider(
            self.options_frame, 
            from_=6, 
            to=32, 
            number_of_steps=26,  # 32 - 6 = 26 steps
            command=self.update_length_label
        )
        self.length_slider.set(12)  # Default length
        self.length_slider.pack(padx=20, pady=5, fill="x")
        
        # Checkboxes for custom character sets
        self.uppercase_var = ctk.BooleanVar(value=True)
        self.uppercase_cb = ctk.CTkCheckBox(
            self.options_frame, 
            text="Include Uppercase Letters (A-Z)", 
            variable=self.uppercase_var
        )
        self.uppercase_cb.pack(padx=20, pady=10, anchor="w")
        
        self.lowercase_var = ctk.BooleanVar(value=True)
        self.lowercase_cb = ctk.CTkCheckBox(
            self.options_frame, 
            text="Include Lowercase Letters (a-z)", 
            variable=self.lowercase_var
        )
        self.lowercase_cb.pack(padx=20, pady=10, anchor="w")
        
        self.numbers_var = ctk.BooleanVar(value=True)
        self.numbers_cb = ctk.CTkCheckBox(
            self.options_frame, 
            text="Include Numbers (0-9)", 
            variable=self.numbers_var
        )
        self.numbers_cb.pack(padx=20, pady=10, anchor="w")
        
        self.symbols_var = ctk.BooleanVar(value=False)
        self.symbols_cb = ctk.CTkCheckBox(
            self.options_frame, 
            text="Include Symbols (!@#$%^&*)", 
            variable=self.symbols_var
        )
        self.symbols_cb.pack(padx=20, pady=(10, 20), anchor="w")
        
        # Display Box for Generated Password
        self.password_entry = ctk.CTkEntry(
            self, 
            placeholder_text="Click Generate to create a password",
            font=ctk.CTkFont(size=14),
            justify="center",
            height=35
        )
        self.password_entry.pack(padx=20, pady=(15, 10), fill="x")
        
        # Buttons layout frame
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(padx=20, pady=(5, 30), fill="x")
        
        # Generate Button
        self.generate_btn = ctk.CTkButton(
            self.buttons_frame, 
            text="Generate Password", 
            command=self.generate_password,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40
        )
        self.generate_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Copy to Clipboard Button
        self.copy_btn = ctk.CTkButton(
            self.buttons_frame, 
            text="Copy to Clipboard", 
            command=self.copy_to_clipboard,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#2e7d32",  # Green color accent
            hover_color="#1b5e20",
            height=40
        )
        self.copy_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))
        
    def update_length_label(self, value):
        """Updates the length label text based on the slider value."""
        self.length_label.configure(text=f"Password Length: {int(value)}")
        
    def generate_password(self):
        """Generates a random password using the selected sets and length."""
        length = int(self.length_slider.get())
        
        # Assemble custom character pool based on checkbox selections
        char_pool = ""
        if self.uppercase_var.get():
            char_pool += string.ascii_uppercase
        if self.lowercase_var.get():
            char_pool += string.ascii_lowercase
        if self.numbers_var.get():
            char_pool += string.digits
        if self.symbols_var.get():
            # Standard safe special characters
            char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
        # Ensure at least one character set is selected
        if not char_pool:
            messagebox.showerror(
                "Selection Error", 
                "Please select at least one character type to generate a password."
            )
            return
            
        # Generate the password
        password = ''.join(random.choice(char_pool) for _ in range(length))
        
        # Clear previous content and set the new password
        self.password_entry.delete(0, ctk.END)
        self.password_entry.insert(0, password)
        
    def copy_to_clipboard(self):
        """Copies the generated password to the system clipboard."""
        password = self.password_entry.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            self.update()  # Update system clipboard manager
            messagebox.showinfo("Success", "Password copied to clipboard successfully!")
        else:
            messagebox.showwarning("Warning", "No password generated yet. Generate one first!")

if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.mainloop()
