import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import math
import os


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PixelCryptGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PixelCrypt")
        self.geometry("900x600")
        self.minsize(820, 540)

        self.generated_image = None
        self.preview_image = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=28, pady=(22, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="PixelCrypt",
            font=ctk.CTkFont(size=28, weight="bold")
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            header,
            text="RGB text encoder & decoder",
            text_color="gray"
        ).grid(row=1, column=0, sticky="w", pady=(2, 0))

        self.mode = ctk.CTkSegmentedButton(
            header,
            values=["Encode", "Decode"],
            command=self.change_mode
        )
        self.mode.set("Encode")
        self.mode.grid(row=0, column=1, rowspan=2, padx=(20, 0))

        # Main area
        self.main = ctk.CTkFrame(self, corner_radius=16)
        self.main.grid(row=1, column=0, sticky="nsew", padx=28, pady=(5, 28))
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_columnconfigure(1, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        self.build_encode_ui()
        self.build_decode_ui()

        self.decode_frame.grid_remove()

    # ---------------- ENCODE ----------------

    def build_encode_ui(self):
        self.encode_frame = ctk.CTkFrame(self.main, fg_color="transparent")
        self.encode_frame.grid(
            row=0, column=0, rowspan=2,
            sticky="nsew", padx=24, pady=24
        )
        self.encode_frame.grid_columnconfigure(0, weight=1)
        self.encode_frame.grid_columnconfigure(1, weight=1)
        self.encode_frame.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(
            self.encode_frame,
            text="Text to encode",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        self.text_input = ctk.CTkTextbox(
            self.encode_frame,
            height=130,
            corner_radius=10
        )
        self.text_input.grid(
            row=1, column=0, columnspan=2,
            sticky="ew", pady=(8, 18)
        )

        ctk.CTkLabel(
            self.encode_frame,
            text="Save location",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=2, column=0, sticky="w")

        self.location_entry = ctk.CTkEntry(
            self.encode_frame,
            placeholder_text="Choose a folder..."
        )
        self.location_entry.grid(
            row=3, column=0,
            sticky="ew", pady=(8, 0)
        )

        ctk.CTkButton(
            self.encode_frame,
            text="Browse",
            width=100,
            command=self.choose_save_location
        ).grid(row=3, column=1, sticky="w", padx=(10, 0), pady=(8, 0))

        ctk.CTkLabel(
            self.encode_frame,
            text="File name",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=4, column=0, sticky="w", pady=(18, 0))

        self.filename_entry = ctk.CTkEntry(
            self.encode_frame,
            placeholder_text="pixelcrypt.png"
        )
        self.filename_entry.grid(
            row=5, column=0,
            sticky="ew", pady=(8, 0)
        )

        self.encode_button = ctk.CTkButton(
            self.encode_frame,
            text="Encode",
            height=42,
            command=self.encode
        )
        self.encode_button.grid(
            row=6, column=0, columnspan=2,
            sticky="ew", pady=(22, 0)
        )

        # Preview
        preview = ctk.CTkFrame(
            self.main,
            corner_radius=12,
            fg_color=("gray90", "gray14")
        )
        preview.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(0, 24), pady=24)
        preview.grid_columnconfigure(0, weight=1)
        preview.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            preview,
            text="Image preview",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, pady=(18, 8))

        self.preview_label = ctk.CTkLabel(
            preview,
            text="No image generated",
            text_color="gray"
        )
        self.preview_label.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.info_label = ctk.CTkLabel(
            preview,
            text="",
            text_color="gray"
        )
        self.info_label.grid(row=2, column=0, pady=(0, 18))

    # ---------------- DECODE ----------------

    def build_decode_ui(self):
        self.decode_frame = ctk.CTkFrame(self.main, fg_color="transparent")
        self.decode_frame.grid(
            row=0, column=0, rowspan=2, columnspan=2,
            sticky="nsew", padx=24, pady=24
        )
        self.decode_frame.grid_columnconfigure(0, weight=1)
        self.decode_frame.grid_columnconfigure(1, weight=1)
        self.decode_frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(
            self.decode_frame,
            text="Image to decode",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        self.decode_path = ctk.CTkEntry(
            self.decode_frame,
            placeholder_text="Select a PNG image..."
        )
        self.decode_path.grid(
            row=1, column=0,
            sticky="ew", pady=(8, 20)
        )

        ctk.CTkButton(
            self.decode_frame,
            text="Browse",
            width=100,
            command=self.choose_decode_file
        ).grid(row=1, column=1, sticky="w", padx=(10, 0), pady=(8, 20))

        result_frame = ctk.CTkFrame(
            self.decode_frame,
            corner_radius=12,
            fg_color=("gray90", "gray14")
        )
        result_frame.grid(
            row=2, column=0, columnspan=2,
            sticky="nsew"
        )
        result_frame.grid_columnconfigure(0, weight=1)
        result_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            result_frame,
            text="Decoded text",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 8))

        self.decoded_text = ctk.CTkTextbox(
            result_frame,
            corner_radius=10
        )
        self.decoded_text.grid(
            row=1, column=0,
            sticky="nsew", padx=16, pady=(0, 16)
        )

        ctk.CTkButton(
            self.decode_frame,
            text="Decode",
            height=42,
            command=self.decode
        ).grid(
            row=3, column=0, columnspan=2,
            sticky="ew", pady=(18, 0)
        )

    # ---------------- MODE ----------------

    def change_mode(self, mode):
        if mode == "Encode":
            self.decode_frame.grid_remove()
            self.encode_frame.grid(
                row=0, column=0, rowspan=2,
                sticky="nsew", padx=24, pady=24
            )
        else:
            self.encode_frame.grid_remove()
            self.decode_frame.grid(
                row=0, column=0, rowspan=2, columnspan=2,
                sticky="nsew", padx=24, pady=24
            )

    # ---------------- FILE PICKERS ----------------

    def choose_save_location(self):
        folder = filedialog.askdirectory(title="Choose save location")
        if folder:
            self.location_entry.delete(0, "end")
            self.location_entry.insert(0, folder)

    def choose_decode_file(self):
        path = filedialog.askopenfilename(
            title="Choose image",
            filetypes=[
                ("PNG images", "*.png"),
                ("Image files", "*.png;*.jpg;*.jpeg"),
                ("All files", "*.*")
            ]
        )

        if path:
            self.decode_path.delete(0, "end")
            self.decode_path.insert(0, path)

    # ---------------- ENCODE ----------------

    def encode(self):
        text = self.text_input.get("1.0", "end-1c")
        location = self.location_entry.get().strip()
        filename = self.filename_entry.get().strip()

        if not text:
            messagebox.showwarning("Missing text", "Enter some text first.")
            return

        if not location or not os.path.isdir(location):
            messagebox.showerror("Invalid location", "Choose a valid save folder.")
            return

        if not filename:
            filename = "pixelcrypt.png"

        if not filename.lower().endswith(".png"):
            filename += ".png"

        ascii_codes = [ord(char) for char in text]

        # The original encoder stores one character in the red channel.
        # RGB channels are limited to 0-255, so reject unsupported characters.
        if any(code > 255 for code in ascii_codes):
            messagebox.showerror(
                "Unsupported character",
                "This encoder can only store characters with Unicode code points from 0 to 255."
            )
            return

        pixel_count = len(ascii_codes)
        size = math.ceil(math.sqrt(pixel_count))

        image = Image.new("RGB", (size, size), (0, 0, 0))

        index = 0
        for y in range(size):
            for x in range(size):
                if index < pixel_count:
                    image.putpixel((x, y), (ascii_codes[index], 0, 0))
                    index += 1

        file_path = os.path.join(location, filename)

        try:
            image.save(file_path)
        except Exception as error:
            messagebox.showerror("Save error", str(error))
            return

        self.show_preview(image)

        self.info_label.configure(
            text=f"{size} × {size}  •  {pixel_count} characters"
        )

        messagebox.showinfo(
            "Done",
            f"Image created successfully.\n\nSaved to:\n{file_path}"
        )

    # ---------------- DECODE ----------------

    def decode(self):
        image_path = self.decode_path.get().strip().strip('"')

        if not image_path:
            messagebox.showwarning("No image", "Choose an image to decode.")
            return

        if not os.path.isfile(image_path):
            messagebox.showerror("Invalid file", "The selected file does not exist.")
            return

        try:
            image = Image.open(image_path).convert("RGB")
        except Exception as error:
            messagebox.showerror("Image error", str(error))
            return

        text = ""

        width, height = image.size

        for y in range(height):
            for x in range(width):
                red, green, blue = image.getpixel((x, y))

                if red == 0:
                    break

                text += chr(red)
            else:
                continue

            break

        self.decoded_text.delete("1.0", "end")
        self.decoded_text.insert("1.0", text)

    # ---------------- PREVIEW ----------------

    def show_preview(self, image):
        self.generated_image = image.copy()

        max_size = 360
        preview = self.generated_image.copy()
        preview.thumbnail((max_size, max_size), Image.Resampling.NEAREST)

        self.preview_image = ImageTk.PhotoImage(preview)

        self.preview_label.configure(
            image=self.preview_image,
            text=""
        )


if __name__ == "__main__":
    app = PixelCryptGUI()
    app.mainloop()