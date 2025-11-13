from openai import OpenAI

from granpost.config import load_api_key
from granpost.schemas.caption_gen import Quote
from granpost.schemas.page_profile import PageProfile

client = OpenAI(api_key=load_api_key())


def generate_quote(profile: PageProfile) -> Quote:
    system_prompt = (
        "You are GranPost, an assistant that writes short, wholesome, Facebook-ready quotes "
        "for a small theme page. "
        "Use the provided page profile to match theme, audience, and core goal. "
        "Never include anything in the 'never_post' list. "
        "Return exactly one quote that could be used as a caption text."
    )

    profile_dict = profile.model_dump()

    user_prompt = (
        "Generate a single quote caption for this page.\n\n"
        "Page profile JSON:\n"
        f"{profile_dict}"
    )

    response = client.responses.parse(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        text_format=Quote,
    )

    print(response)
    return response.output_parsed


def main():
    profile = PageProfile(
        page_handle="@RememberWhen",
        theme="60s–90s nostalgia and throwbacks",
        timezone="America/Los_Angeles",
        never_post="politics, tragic news",
        core_goal="spark warm memories about childhood and family",
        content_focus="short nostalgic reflections and everyday moments",
        audience="adults 35+ who grew up in the 60s–90s",
    )
    quote = generate_quote(profile)
    print(quote.text)
    print(quote.hashtags)
    print(quote.alt_text)


if __name__ == "__main__":
    main()
