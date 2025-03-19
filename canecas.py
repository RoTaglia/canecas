import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from fpdf import FPDF
import sys
import os
import fitz  # PyMuPDF
import tempfile
import webbrowser  # Para abrir o PDF no navegador

# Função para acessar arquivos embutidos
def resource_path(relative_path):
    try:
        # Quando o aplicativo for empacotado com PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Durante o desenvolvimento
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Classe PDF
class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='L', unit='cm', format='A4')

    def add_image(self, image_path, position):
        page_width = 29.7
        cm_height = 9.3
        spacing = 1
        margin = 0.5

        img = Image.open(image_path)
        width, height = img.size
        scale = (cm_height * 37.8) / height
        img_width = width * scale / 37.8

        x_offset = (page_width - img_width) / 2
        y_offset = margin + position * (cm_height + spacing)

        self.image(image_path, x=x_offset, y=y_offset, w=img_width, h=cm_height)

        # Alinhar as linhas com o bottom das imagens
        self.set_font("Helvetica", size=12)
        self.text(x_offset - 1.5, y_offset + cm_height, "___")  # Linha à esquerda
        self.text(page_width - x_offset + 0.75, y_offset + cm_height, "___")  # Linha à direita


# Função para gerar o PDF e abrir no navegador
def generate_pdf():
    if not selected_images:
        messagebox.showwarning("Aviso", "Nenhuma imagem selecionada para gerar o PDF.")
        return

    pdf = PDF()
    pdf.add_page()

    for i, image_path in enumerate(selected_images):
        if i > 0 and i % 2 == 0:
            pdf.add_page()
        position = i % 2
        pdf.add_image(image_path, position)

    # Salvar temporariamente o arquivo
    global temp_pdf_path
    temp_pdf_path = os.path.join(tempfile.gettempdir(), "visualizacao_temp.pdf")
    pdf.output(temp_pdf_path)

    # Abrir o PDF no navegador padrão
    webbrowser.open(temp_pdf_path)


# Função para adicionar novas imagens
def select_images():
    file_paths = filedialog.askopenfilenames(title="Selecione as imagens", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp")])

    for path in file_paths:
        if path not in selected_images:
            selected_images.append(path)
            add_thumbnail(path)


# Função para exibir miniaturas das imagens selecionadas
def add_thumbnail(image_path):
    img = Image.open(image_path)
    img.thumbnail((100, 100))
    img_tk = ImageTk.PhotoImage(img)

    frame = tk.Frame(thumbnail_frame, bd=2, relief=tk.RIDGE, bg="#34495e")
    frame.pack(side=tk.LEFT, padx=5, pady=5)

    label = tk.Label(frame, image=img_tk, bg="#34495e")
    label.image = img_tk
    label.pack()

    remove_btn = tk.Button(frame, text="Excluir", command=lambda: remove_image(image_path, frame), bg="#e74c3c", fg="white")
    remove_btn.pack()


# Função para remover imagem selecionada
def remove_image(image_path, frame):
    if image_path in selected_images:
        selected_images.remove(image_path)
        frame.destroy()

# Inicializar interface gráfica em tela maximizada
root = tk.Tk()
root.title("Gerar PDF de Imagens para Canecas")
root.state("zoomed")  # Iniciar em tela maximizada
root.configure(bg="#2c3e50")  # Cor de fundo da janela

# Carregar o ícone como imagem para o título
icon_image = Image.open(resource_path("caneca.png"))
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

# Carregar a imagem da caneca
caneca_image = Image.open(resource_path("caneca.png"))
caneca_image = caneca_image.resize((150, 150))  # Redimensionar para um tamanho adequado
caneca_tk = ImageTk.PhotoImage(caneca_image)

# Exibir a imagem no canto superior esquerdo
caneca_label = tk.Label(root, image=caneca_tk, bg="#2c3e50")
caneca_label.image = caneca_tk  # Manter a referência da imagem
caneca_label.place(x=20, y=20)  # Posição no canto superior esquerdo com uma margem de 10px

# Lista para armazenar as imagens selecionadas
selected_images = []

# Elementos da interface
label = tk.Label(root, text="Escolha as imagens para as canecas", font=("Helvetica", 20, "bold"), fg="#ecf0f1", bg="#2c3e50")
label.pack(pady=20)

# Botões com estilo moderno
btn_style = {
    "font": ("Helvetica", 14, "bold"),
    "bg": "#3498db",
    "fg": "#ecf0f1",
    "activebackground": "#2980b9",
    "activeforeground": "#ecf0f1",
    "bd": 0,
    "relief": tk.RAISED,
    "width": 20
}

btn_select = tk.Button(root, text="Adicionar Imagens", command=select_images, **btn_style)
btn_select.pack(pady=10)

btn_generate = tk.Button(root, text="Gerar PDF", command=generate_pdf, **btn_style)
btn_generate.pack(pady=10)

# Área de thumbnails com fundo diferenciado
thumbnail_frame = tk.Frame(root, bg="#34495e", bd=2, relief=tk.SUNKEN)
thumbnail_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Executar a aplicação
root.mainloop()