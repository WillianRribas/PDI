
# 🖼️ Processamento Digital de Imagens (PDI) - GUI com Tkinter

## 📖 Descrição

Este projeto é uma aplicação gráfica para **processamento digital de imagens (PDI)** utilizando **Python** com a biblioteca **Tkinter**. A aplicação implementa um conjunto de transformações geométricas e filtros básicos, permitindo carregar, visualizar, processar e salvar imagens.

O sistema possui um menu intuitivo com opções para transformação, aplicação de filtros e manipulação de imagens. Além disso, está preparado para a expansão com funções avançadas de **morfologia matemática** e **extração de características**.

## 🎯 Funcionalidades Implementadas

### ✅ Menu Arquivo
- **Abrir Imagem:** carrega uma imagem do disco.
- **Salvar Imagem:** salva a imagem processada.
- **Sobre:** exibe informações sobre o autor e o projeto.
- **Sair:** encerra a aplicação.

### ✅ Transformações Geométricas
- **Transladar:** desloca a imagem horizontal e verticalmente.
- **Rotacionar:** rotaciona a imagem por um ângulo definido.
- **Espelhar:** cria uma cópia espelhada horizontalmente.
- **Aumentar:** amplia a imagem por um fator definido.
- **Diminuir:** reduz a imagem por um fator definido.

### ✅ Filtros
- **Grayscale:** converte a imagem para tons de cinza.
- **Passa Baixa:** suaviza a imagem utilizando uma média de pixels vizinhos.
- **Passa Alta:** realça as bordas através de uma máscara de convolução.
- **Threshold:** aplica binarização com um limiar definido.

## 🚀 Funcionalidades Futuras

### ✅ Morfologia Matemática
- **Dilatação**
- **Erosão**
- **Abertura**
- **Fechamento**

### ✅ Extração de Características
- **Desafio:** funcionalidade ainda a ser definida, com foco em técnicas avançadas de PDI.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `Tkinter`: interface gráfica.
  - `PIL (Pillow)`: manipulação de imagens.
  - `math`: funções matemáticas.
  - `filedialog`, `simpledialog`, `messagebox`: interação com o usuário.

## ▶️ Como Executar

1. **Pré-requisitos:**
   - Python 3 instalado.
   - Biblioteca Pillow instalada:

     ```bash
     pip install pillow
     ```

2. **Execução:**
   - Execute o script no terminal ou IDE de sua preferência:

     ```bash
     python "PDI - Willian dos Santos Ribas - Etapa 1.py"
     ```

3. **Uso:**
   - Utilize o menu **Arquivo** para abrir ou salvar imagens.
   - Aplique as **transformações geométricas** e **filtros** via os menus correspondentes.
   - Visualize a imagem original e a imagem processada lado a lado.

## 📝 Observações

- O sistema é **modular** e preparado para fácil expansão.
- Todos os efeitos são aplicados diretamente sobre uma cópia da imagem original.
- A aplicação exibe as imagens redimensionadas para melhor visualização na interface.

## 👨‍💻 Autor

Projeto desenvolvido por **Willian dos Santos Ribas**.
