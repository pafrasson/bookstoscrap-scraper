# 📚 Books to Scrape - Web Scraper

Um projeto de web scraping usando **Playwright (Python)** para extrair informações de livros do site [Books to Scrape](http://books.toscrape.com).

---

## 🔧 Funcionalidades

- Navega automaticamente por todas as páginas de livros.
- Extrai os seguintes dados de cada livro:
  - Título
  - Tipo de produto
  - Preço (sem e com taxa)
  - Taxa
  - Disponibilidade
  - Rating
  - URL da página
- Salva tudo em um arquivo `books.csv`.

---

## ▶️ Como Executar

### 1. Instale as dependências

```bash
pip install playwright
playwright install
```

### 2. Execute o scraper

```bash
python src/main.py
```

> O navegador será aberto em modo visual (`headless=False`). Você pode alterar isso em `runner.py`.

---

## 💾 Resultado

Será gerado um arquivo chamado:

```
books.csv
```

Exemplo de conteúdo:

| title                  | product_type | price_excl_tax | price_incl_tax | tax   | availability         | url                                       |
|------------------------|--------------|----------------|----------------|-------|----------------------|--------------------------------------------|
| A Light in the Attic   | Books        | £51.77         | £51.77         | £0.00 | In stock (22 available) | http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html |

---

## 📌 Requisitos

- Python 3+
- Playwright

---

## 📄 Licença

Este projeto é apenas para fins educacionais e de demonstração de scraping.