import re
import os
import json
from loguru import logger
from utils.utiles import read_log_file,save_json_file


def mkdir(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)

def load_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def extract_re(file_path, save_dir):
    """extract IPs and URLfrom log file using regular expression
    file_path: str log file to extract
    save_dir: str directory to save the result
    """
    text_re = read_log_file(file_path)
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    IP = re.findall(ip_pattern, text_re)
    IP = list(set(IP))
    # logger.info("IP:", IP)
    logger.info(f"Total IPs found:{len(IP)}")

    URL_pattern = r"([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|[0-9-]+(?:\.[0-9]+){3})"
    URL = re.findall(URL_pattern, text_re)
    URL = list(set(URL) - set(IP))  # remove IP in URL
    # logger.info(f"URL:{URL}")
    logger.info(f"Total URL found:{len(URL)}")

    Result = {}
    Result["IP"] = IP
    Result["URL"] = URL
    mkdir(save_dir)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    save_name = os.path.join(save_dir, f"result_re_{file_name}.json")

    with open(save_name, "w") as f:
        json.dump(Result, f, indent=4)
    return Result


def recall_llm(predict_result, standard_result):
    """calculate the recall of LLM"""
    recall_ip = len(set(predict_result["IP"])&set(standard_result["IP"])) / len(
        set(standard_result["IP"])
    )

    recall_url = len( set(predict_result["URL"])&set(standard_result["URL"])) / len(
        set(standard_result["URL"])
    )

    return recall_ip, recall_url


def precision_llm(predict_result, standard_result):
    """calculate the precision of LLM"""    
    precision_ip = len(set(predict_result["IP"])&set(standard_result["IP"])) / len(set(predict_result["IP"]))
    precision_url = len(set(predict_result["URL"])&set(standard_result["URL"])) / len(set(predict_result["URL"]))
    return precision_ip, precision_url


def pure_llm(llm_result: dict, standard_result: dict)->dict:
    """exchange these misclassified url/ip(comparedd with standard result)
    """
    new_LLM_result = {}
    original_ip = set(llm_result["IP"])
    original_url = set(llm_result["URL"])
    url_in_ip = list(set(llm_result["IP"]) & set(standard_result["URL"]))
    logger.info(f"nums of URL in IP:{len(url_in_ip)}")
    ip_in_url = list(set(llm_result["URL"]) & set(standard_result["IP"]))
    logger.info(f"nums of IP in URL:{len(ip_in_url)}")
    ip_pure = list(original_ip - set(url_in_ip))
    url_pure = list(original_url - set(ip_in_url))
    logger.info(f"nums of pure IP:{len(ip_pure)}")
    logger.info(f"nums of pure URL:{len(url_pure)}")
    new_LLM_result["IP"] = list(set(ip_pure+ip_in_url))
    new_LLM_result["URL"] = list(set(url_pure+url_in_ip))
    logger.info(f"nums of pure IP after exchange:{len(new_LLM_result['IP'])}")
    logger.info(f"nums of pure URL after exchange:{len(new_LLM_result['URL'])}")
    return new_LLM_result


def get_miss_case(result_predict, result_standard):
    """get miss extracted IPs and URL for predict result from standard result"""
    miss_case = {}
    miss_case["IP"] = list(set(result_standard["IP"]) - set(result_predict["IP"]))
    miss_case["URL"] = list(set(result_standard["URL"]) - set(result_predict["URL"]))
    return miss_case


def get_bad_case(result_predict, result_standard):
    """get bad extracted IPs and URL for predict result from standard result"""
    bad_case = {}
    bad_case["IP"] = list(set(result_predict["IP"]) - set(result_standard["IP"]))
    bad_case["URL"] = list(set(result_predict["URL"]) - set(result_standard["URL"]))
    return bad_case


