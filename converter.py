import re

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

def html_to_markdown(html):
    # convert headings
    html = re.sub(r"<h([1-6])>(.+?)</h[1-6]>", lambda m: "#" * int(m.group(1)) + " " + m.group(2), html)
    # convert anchor tags
    html = re.sub(r'<a href="(.+?)">(.+?)</a>', r"[\2](\1)", html)
    return html

def markdown_to_html(markdown):
    # convert headings
    markdown = re.sub(r"^(#+)(.+)$", lambda m: "<h" + str(len(m.group(1))) + ">" + m.group(2) + "</h" + str(len(m.group(1))) + ">", markdown, flags=re.MULTILINE)
    # convert anchor tags
    markdown = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown)
    return markdown

which_to_which = input("Do you want to convert?\n1. HTML to Markdown\n2. Markdown to HTML\nEnter 1 or 2: ")

if which_to_which == "1":
    # Create input.txt to take the raw code
    file = open(INPUT_FILE_NAME, "w")
    file.close()

    # Asking to paste the raw code into input.txt
    pause = input(
        "Kindly put the HTML code into input.txt, after that press ENTER ")

    # Reading the raw Code
    file1 = open(INPUT_FILE_NAME, "r")
    # Making output.txt and writing the converted code into it
    file2 = open(OUTPUT_FILE_NAME, "w")

    for line in file1.readlines():
        # Passing the raw code to the function
        file2.write(html_to_markdown(line))

    file1.close()
    file2.close()

elif which_to_which == "2":
    # Create input.txt to take the raw code
    file = open(INPUT_FILE_NAME, "w")
    file.close()

    # Asking to paste the raw code into input.txt
    pause = input(
        "Kindly put the Markdown code into input.txt, after that press ENTER ")

    # Reading the raw Code
    file1 = open(INPUT_FILE_NAME, "r")
    # Making output.txt and writing the converted code into it
    file2 = open(OUTPUT_FILE_NAME, "w")

    for line in file1.readlines():
        # Passing the raw code to the function
        file2.write(markdown_to_html(line))

    file1.close()
    file2.close()
