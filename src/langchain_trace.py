# highlight-next-line
import weave
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()


weave.init("jurassic-park")


@weave.op()
def generate_answer(question: str) -> str:
    model = init_chat_model(model="openai:gpt-5-nano", reasoning_effort="low")
    answer = model.invoke(
        [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=question),
        ],
    )

    reflection = model.invoke(
        [
            SystemMessage(content="回答が正しいかチェックしてください"),
            HumanMessage(content=f"回答: {answer}\n質問: {question}"),
        ],
    )

    return answer.content


question = "日本の首都は？"
answer = generate_answer(question)
print(answer)
