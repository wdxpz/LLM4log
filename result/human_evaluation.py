import json

with open("result/human_evaluation_origin.json", "r") as f:
    human_result = json.load(f)
print("num of original data: ", len(human_result["IP"]), len(human_result["URL"]))
human_result["IP"] = list(set(human_result["IP"]))
human_result["URL"] = list(set(human_result["URL"]))

with open("result/human_evaluation.json", "w") as f:
    json.dump(human_result, f, indent=4)

print("num of removed data: ", len(human_result["IP"]), len(human_result["URL"]))
