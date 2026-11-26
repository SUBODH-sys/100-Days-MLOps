import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)


def clarify_bug(description: str) -> str:
    prompt = (
        "Rewrite the following informal developer bug report into a clear, "
        "structured, and professional issue summary (including a concise title, "
        "summary, and reproduction/investigation notes based on the report):\n\n"
        f"{description}"
    )

    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=200,
        temperature=0.0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    bug_report = "App keeps crashing when I click save."
    response = clarify_bug(bug_report)
    print(response)
