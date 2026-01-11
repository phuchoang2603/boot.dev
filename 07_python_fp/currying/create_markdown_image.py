def create_markdown_image(alt_text: str):
    enclosed_alt_text = f"![{alt_text}]"

    def insert_url(url: str):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        enclosed_url = f"({escaped_url})"
        base_image = enclosed_alt_text + enclosed_url

        def insert_title(title: str | None = None):
            if title is not None:
                enclosed_title = f'"{title}"'
                return f"{base_image[:-1]} {enclosed_title})"
            return base_image

        return insert_title

    return insert_url
