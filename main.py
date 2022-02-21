import random

import image_generator
import metadata_image_generator
import metadata_traits_generator
import traits
import traits_count

TOTAL_IMAGES = 10
all_images = []


def create_new_image():
    new_image = {"Body": random.choices(traits.body, traits.body_weights)[0],
                 "Hand Right": random.choices(traits.hand_right, traits.hand_right_weights)[0],
                 "Clothes": random.choices(traits.clothes, traits.clothes_weights)[0],
                 "Hat": random.choices(traits.hat, traits.hat_weights)[0]
                 }
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


def count_traits():
    for image in all_images:
        traits_count.body_count[image["Body"]] += 1
        traits_count.hand_right_count[image["Hand Right"]] += 1
        traits_count.clothes_count[image["Clothes"]] += 1
        traits_count.hat_count[image["Hat"]] += 1


def main():
    for i in range(TOTAL_IMAGES):
        new_trait_image = create_new_image()
        all_images.append(new_trait_image)

    i = 0
    for item in all_images:
        item["tokenId"] = i
        i += 1
    count_traits()
    image_generator.generate_images(all_images)

    metadata_traits_generator.generate_metadata(all_images)
    metadata_image_generator.generate_metadata()


if __name__ == '__main__':
    main()
    pass
