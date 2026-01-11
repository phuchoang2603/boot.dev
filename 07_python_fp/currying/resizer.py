def new_resizer(max_width: int, max_height: int):
    def set_min_size(min_width: int = 0, min_height: int = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize_image(width: int, height: int):
            width = max(min(width, max_width), min_width)
            height = max(min(height, max_height), min_height)
            return width, height

        return resize_image

    return set_min_size
