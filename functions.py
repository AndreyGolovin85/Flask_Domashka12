import json


def load_json_fliles(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def overwrite_json_files(list, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(list, file)



def search_post(substr, path):
    list_post = load_json_fliles(path)
    found_list_post = []
    for post in list_post:
        if substr.lower() in post["content"].lower():
            found_list_post.append(post)
    return found_list_post

print(load_json_fliles("data/posts.json"))