import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def get_wikipedia_page():
    while True:
        title = input("Enter page title: ")
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, autosuggest=False)
            print(f"\n{page.title}")
            print(page.summary[:500] + "...")
            print(page.url)

        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_wikipedia_page()
