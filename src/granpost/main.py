import json
from pathlib import Path

from granpost.generator import generate_quote
from granpost.schemas.page_profile import PageProfile

# --- Paths ---
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_OUT = REPO_ROOT / "data" / "output"
PROFILES_FILE = DATA_OUT / "profiles.json"
QUOTES_FILE = DATA_OUT / "quotes.json"


def load_profiles(path: Path) -> list[PageProfile]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [PageProfile(**item) for item in data]


def choose_profile(profiles: list[PageProfile]) -> PageProfile:
    print("Choose a profile:\n")

    for idx, profile in enumerate(profiles):
        print(f"{idx + 1}: {profile.page_handle}\n")

    while True:
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 0 < choice <= len(profiles):
            return profiles[choice - 1]
        else:
            print("Invalid choice. Please try again.")


def main() -> None:
    profiles = load_profiles(PROFILES_FILE)
    if not profiles:
        print("No profiles found. Exiting.")
        return

    profile = choose_profile(profiles)
    while True:
        print(
            f"Current profile: {profile.page_handle}\n\n"
            f"Actions: \n"
            f"1. Generate a quote\n"
            f"2. Go back\n"
            f"3. Exit\n"
        )

        if (choice := input("Enter an action: ")) == "1":
            print("\nGenerating quote...\n")
            try:
                quote = generate_quote(profile)
            except Exception as e:
                print(f"Error: {e}")
                continue

            print(f"Quote: {quote.text}")
            print(f"Hashtags: {', '.join('#' + tag for tag in quote.hashtags)}")
            print(f"Alt-text: {quote.alt_text}\n")

        elif choice == "2":
            profile = choose_profile(profiles)
            continue

        elif choice == "3":
            print("\nExiting.")
            return

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
