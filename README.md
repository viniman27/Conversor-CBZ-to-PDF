# Conversor CBZ/CBR para PDF

Este script em Python facilita a conversão de quadrinhos digitais nos formatos **.cbz** (ZIP) e **.cbr** (RAR) em documentos PDF.

## Funcionalidades

- **Extração** automática de arquivos `.cbz` e `.cbr`.
- **Conversão** de todas as imagens extraídas em um único PDF.
- **Salvamento** dos PDFs na pasta `PDFs/` dentro do diretório de entrada.

## Pré-requisitos

- **Python 3.7+**
- **Bibliotecas Python** (instale via `pip`):
  ```bash
  pip install pillow patool rarfile
  ```
- **Ferramenta de extração RAR** (`unar` ou `unrar`):
  - **MacPorts**:
    ```bash
    sudo port install unar
    ```
  - **Instalação manual** (exemplo com `unar` v1.10.1):
    ```bash
    curl -L https://github.com/MacPaw/unar/releases/download/1.10.1/unar-1.10.1-macOS.zip -o unar.zip
    unzip unar.zip -d unar-bin
    sudo mv unar-bin/unar /usr/local/bin
    sudo mv unar-bin/lsar /usr/local/bin
    sudo chmod +x /usr/local/bin/unar /usr/local/bin/lsar
    rm -rf unar.zip unar-bin
    ```

> **Importante:** verifique se o comando `unar` está no PATH:
> ```bash
> which unar
> ```

## Instalação do projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/<seu-usuario>/<seu-repo>.git
   cd <seu-repo>
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como usar

1. Coloque seus arquivos `.cbz` e `.cbr` na pasta `HqsIneditas/` ou ajuste a variável `input_folder` no script.  
2. Execute o script:
   ```bash
   python3 conversorcbz.py
   ```
3. Os PDFs serão gerados em `HqsIneditas/PDFs/`.

## Estrutura do projeto

```text
ConversorCBZ/
├── HqsIneditas/
│   ├── AbsoluteFlash003.cbz
│   ├── AbsoluteBatman008.cbr
│   └── PDFs/
│       ├── AbsoluteFlash003.pdf
│       └── AbsoluteBatman008.pdf
├── conversorcbz.py
└── README.md
```

## Personalização

- **Diretórios**: ajuste `input_folder` e `output_folder` no topo do `conversorcbz.py`.  
- **Formatos de imagem**: modifique a lista de extensões na função que coleta arquivos.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

*Desenvolvido por viniciusassumpcao.*
