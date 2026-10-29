# 📊 ArXiv Graph Theory Daily Monitor

[![Daily ArXiv Graph Papers Monitor](https://github.com/wlomenha/arxiv-graph-monitor/actions/workflows/daily_arxiv.yml/badge.svg)](https://github.com/wlomenha/arxiv-graph-monitor/actions/workflows/daily_arxiv.yml)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Groq API](https://img.shields.io/badge/LLM-Groq%20Cloud-orange.svg)

Uma pipeline automatizada de ponta a ponta que monitora diariamente os novos preprints lançados no **arXiv**, filtra artigos focados em **Teoria dos Grafos e Combinatória**, e gera boletins científicos formatados em Markdown utilizando a API de alto desempenho da **Groq**.

> 🚀 **Acesse o boletim mais recente**: [Ler LATEST.md](./LATEST.md)

---

## 🛠️ Como Funciona o Pipeline

```mermaid
graph TD
    A[arXiv API / Web Scraping] -->|Categorias: math.CO, cs.DS, cs.DM| B(Filtro de Palavras-Chave)
    B -->|Deduplicação & Lotes| C[Groq LLM API - gpt-oss-120b]
    C -->|Geração de Resumos Executivos| D[Arquivos Markdown Formatados]
    D -->|GitHub Actions Cron| E[Repositório: /reports & LATEST.md]