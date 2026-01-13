import os
import shutil
import re
from block_markdown import markdown_to_html_node


def copy_files(src_dir: str, des_dir: str, is_root: bool = True) -> None:
    # Only delete and recreate the destination at the root level
    if is_root:
        if os.path.exists(des_dir):
            shutil.rmtree(des_dir)
        os.mkdir(des_dir)
    else:
        if not os.path.exists(des_dir):
            os.mkdir(des_dir)

    for filename in os.listdir(src_dir):
        filepath = os.path.join(src_dir, filename)
        despath = os.path.join(des_dir, filename)

        if os.path.isfile(filepath):
            try:
                shutil.copy(filepath, despath)
                print(f"Copied {filename} to {despath}")
            except Exception as e:
                raise Exception(f"Error copying {filename}: {e}")
        else:
            copy_files(filepath, despath, is_root=False)


def extract_title(markdown: str) -> str:
    match = re.search(r"^#\s(.*?)\n", markdown)
    if match is None:
        raise Exception("Error: title not found")
    else:
        return match.group(1)


def generate_page(
    from_path: str, dest_path: str, template_path: str = "template.html"
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        with open(from_path, "r") as f:
            markdown = f.read()

        with open(template_path, "r") as f:
            template = f.read()

        title = extract_title(markdown)
        html = markdown_to_html_node(markdown).to_html()

        template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

        with open(dest_path, "w") as f:
            f.write(template)
    except Exception as e:
        raise Exception(f"Error: {e}")


def generate_pages(src_dir: str, des_dir: str) -> None:
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)

    for filename in os.listdir(src_dir):
        filepath = os.path.join(src_dir, filename)
        despath = os.path.join(des_dir, filename)

        if os.path.isfile(filepath):
            try:
                despath_html = despath.split(".")[0] + ".html"
                generate_page(from_path=filepath, dest_path=despath_html)
            except Exception as e:
                raise Exception(f"Error generating {filename}: {e}")
        else:
            generate_pages(src_dir=filepath, des_dir=despath)
