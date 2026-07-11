from PIL import Image
import io


def process_crop_image(uploaded_file):

    try:

        image = Image.open(
            uploaded_file
        )


        # Resize for AI efficiency

        image.thumbnail(
            (512,512)
        )


        image_info = {


            "filename":
            uploaded_file.name,


            "format":
            image.format,


            "size":
            image.size,


            "mode":
            image.mode,


            "description":

            """
Crop image uploaded by farmer.

Gemma 4 vision model will analyze:

- Leaf colour
- Lesions
- Pest damage
- Plant stress
- Disease symptoms

            """

        }


        return image, image_info



    except Exception as e:


        print(e)

        return None, None