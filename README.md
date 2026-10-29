# 📊 ArXiv Graph Theory Daily Monitor

[![Daily ArXiv Graph Papers Monitor](https://github.com/wlomenha/arxiv-graph-monitor/actions/workflows/daily_arxiv.yml/badge.svg)](https://github.com/wlomenha/arxiv-graph-monitor/actions/workflows/daily_arxiv.yml)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Groq API](https://img.shields.io/badge/LLM-Groq%20Cloud-orange.svg)

Uma pipeline automatizada de ponta a ponta que monitora diariamente os novos preprints lançados no **arXiv**, filtra artigos focados em **Teoria dos Grafos e Combinatória**, e gera boletins científicos formatados em Markdown utilizando a API de alto desempenho da **Groq** (`openai/gpt-oss-120b`).

> 🚀 **Acesse o boletim mais recente**: [Ler LATEST.md](./LATEST.md)

---

## 🛠️ Como Funciona o Pipeline

1. **Scraping & Deduplicação**: O script raspa diariamente as categorias `math.CO`, `cs.DS` e `cs.DM`, identifica menções relevantes a grafos, extrai links/autores e elimina artigos duplicados.
2. **Sintetização por IA**: Os artigos são processados em lotes otimizados com pausas para respeitar o *Rate Limit* e enviados para o modelo `openai/gpt-oss-120b` da Groq.
3. **Publicação Automática**: O workflow do GitHub Actions armazena o histórico em `reports/arxiv-YYYY-MM-DD.md` e sobrescreve o arquivo [LATEST.md](./LATEST.md) na raiz do repositório.

---

## 📂 Estrutura do Repositório

- `.github/workflows/daily_arxiv.yml`: Workflow de automação diária (CI/CD)
- `reports/`: Histórico diário de boletins gerados em Markdown
- `LATEST.md`: Último boletim diário atualizado
- `main.py`: Script principal de raspagem e sumarização
- `requirements.txt`: Dependências do projeto Python
- `README.md`: Documentação do projeto

---

## ⚙️ Execução Local

### 1. Clonar o Repositório
```bash
git clone [https://github.com/wlomenha/arxiv-graph-monitor.git](https://github.com/wlomenha/arxiv-graph-monitor.git)
cd arxiv-graph-monitor