import json
import os


def merge_new_json_files(folder_path, output_file):
    '''new json file schema:IP and URL are arrays, items are dicts, each item has key "IP"/"URL" and "count"
    for memory, we add the counts and compare the other keys in the dcits
    folder_path: path of folder contains multiple json files
    output_file: path of output merged json file
    '''
    merged_dict = {"IP": [], "URL": [], "memory": []}
    ip_dict = {}
    url_dict = {}
    memory_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                # merge IP and URL
                for ip_entry in data.get("IP", []):
                    if ip_entry["IP"] in ip_dict:                       
                        ip_dict[ip_entry["IP"]] += ip_entry["count"]
                    else:
                        ip_dict[ip_entry["IP"]] = ip_entry["count"]
                for url_entry in data.get("URL", []):
                    if url_entry["URL"] in url_dict:
                        url_dict[url_entry["URL"]] += url_entry["count"]
                    else:
                        url_dict[url_entry["URL"]] = url_entry["count"]
                # todo merge memory
    
    merged_dict["IP"] = [{"IP": ip, "count": count} for ip, count in ip_dict.items()]
    merged_dict["URL"] = [{"URL": url, "count": count} for url, count in url_dict.items()]
                          
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged_dict, f, ensure_ascii=False)


merge_new_json_files("result/128k-18-result","result/128k-18-result/merge_128k_18.json")

merge_new_json_files("result/128k-18-result/human_result","result/128k-18-result/human_result/human_128k_18.json")
