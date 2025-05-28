import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import math

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Processamento de Imagens - Autor: Willian dos Santos Ribas")
        self.root.geometry("900x600")

        # Menu
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Menu Arquivo
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir Imagem", command=self.open_image)
        file_menu.add_command(label="Salvar Imagem", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Sobre", command=self.show_about)
        file_menu.add_command(label="Sair", command=root.quit)
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Menu Transformações Geométricas
        transform_menu = tk.Menu(self.menu_bar, tearoff=0)
        transform_menu.add_command(label="Rotacionar", command=self.apply_rotation)
        transform_menu.add_command(label="Transladar", command=self.apply_translation)
        transform_menu.add_command(label="Espelhar", command=self.apply_mirror)
        transform_menu.add_command(label="Aumentar", command=self.apply_scale_up)
        transform_menu.add_command(label="Diminuir", command=self.apply_scale_down)
        self.menu_bar.add_cascade(label="Transformações Geométricas", menu=transform_menu)

        # Menu Filtros
        filter_menu = tk.Menu(self.menu_bar, tearoff=0)
        filter_menu.add_command(label="Grayscale", command=self.apply_grayscale)
        filter_menu.add_command(label="Passa Baixa", command=self.apply_low_pass)
        filter_menu.add_command(label="Passa Alta", command=self.apply_high_pass)
        filter_menu.add_command(label="Threshold", command=self.apply_threshold)
        self.menu_bar.add_cascade(label="Filtros", menu=filter_menu)

        # Frames para imagens
        self.left_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.right_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.original_label = tk.Label(self.left_frame, text="Imagem Sem Efeito")
        self.original_label.pack()

        self.processed_label = tk.Label(self.right_frame, text="Imagem Com Efeito")
        self.processed_label.pack()

        self.original_image = None
        self.processed_image = None

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            self.original_image = Image.open(file_path).convert("RGB")
            self.processed_image = self.original_image.copy()
            self.display_image(self.original_image, self.original_label, self.left_frame)

    def save_image(self):
        if self.processed_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")])
            if file_path:
                self.processed_image.save(file_path)
                messagebox.showinfo("Salvar Imagem", "Imagem salva com sucesso!")
        else:
            messagebox.showwarning("Salvar Imagem", "Nenhuma imagem processada para salvar.")

    def show_about(self):
        messagebox.showinfo("Sobre", "Projeto de Processamento de Imagens\nAutor: Willian dos Santos Ribas")

        # Rotacionar
    def apply_rotation(self):
        if self.original_image:
            angle = simpledialog.askfloat("Rotacionar", "Digite o ângulo de rotação:", minvalue=-360, maxvalue=360)
            if angle is None:
                return

            angle_rad = math.radians(-angle)
            cos_theta = math.cos(angle_rad)
            sin_theta = math.sin(angle_rad)

            width, height = self.original_image.size
            center_x, center_y = width // 2, height // 2

            new_width = int(abs(width * cos_theta) + abs(height * sin_theta))
            new_height = int(abs(width * sin_theta) + abs(height * cos_theta))
            new_image = Image.new("RGB", (new_width, new_height), (0, 0, 0))

            original_pixels = self.original_image.load()
            new_pixels = new_image.load()

            for x in range(new_width):
                for y in range(new_height):
                    original_x = int((x - new_width // 2) * cos_theta + (y - new_height // 2) * sin_theta + center_x)
                    original_y = int(-(x - new_width // 2) * sin_theta + (y - new_height // 2) * cos_theta + center_y)
                    if 0 <= original_x < width and 0 <= original_y < height:
                        new_pixels[x, y] = original_pixels[original_x, original_y]

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Translação
    def apply_translation(self):
        if self.original_image:
            dx = simpledialog.askinteger("Translação", "Digite o deslocamento horizontal:")
            dy = simpledialog.askinteger("Translação", "Digite o deslocamento vertical:")
            width, height = self.original_image.size
            new_image = Image.new("RGB", (width, height), (0, 0, 0))
            pixels = self.original_image.load()
            new_pixels = new_image.load()

            for x in range(width):
                for y in range(height):
                    if 0 <= x - dx < width and 0 <= y - dy < height:
                        new_pixels[x, y] = pixels[x - dx, y - dy]

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Espelhar
    def apply_mirror(self):
        if self.original_image:
            width, height = self.original_image.size
            new_image = Image.new("RGB", (width, height))
            pixels = self.original_image.load()
            new_pixels = new_image.load()

            for x in range(width):
                for y in range(height):
                    new_pixels[x, y] = pixels[width - 1 - x, y]

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Aumentar o tamanho
    def apply_scale_up(self):
        if self.original_image:
            factor = simpledialog.askfloat("Aumentar", "Digite o fator de escala:", minvalue=1.1)
            if factor:
                self.processed_image = self.original_image.resize((int(self.original_image.width * factor), int(self.original_image.height * factor)))
                self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Diminuir o tamanho
    def apply_scale_down(self):
        if self.original_image:
            factor = simpledialog.askfloat("Diminuir", "Digite o fator de escala:", minvalue=0.1, maxvalue=0.9)
            if factor:
                self.processed_image = self.original_image.resize((int(self.original_image.width * factor), int(self.original_image.height * factor)))
                self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Grayscale
    def apply_grayscale(self):
        if self.original_image:
            width, height = self.original_image.size
            new_image = Image.new("RGB", (width, height))
            pixels = self.original_image.load()
            new_pixels = new_image.load()

            for x in range(width):
                for y in range(height):
                    r, g, b = pixels[x, y]
                    gray = int((r + g + b) / 3)
                    new_pixels[x, y] = (gray, gray, gray)

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Passa Baixa
    def apply_low_pass(self):
        if self.original_image:
            width, height = self.original_image.size
            pixels = self.original_image.load()
            new_image = Image.new("RGB", (width, height))
            new_pixels = new_image.load()

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    r_sum = g_sum = b_sum = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            r, g, b = pixels[x + dx, y + dy]
                            r_sum += r
                            g_sum += g
                            b_sum += b
                    new_pixels[x, y] = (
                        r_sum // 9,
                        g_sum // 9,
                        b_sum // 9
                    )

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)

        # Passa Alta
    def apply_high_pass(self):
        if self.original_image:
            width, height = self.original_image.size
            pixels = self.original_image.load()
            new_image = Image.new("RGB", (width, height))
            new_pixels = new_image.load()

            kernel = [[-1, -1, -1],
                      [-1,  8, -1],
                      [-1, -1, -1]]

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    r_sum = g_sum = b_sum = 0
                    for i in range(3):
                        for j in range(3):
                            dx = i - 1
                            dy = j - 1
                            r, g, b = pixels[x + dx, y + dy]
                            weight = kernel[i][j]
                            r_sum += r * weight
                            g_sum += g * weight
                            b_sum += b * weight

                    r = min(max(r_sum, 0), 255)
                    g = min(max(g_sum, 0), 255)
                    b = min(max(b_sum, 0), 255)
                    new_pixels[x, y] = (r, g, b)

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)


        # Threshold
    def apply_threshold(self):
        if self.original_image:
            limiar = simpledialog.askinteger("Threshold", "Digite o valor do limiar (0 a 255):", minvalue=0, maxvalue=255)
            if limiar is None:
                return

            width, height = self.original_image.size
            new_image = Image.new("RGB", (width, height))
            pixels = self.original_image.load()
            new_pixels = new_image.load()

            for x in range(width):
                for y in range(height):
                    r, g, b = pixels[x, y]
                    gray = (r + g + b) // 3
                    value = 255 if gray >= limiar else 0
                    new_pixels[x, y] = (value, value, value)

            self.processed_image = new_image
            self.display_image(self.processed_image, self.processed_label, self.right_frame)

    def display_image(self, image, label, frame):
        max_size = 300
        img_width, img_height = image.size
        scale = min(max_size / img_width, max_size / img_height, 1.0)
        new_size = (int(img_width * scale), int(img_height * scale))
        display_img = image.resize(new_size, Image.LANCZOS)

        image_tk = ImageTk.PhotoImage(display_img)
        label.config(image=image_tk)
        label.image = image_tk
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()