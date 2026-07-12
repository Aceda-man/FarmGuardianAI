from PIL import Image
import io


def process_crop_image(uploaded_file):

    try:

        # Read image

        image_bytes = uploaded_file.read()


        image = Image.open(
            io.BytesIO(image_bytes)
        )


        # Basic image information

        image_info = {

            "filename":
            uploaded_file.name,


            "format":
            image.format,


            "size":
            image.size,


            "description":
            """
Crop image uploaded by farmer.

Image will be analyzed by
Gemma multimodal intelligence
for disease, pest damage,
nutrient deficiency and stress signs.
"""
        }


        return image, image_info



    except Exception as e:


        print(
            "Image processing error:",
            e
        )


        return None, None