import json
import yaml
#ex 1

dict_ = {'items': {'name': 'Mher', 'surname': 'Petrosyan'}, 'other_item': {'age': 26, 'status': 'drunk'}}
# list_ = [123, True, {'name': 'Mher', 'surname': 'Petrosyan'}, ([1, 2, 3])]
with open('new_json.json', 'w') as f:
    json.dump(dict_, f, indent=4)


def json_text_parser(json_file):
    with open(json_file, 'r') as json_f:
        data = json.load(json_f)
        str_data = str(data)
    with open('text.txt', 'a') as text_file:
        text_file.write(str_data)


json_text_parser('new_json.json')


def json_yaml_parser(json_file):
    with open(json_file, 'r') as json_f:
        data_ = json.load(json_f)
    with open('new_file.yaml', 'w') as yaml_file:
        yaml.dump(data_, yaml_file)


json_yaml_parser('new_json.json')


def yaml_json_parser(yaml_file):
    with open(yaml_file, 'r') as yaml_f:
        data_ = yaml.load(yaml_f, Loader=yaml.FullLoader)
    with open('new_json.json', 'w') as json_f:
        json.dump(data_, json_f, indent=4)


yaml_json_parser('new_file.yaml')
