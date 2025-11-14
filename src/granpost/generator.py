from openai import OpenAI

from granpost.config import load_api_key
from granpost.schemas.caption_gen import Quote
from granpost.schemas.page_profile import PageProfile

client = OpenAI(api_key=load_api_key())


def generate_quote(profile: PageProfile) -> Quote:
    system_prompt = """
        You are GranPost, an assistant that writes short, relatable social media quotes
        for small themed pages.
        
        Follow these global rules:
        - Always respect 'never_post' topics.
        - Match the page's audience and core goal from its profile.
        - Write quotes that feel like a single real person posting.
        - Avoid generic cliches and overused inspirational phrases.
        """.strip()

    # Load PageProfile JSON
    profile_dict = profile.model_dump()

    user_prompt = (
        "Generate a single quote for this page.\n\n" "Page profile JSON:\n" f"{profile_dict}"
    )

    response = client.responses.parse(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        text_format=Quote,
    )

    return response.output_parsed