def evaluate_result(config):
    '''evaluate the result of RE and LLM
    config: edict object
    '''
    logger.info("Running in test mode")
    logger.info("loading results")
    llm_result_file = config.test.llm_result_file
    re_result_file = config.test.re_result_file
    human_result_file = config.test.human_result_file
    logger.info(f"llm_result_file: {llm_result_file}")
    logger.info(f"re_result_file: {re_result_file}")
    logger.info(f"human_result_file: {human_result_file}")
    # load json file
    llm_result = load_json(llm_result_file)
    re_result = load_json(re_result_file)
    human_result = load_json(human_result_file)
    logger.info("human resut as standard")
    logger.info("num of ip in human result:{}".format(len(human_result["IP"])))
    logger.info("num of url in human result:{}".format(len(human_result["URL"])))
    logger.info("num of ip in llm result:{}".format(len(llm_result["IP"])))
    logger.info("num of url in llm result:{}".format(len(llm_result["URL"])))
    
    # miss case
    logger.info("-"*80)
    miss_case_llm_human = get_miss_case(llm_result, human_result)
    save_json_file(
        miss_case_llm_human,
        os.path.join(config.save_dir, "miss_case_llm_human.json"),
    )
    logger.info(
        "miss case between llm and human:{},{}".format(
            len(miss_case_llm_human["IP"]), len(miss_case_llm_human["URL"])
        )
    )
    miss_case_llm_re = get_miss_case(llm_result, re_result)
    save_json_file(
        miss_case_llm_re, os.path.join(config.save_dir, "miss_case_llm_re.json")
    )
    logger.info(
        "miss case between llm and re:{},{}".format(
            len(miss_case_llm_re["IP"]), len(miss_case_llm_re["URL"])
        )
    )
    

    miss_case_re_human = get_miss_case(re_result, human_result)
    save_json_file(
        miss_case_re_human, os.path.join(config.save_dir, "miss_case_re_human.json")
    )
    logger.info(
        "miss case between re and human:{},{}".format(
            len(miss_case_re_human["IP"]), len(miss_case_re_human["URL"])
        )
    )
    logger.info("-"*80)
    # pure llm result

    logger.info("exchange missed classify url and ip for result of llm to get pure llm result")
    pure_llm_result = pure_llm(llm_result, human_result)
    save_json_file(
        pure_llm_result, os.path.join(config.save_dir, "pure_llm_result.json")
    )

    logger.info(
        "num of ip in pure_llm_result:{}".format(len(pure_llm_result["IP"]))
    )
    logger.info(
        "num of url in pure_llm_result:{}".format(len(pure_llm_result["URL"]))
    )
    logger.info("-"*80)
    # miss case for pure llm
    miss_case_pure_llm_human = get_miss_case(pure_llm_result, human_result)
    save_json_file(
        miss_case_pure_llm_human,
        os.path.join(config.save_dir, "miss_case_pure_llm_human.json"),
    )
    logger.info(
        "miss case between pure_llm and human:{},{}".format(
            len(miss_case_pure_llm_human["IP"]),
            len(miss_case_pure_llm_human["URL"]),
        )
    )
    miss_case_pure_llm_re = get_miss_case(pure_llm_result, re_result)
    save_json_file(
        miss_case_pure_llm_re,
        os.path.join(config.save_dir, "miss_case_pure_llm_re.json"),
    )
    logger.info(
        "miss case between pure_llm and re:{},{}".format(
            len(miss_case_pure_llm_re["IP"]), len(miss_case_pure_llm_re["URL"])
        )
    )


    miss_case_re_human = get_miss_case(re_result, human_result)
    save_json_file(
        miss_case_re_human, os.path.join(config.save_dir, "miss_case_re_human.json")
    )
    logger.info(
        "miss case between re and human: {},{}".format(
            len(miss_case_re_human["IP"]), len(miss_case_re_human["URL"])
        )
    )

    logger.info("-"*80)
    # bad case
    bad_case_llm_human = get_bad_case(llm_result, human_result)
    save_json_file(
        bad_case_llm_human, os.path.join(config.save_dir, "bad_case_llm_human.json")
    )
    logger.info(
        "bad case between llm and human:{},{}".format(
            len(bad_case_llm_human["IP"]), len(bad_case_llm_human["URL"])
        )
    )

    bad_case_pure_llm_human = get_bad_case(pure_llm_result, human_result)
    save_json_file(
        bad_case_pure_llm_human,
        os.path.join(config.save_dir, "bad_case_pure_llm_human.json"),
    )
    logger.info(
        "bad case between pure_llm and human:{},{}".format(
            len(bad_case_pure_llm_human["IP"]), len(bad_case_pure_llm_human["URL"])
        )
    )
    logger.info("-"*80)
    # recall and precision of llm and pure_llm

    logger.info("recall of llm{}".format(recall_llm(llm_result, human_result)))
    logger.info(
        "recall of pure_llm{}".format(recall_llm(pure_llm_result, human_result))
    )
    logger.info("recall of re{}".format(recall_llm(re_result, human_result)))

    logger.info(
        "precision of llm{}".format(precision_llm(llm_result, human_result))
    )
    logger.info(
        "precision of pure_llm{}".format(
            precision_llm(pure_llm_result, human_result)
        )
    )
    logger.info("precision of re{}".format(precision_llm(re_result, human_result)))
    
    
if __name__ == "__main__":
    save_dir = "result/re_results"
    text_re = read_log_file("data/Linux.txt")
    re_result = extract_re(text_re, save_dir)

    with open("result/result_2024-08-20_09-58-22/merged_output.json", "r") as f:
        predict_result = json.load(f)

