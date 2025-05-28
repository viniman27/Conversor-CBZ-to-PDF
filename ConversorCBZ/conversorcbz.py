import os
import shutil
import tempfile
from PIL import Image
import patoolib

def extract_archive(archive_path: str, extract_dir: str) -> None:
    """
    Extrai CBZ/CBR para a pasta temporária usando patool.
    """
    patoolib.extract_archive(archive_path, outdir=extract_dir)

def convert_images_to_pdf(image_paths: list[str], output_pdf_path: str) -> None:
    """
    Carrega as imagens, converte para RGB e salva em um PDF.
    """
    images = []
    for img_path in image_paths:
        with Image.open(img_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            images.append(img.copy())
    if not images:
        raise ValueError("Nenhuma imagem encontrada para conversão.")
    first, rest = images[0], images[1:]
    first.save(output_pdf_path, "PDF", resolution=100.0, save_all=True, append_images=rest)

def main():
    # Pasta contendo os CBZ/CBR
    input_folder = "" 
    output_folder = os.path.join(input_folder, "PDFs")
    os.makedirs(output_folder, exist_ok=True)

    # Diretório temporário para extração
    temp_dir = tempfile.mkdtemp()

    for filename in os.listdir(input_folder):
        name, ext = os.path.splitext(filename)
        if ext.lower() in [".cbz", ".cbr"]:
            archive_path = os.path.join(input_folder, filename)
            print(f"Processando: {archive_path}")

            # Limpa conteúdo anterior do temp_dir
            for entry in os.listdir(temp_dir):
                path = os.path.join(temp_dir, entry)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)

            # Extrai CBZ/CBR
            extract_archive(archive_path, temp_dir)

            # Coleta todos os arquivos de imagem da extração
            image_files = []
            for root, _, files in os.walk(temp_dir):
                for f in files:
                    if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".gif", ".webp")):
                        image_files.append(os.path.join(root, f))
            image_files.sort()

            # Converte para PDF
            output_pdf = os.path.join(output_folder, f"{name}.pdf")
            convert_images_to_pdf(image_files, output_pdf)
            print(f"PDF salvo em: {output_pdf}")

    # Remove diretório temporário
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
