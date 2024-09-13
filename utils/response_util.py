from http import HTTPStatus
from typing import List
import dashscope
dashscope.api_key="sk-14cf82dceac946d2bfe1e2d5334f96f0"

def call_with_prompt():
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_turbo,
        prompt=prompt_list
    )
    # 如果调用成功，则打印模型的输出
    if response.status_code == HTTPStatus.OK:
        print(response)
    # 如果调用失败，则打印出错误码与失败信息
    else:
        print(response.code)
        print(response.message)

class Demo(object):
    def __init__(self, engine):
        self.engine = engine


    def get_multiple_sample(self, prompt_list: List[str]):
        response = dashscope.Generation.call(
            model=self.engine,
            prompt=prompt_list,
        )

        # print(response)
        return response


def run(prompt_list):
    demo = Demo(
        engine=dashscope.Generation.Models.qwen_turbo, 

    )
    response = demo.get_multiple_sample(prompt_list)
    print(response.output.text)
    # for i in response:
    #     print(i)


if __name__ == '__main__':
    prompt_list = 'this is a test'
    run(prompt_list)
















