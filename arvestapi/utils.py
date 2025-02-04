import json
import os
import datetime

def debug_print_response_body(rb, obj):
    if obj.debug:
        print(f"---\nDebug: {obj}")
        pretty_print_dict(rb, 1)
        print("---\n")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        write_json(rb, os.path.join(os.getcwd(), "debug", f"{current_time}_{obj}.json"))

def pretty_print_dict(d, level):
    tab = ""
    for i in range(level):
        tab = tab + " "
    for item in d:
        if isinstance(d[item], dict):
            pretty_print_dict(d[item], level + 1)
        else:
            print(f"{tab}{item} : {str(d[item])}")

def write_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)