from textnode import TextNode, TextType
import os
import shutil
from generate import generate_page

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)
    print("Searching for markdown files in content directory...")
    finder_to_generator("content/")


def copy_static(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_static(from_path, dest_path)

def finder_to_generator(directory_path):
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            full_path = os.path.join(directory_path, filename)
            
            if os.path.isfile(full_path):
                if filename.endswith(".md"):
                    html_filename = filename.replace(".md", ".html")
                    public_dir_path = directory_path.replace("content", "public")
                    dest_full_path = os.path.join(public_dir_path, html_filename)
                    os.makedirs(public_dir_path, exist_ok=True)
                    generate_page(full_path, "template.html", dest_full_path)
            else:
                finder_to_generator(full_path)


if __name__ == "__main__":
    main()