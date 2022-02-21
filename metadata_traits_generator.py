import json

METADATA_FILENAME = './metadata/traits.json'


def generate_metadata(all_images):
    with open(METADATA_FILENAME, 'w') as file:
        json.dump(all_images, file, indent=4)
