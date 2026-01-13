import os
import shutil


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
