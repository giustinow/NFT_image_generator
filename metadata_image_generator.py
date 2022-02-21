import json

IMAGES_BASE_URL = 'https://gateway.pinata.cloud/ipfs/QmdKWpQ6UReLMdQ7SckKExkRq4zWWi1B7T3mWEFv87bjWb'
PROJECT_NAME = 'Massi NFT'


def get_attribute(key, value):
    return {
        'trait_type': key,
        'value': value
    }


def generate_metadata():
    file = open('./metadata/traits.json')
    data = json.load(file)

    for element in data:
        token_id = element['tokenId']
        token = {
            "image": IMAGES_BASE_URL + str(token_id) + '.png',
            "tokenId": token_id,
            "name": PROJECT_NAME + ' ' + str(token_id),
            "attributes": []
        }
        token["attributes"].append(get_attribute("Body", element["Body"]))
        token["attributes"].append(get_attribute("Clothes", element["Clothes"]))
        token["attributes"].append(get_attribute("Hand Right", element["Hand Right"]))
        token["attributes"].append(get_attribute("Hat", element["Hat"]))

        with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
            json.dump(token, outfile, indent=4)

    file.close()
