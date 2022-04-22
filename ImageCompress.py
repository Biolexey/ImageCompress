import os
import glob
from PIL import Image

dst_dir = 'data/temp/images_compressd'
os.makedirs(dst_dir, exist_ok=True)

#圧縮したい拡張子を入力
files = glob.glob('./data/temp/images/*.png')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((240, 135))
    root, ext = os.path.splitext(f)
    basename = os.path.basename(root)
    img_resize.save(os.path.join(dst_dir, basename + ext))