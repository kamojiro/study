import asyncio

from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama.chat_models import ChatOllama

from logging_config import logger

load_dotenv()

model = "deepseek-r1:8b"
# model = "deepseek-r1:14b"
llm = ChatOllama(
    model=model,
    temperature=0,
)


async def load_articles(url: str):
    loader = WebBaseLoader(url)
    docs = await asyncio.to_thread(loader.load)
    return docs


async def summarize(docs):
    document = "\n\n\n".join([doc.page_content for doc in docs])
    messages = [
        (
            "system",
            "あなたはドキュメントを要約するスペシャリストです。ドキュメントを要約して日本語で出力してください。",
        ),
        (
            "human",
            f"""【指示】
            以下の文章の内容を、必ず日本語のみで、簡潔かつ分かりやすく要約してください。回答は日本語のみで記述し、英語や中国語は一切使用しないでください。文章の要点を正確に捉え、重要な情報を漏らさずまとめるようにしてください。

            【文章】
            {document}

            【指示】
            文章を箇条書きで要約し、日本語で出力してください。回答のみを出力してください。
            """,
        ),
    ]
    ai_msg = await llm.ainvoke(messages)
    content = ai_msg.content
    try:
        _, result = content[len("<think>") :].split("</think>")
    except Exception as e:
        logger.warning(f"The following content was not processed: \n{content}")
        raise e
    return result


async def summarize_from_url(url):
    docs = await load_articles(url)
    summary = await summarize(docs)
    return summary


def main():
    url = "https://zenn.dev/aimasaou/articles/96182d46ae6ad2"
    docs = load_articles(url)
    summary = summarize(docs)
    print(summary)


if __name__ == "__main__":
    main()
