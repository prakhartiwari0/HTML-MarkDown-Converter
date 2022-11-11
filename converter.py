import re
which_to_which = input("Do you want to convert - \n 1.HTML to Markdown\n2.Markdown to HTML\n\nEnter 1 or 2: ")



def htmltomd(source_code):
    # HEADINGS
    # <h1> to #
    heading_dict = {"<h1": "#",
                    "<h2": "##", 
                    "<h3": "###", 
                    "<h4": "####", 
                    "<h5": "#####",
                    "<h6": "######"}
    for key in heading_dict.keys():
        if key in source_code:   
            md_code = re.sub(key, heading_dict[key], source_code)

    md_code = re.sub("</h[1-6]", "\n", md_code)
    md_code = re.sub(">", " ", md_code)


    # md_code = source_code.replace("<h1", "#")
    # md_code = md_code.replace("</h[1-6]", "\n") 
    # md_code = md_code.replace(">", " ")

    # LINKS

    # Remember to put md_code.replace() 
    # and not source_code.replace() to 
    # continue making changes to the modified code.
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
