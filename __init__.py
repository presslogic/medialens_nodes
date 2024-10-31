from PIL import Image
import numpy as np
import base64
from io import BytesIO
import os
import folder_paths

class image_save_path:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'
        self.prefix_append = ''
            
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                'filename': ('STRING', {'default': ''}),
                'folder': ('STRING', {'default': ''}),
            }
        }
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "medialens"
    FUNCTION = "image_save_path"
    def save_images(self, images, filename, folder):
        output_path = os.path.join(self.output_dir, folder)
        os.makedirs(output_path, exist_ok=True)
        # pil_images: List[Image.Image] = []
        paths = []
        for index, image in enumerate(images):
            filename = f'{filename}_{index}.png'
            img = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
            image_path = os.path.join(output_path, filename)
            img.save(image_path, compress_level=4)
            paths.append(image_path)
            # pil_images.append(img)
        
        results = [
            {
                "paths": paths,
                "type": "output",
            }
        ]
        return {"ui": {"string": results}}


NODE_CLASS_MAPPINGS = {
    "Images save path": image_save_path
}