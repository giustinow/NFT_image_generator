import os
from PIL import Image
import traits_classification

try:
    os.makedirs('./assets/images/generated')
except:
    pass


def generate_images(all_images):
    first_image = Image.open(f'./assets/body_parts/body/Transparent.png').convert('RGBA')
    print('BEGINNING IMAGE GENERATION', end='\n')
    for item in all_images:
        im1 = Image.open(f'./assets/body_parts/body/{traits_classification.body_files[item["Body"]]}.png').convert(
            'RGBA')
        im2 = Image.open(
            f'./assets/body_parts/hand_right/{traits_classification.hand_right_files[item["Hand Right"]]}.png').convert(
            'RGBA')
        im3 = Image.open(
            f'./assets/body_parts/clothes/{traits_classification.clothes_files[item["Clothes"]]}.png').convert('RGBA')
        im4 = Image.open(f'./assets/body_parts/hat/{traits_classification.hat_files[item["Hat"]]}.png').convert(
            'RGBA')

        bg = Image.new('RGBA', first_image.size, 'WHITE')
        com0 = Image.alpha_composite(bg, im1)
        com1 = Image.alpha_composite(com0, im2)
        com2 = Image.alpha_composite(com1, im3)
        com3 = Image.alpha_composite(com2, im4)

        rgb_im = com3.convert('RGB')
        file_name = str(item["tokenId"]) + ".png"

        print('GENERATING IMAGE WITH ID: ', item['tokenId'])

        rgb_im.save("./assets/images/generated/" + file_name, 'PNG')
    print('\n IMAGE GENERATION ENDED')
