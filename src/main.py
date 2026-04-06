from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_files_recursive
from inline_markdown import generate_page, generate_pages_recursive

def main():

    

    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_files_recursive("./static", "./public")

    generate_pages_recursive("content", "template.html", "./public")





main()