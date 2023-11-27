from jinja2 import Environment, FileSystemLoader, select_autoescape

# Vaste lijst van auteursnamen
authors = ["Vincent", "Alice", "Bob", "Kobe", "Dario"]

# Maak de lege matrix
plagiarism_matrix = {author: {other_author: [] for other_author in authors if other_author != author} for author in authors}

# Voeg handmatig een paar opmerkingen toe (je kunt dit aanpassen op basis van je gegevens)
plagiarism_matrix["Vincent"]["Alice"] = ["dezelfde verdachte fout"]
plagiarism_matrix["Alice"]["Bob"]= ["duidelijke plagiaat"]
plagiarism_matrix["Kobe"]["Dario"] = ["potentieel plagiaat"]

# Toon de datastructuur
print(plagiarism_matrix)

# Maak een alias mapping voor privacy
alias_mapping = {author: f"author {i+1}" for i, author in enumerate(authors)}

# Configureer de Jinja Environment
env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

# Laad het HTML-template
template = env.get_template("outputtemplate.html")

# Vraag de gebruiker om de uitvoerbestandsnaam
output_file = input("Geef de naam van het uitvoerbestand (bijvoorbeeld: output.html): ")

# Render het HTML-rapport en sla het op
with open(output_file, "w") as f:
    f.write(template.render(matrix=plagiarism_matrix, alias_mapping=alias_mapping))

print(f"Rapport gegenereerd als {output_file}")
