import json

with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    print(type(load_dict))
    print(load_dict)
    load_dict['video-option']['frame-rate-select'] = 144
with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'w', encoding='utf-8') as f:
    json.dump(load_dict, load_f, ensure_ascii=False)
    print(type(load_dict))
    print(load_dict)

