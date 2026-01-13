import os
import shutil
import re
from block_markdown import markdown_to_html_node
from pathlib import Path
from config import TEMPLATE_PATH


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
            shutil.copy(filepath, despath)
            print(f"Copied {filename} to {despath}")
        else:
            copy_files(filepath, despath, is_root=False)


def extract_title(markdown: str) -> str:
    match = re.search(r"^#\s(.*?)\n", markdown)
    if match is None:
        raise Exception("Error: title not found")
    else:
        return match.group(1)


def apply_template(template_path: str, title: str, content: str) -> str:
    with open(template_path, "r") as f:
        template = f.read()

    return template.replace("{{ Title }}", title).replace("{{ Content }}", content)


def markdown_file_to_html(markdown_path: str) -> tuple[str, str]:
    with open(markdown_path, "r") as f:
        markdown = f.read()

    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()

    return (title, html)


def generate_page(
    from_path: str, dest_path: str, template_path: str = TEMPLATE_PATH
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    title, html = markdown_file_to_html(from_path)
    final_html = apply_template(template_path, title, html)

    with open(dest_path, "w") as f:
        f.write(final_html)


def generate_pages(src_dir: str, des_dir: str) -> None:
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)

    for filename in os.listdir(src_dir):
        filepath = os.path.join(src_dir, filename)
        despath = os.path.join(des_dir, filename)

        if os.path.isfile(filepath):
            despath_html = str(Path(despath).with_suffix("html"))
            generate_page(from_path=filepath, dest_path=despath_html)
        else:
            generate_pages(src_dir=filepath, des_dir=despath)
