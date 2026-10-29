import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from IPython.display import Markdown, display

# Configuração para Produção via Groq Cloud
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "openai/gpt-oss-20b"

# Lista de URLs do arXiv para monitoramento
TARGET_URLS = [
    "https://arxiv.org/list/math.CO/new",
    "https://arxiv.org/list/cs.DS/recent",
    "https://arxiv.org/list/cs.DM/recent"
]

system_prompt = """
You are a senior academic researcher specialized in Graph Theory and Combinatorics.
Your task is to generate a clean, structured bulletin from a list of arXiv preprints focused specifically on Graph Theory.

CRITICAL RULES:
1. Process EVERY paper provided in the input list individually.
2. DO NOT write a high-level general overview or summary of the page.
3. Respond in clear Markdown with headers.

For EACH paper, format as follows:
### [Number] Title of the Paper
- **Main Result/Innovation**: 2 to 3 concise sentences explaining the primary finding or theorem proved in the abstract.
- **Key Concepts / Graph Topics**: List specific graph types, parameters, or techniques involved (e.g., Chromatic Number, Planar Graphs, Spectral Graph Theory, Extremal Graphs).

---
"""

user_prompt_prefix = """
Here is the filtered list of new arXiv papers related to Graph Theory.
Process each paper individually and format the executive summary in English:

"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

GRAPH_KEYWORDS = [
    "graph", "graphs", "vertex", "vertices", "edge", "edges",
    "clique", "chromatic", "adjacency", "degree sequence",
    "bipartite", "hypergraph", "tree", "trees", "path convexity",
    "eulerian", "hamiltonian", "spectral", "laplacian", "coloring", "decomposition", "degree",
    "subgraph", "hypergraphs", "connectivity", "matching", "domination", 
    "ramsey", "planar", "extremal", "isomorphism", "colorability", "colourability" 
]

def is_graph_paper(title, abstract):
    """Verifica se o título ou o resumo contém termos típicos de Teoria dos Grafos."""
    text_to_check = (title + " " + abstract).lower()
    return any(keyword in text_to_check for keyword in GRAPH_KEYWORDS)

def fetch_graph_papers_from_urls(urls):
    """Raspa e filtra artigos de grafos de múltiplas URLs do arXiv, eliminando duplicatas."""
    all_papers = []
    seen_titles = set()
    
    for url in urls:
        print(f"Scraping source: {url}...")
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code != 200:
                print(f"Failed to fetch {url} (Status: {response.status_code})")
                continue
                
            soup = BeautifulSoup(response.content, "html.parser")
            dt_list = soup.find_all("dt")
            dd_list = soup.find_all("dd")
            
            for dt, dd in zip(dt_list, dd_list):
                title_div = dd.find("div", class_="list-title")
                title = title_div.text.replace("Title:", "").strip() if title_div else "No title"
                
                # Normaliza o título para desduplicação
                normalized_title = title.lower().strip()
                if normalized_title in seen_titles:
                    continue
                
                abstract_p = dd.find("p", class_="mathjax")
                abstract = abstract_p.text.strip() if abstract_p else "No abstract available"
                
                if is_graph_paper(title, abstract):
                    seen_titles.add(normalized_title)
                    all_papers.append({
                        "title": title,
                        "abstract": abstract
                    })
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            
    return all_papers

def messages_for(batch_text):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + batch_text}
    ]

def summarize_batch(batch_text):
    """Envia um lote individual para a API da Groq."""
    client = OpenAI(
        base_url=GROQ_BASE_URL,
        api_key=GROQ_API_KEY
    )
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages_for(batch_text),
        temperature=0.2
    )
    return response.choices[0].message.content

def summarize_all_in_batches(urls, batch_size=5):
    """Orquestra a raspagem de múltiplas fontes, fatiamento em lotes e junção das respostas."""
    papers = fetch_graph_papers_from_urls(urls)
    total = len(papers)
    
    if total == 0:
        return "No Graph Theory papers were found across the provided arXiv categories today."
        
    print(f"\nFound {total} unique Graph Theory papers across all sources.")
    print(f"Processing in batches of {batch_size} via Groq ({MODEL_NAME})...\n")
    
    full_report = []
    
    for i in range(0, total, batch_size):
        batch = papers[i : i + batch_size]
        
        batch_text = ""
        for idx, paper in enumerate(batch, start=i+1):
            batch_text += f"Paper {idx}:\nTITLE: {paper['title']}\nABSTRACT: {paper['abstract']}\n\n"
            
        print(f"Sending batch {i//batch_size + 1} (Papers {i+1} to {min(i+batch_size, total)})...")
        
        summary = summarize_batch(batch_text)
        full_report.append(summary)
        
    return "\n\n---\n\n".join(full_report)

def display_summary(urls):
    summary = summarize_all_in_batches(urls, batch_size=5)
    display(Markdown(summary))

def main():
    report = summarize_all_in_batches(TARGET_URLS, batch_size=5)
    print("\n=== FINAL BULLETIN ===\n")
    print(report)

if __name__ == "__main__":
    main()