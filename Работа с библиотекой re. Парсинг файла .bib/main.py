import re

def parse_bibtex(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        bibtex_data = file.read()

    pattern = re.compile(r'@(\w+)\{(.*?),\s*([^@]*)\}', re.DOTALL) # паттерн для поиска каждой записи в формате BibTeX

    matches = pattern.findall(bibtex_data) # используем findall для нахождения всех соответствий

    parsed_references = []

    for match in matches:
        entry_type = match[0].strip()
        entry_key = match[1].strip()
        entry_body = match[2].strip()

        fields = dict(re.findall(r'(\w+)\s*=\s*{(.*?)}', entry_body, re.DOTALL)) # разбиваем запись на отдельные поля

        # проверяем, что все необходимые поля присутствуют в записи
        if 'Author' in fields and 'Title' in fields and 'Journal' in fields and 'Year' in fields:
            authors = fields['Author']
            title = fields['Title']
            journal = fields['Journal']
            year = fields['Year']

            reference = f"{authors.strip()}, {title.strip()} // {journal.strip()}.– {year.strip()}." # формат ГОСТ

            # проверяем наличие дополнительных полей и их добавление
            if 'Volume' in fields:
                reference += f"– Vol. {fields['Volume'].strip()}."
            if 'Pages' in fields:
                reference += f"– P. {fields['Pages'].strip()}."
            if 'DOI' in fields:
                reference += f" DOI: {fields['DOI'].strip()}"
            if 'Language' in fields:
                reference += f" Language: {fields['Language'].strip()}"

                if fields['Language'] == 'russian':
                  reference = reference.replace("Vol", "Звук")
                  reference = reference.replace("– P.", "- С.")

            parsed_references.append(reference)

    return parsed_references

file_path = '/content/drive/MyDrive/biblio.bib'

references = parse_bibtex(file_path)
for reference in references:
    print(reference)