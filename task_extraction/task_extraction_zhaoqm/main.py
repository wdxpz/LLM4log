import os

from utils.arg_helper import parse_arguments, get_config
from utils.utiles import file_chunks, merge_new_json_files, merge_json_files, read_log_file
# from utils.re_extract import evaluate_result
from utils.eval_util_test import evaluate_result
from loguru import logger


from llms.claude import complete_claude
from llms.gemini import complete_gemini
from llms.llama import complete_llama
from llms.mistral import complete_mistral

from config.config import global_config

from prompt import (
    system_instruction,
    parameters,
    response_schema,
    context,
    safety_config,
)


def main():

    # if using proxy, uncomment below lines and set proxy address
    # os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
    # os.environ['HTTPs_PROXY'] = 'http://127.0.0.1:10809'

    args = parse_arguments()
    config = global_config()

    PROJECT_ID = config.project.PROJECT_ID
    LOCATION = config.project.LOCATION
    MODEL_NAME = config.model.MODEL_ID

    logger.info("Starting the application")
    log_file = os.path.join(
        config.save_dir, f"log_{config.exp_time}_{config.run_id}.txt"
    )
    logger.add(log_file)
    logger.info(f"Log file created at: {log_file}")
    logger.info(f"experiment comment:{args.comment}")  
    RUN_ID = config.run_id
    logger.info(f"RUN_ID: {RUN_ID}")
    if not args.test:
        # todo
        logger.info("Running in inference mode")
        logger.info("-" * 80)
        
        logger.info(f"PROJECT_ID: {PROJECT_ID}")
        logger.info(f"LOCATION: {LOCATION}")
        logger.info(f"MODEL_NAME: {MODEL_NAME}")
        # model = vertexai_init(PROJECT_ID, LOCATION, MODEL_NAME, system_instruction)
        logger.info(f"system_instruction: {system_instruction}")
        logger.info(f"prompt: {context}")

        #split original file into chunks
        if config.inference.chunk_size:
            # chunks file into a list
            document = file_chunks(
                config.dataset.log_file, eval(config.inference.chunk_size)
            )  # 728 * 728
        else:
            document = [read_log_file(config.dataset.log_file)]
        #create output dir
        inference_dir = os.path.join(config.save_dir, "inference_output")
        os.makedirs(inference_dir, exist_ok=True)
        #do infer on each chunk
        for i, chunk in enumerate(document):
            save_path = os.path.join(inference_dir, f"output{i}.json")
            logger.info(f"process the {i}th chunk, save to {save_path}")

            complete(args.llm, context, chunk, save_path, response_schema)

        #merge all results
        if config.inference.chunk_size:
            if config.inference.count:
                merge_new_json_files(inference_dir, f"{inference_dir}/merged_output.json")
            else:
                merge_json_files(inference_dir, f"{inference_dir}/merged_output.json")
            config.test.llm_result_file = f"{inference_dir}/merged_output.json"
        else:
            config.test.llm_result_file = f"{inference_dir}/output0.json"

        #evaluate 
        evaluate_result(config)
    else:
        evaluate_result(config)

def complete(llm_option, prompt, document, output_filename, response_schema=None):
    contents=f"{prompt}, {document}"
    if llm_option == 'gemini':
        response = complete_gemini(contents, response_schema)
    elif llm_option == 'llama':
        response = complete_llama(contents)
    elif llm_option == 'claude':
        response = complete_claude(contents)
    elif llm_option == 'mistral':
        response = complete_mistral(contents)
    else:
        raise Exception(f"wrong LLM model {llm_option} input!")
    
    write_response(response.text, output_filename)

def write_response(response, filename):
    """write response to file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response)
    logger.info(f"Generated response in {filename}")



if __name__ == "__main__":
    main()
