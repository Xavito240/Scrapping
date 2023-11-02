import tkinter as tk
import requests
from bs4 import BeautifulSoup

def scrape_technical_specifications(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    technical_specifications = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        specs_div = soup.find('div', class_='c-specs table-responsive-md')

        if specs_div:
            technical_specifications.append(specs_div.get_text(separator='\n'))
        else:
            technical_specifications.append("Caractéristiques techniques introuvables sur la page.")
    else:
        technical_specifications.append(f"La requête a échoué. Statut de réponse : {response.status_code}")

    return technical_specifications

def get_url_and_scrape():
    url = url_entry.get()
    caracteristiques = scrape_technical_specifications(url)
    
    text_box.delete(1.0, tk.END)
    
    for caract in caracteristiques:
        text_box.insert(tk.END, caract + '\n')

root = tk.Tk()
root.title("Scraping des Caractéristiques Techniques")

url_label = tk.Label(root, text="URL du produit:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

scrape_button = tk.Button(root, text="Scrape", command=get_url_and_scrape)
scrape_button.pack()

text_box = tk.Text(root, width=800, height=200, wrap=tk.WORD)
text_box.pack()

scrollbar = tk.Scrollbar(root, command=text_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=scrollbar.set)

root.mainloop()
