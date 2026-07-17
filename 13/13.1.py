import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = ""
    inside_tag = False

    for symbol in html:
        if symbol == "<":
            inside_tag = True
        elif symbol == ">":
            inside_tag = False
        elif not inside_tag:
            text += symbol

    lines = text.split("\n")

    with codecs.open(result_file, "w", "utf-8") as file:
        for line in lines:
            line = line.strip()
            if line != "":
                file.write(line + "\n")


delete_html_tags("draft.html")
