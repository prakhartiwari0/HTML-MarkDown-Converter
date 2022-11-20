import re

INUPT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

which_to_which = input(
    "Do you want to convert - \n 1.HTML to Markdown\n2.Markdown to HTML\n\nEnter 1 or 2: ")


def custom_make_translation(txt, trans):
    # convert multiple string easily with dictionary
    regex = re.compile('|'.join(map(re.escape, trans)))
    return regex.sub(lambda match: trans[match.group(0)], txt)


def htmltomd(source_code):
    # HEADINGS
    # <h1-6> to # - ######

    md_code = custom_make_translation(
        source_code, {f'<h{i}>': '#'*i + ' ' for i in range(1, 7)})
    md_code = custom_make_translation(
        md_code, {f'</h{i}>': '\n' for i in range(1, 7)})

    # LINKS

    return md_code


def mdtohtml(source_code):
    # HEADINGS
    # # to <h1>
    html_code = "This part needs to be programmed"

    # LINKS -> <a href=""> to [Name](URL)

    return html_code



if which_to_which == "1":
    # Create input.txt to take the raw code
    file = open("input.txt", "w")
    file.close()

    # Asking to paste the raw code into input.txt 
    pause = input("Kindly put the HTML code into input.txt, after that press ENTER ")

    # Reading the raw Code
    file = open("input.txt", "r")
    source_html = file.read()
    file.close()

    # Passing the raw code to the function
    converted_code = htmltomd(source_html)

    # Making output.txt and writing the converted code into it
    file = open("output.txt", "w")
    file.write(converted_code)
    file.close()

elif which_to_which == "2":
    # Create input.txt to take the raw code
    file = open("input.txt", "w")
    file.close()

    # Asking to paste the raw code into input.txt
    pause = input("Kindly put the Markdown code into input.txt, after that press ENTER ")

    # Reading the raw Code
    file = open("input.txt", "r")
    source_md = file.read()
    file.close()

    # Passing the raw code to the function
    converted_code = mdtohtml(source_md)

    # Making output.txt and writing the converted code into it
    file = open("output.txt", "w")
    file.write(converted_code)
