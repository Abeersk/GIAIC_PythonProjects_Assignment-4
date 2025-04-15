print("00_joke_bot")

prompt: str = "what do you want?"
joke: str = "Why did the scarecrow win an award? \nBecause he was outstanding in his field! 😆"
sorry: str = "Sorry, I tell only jokes."

def main():
    user_input = input(prompt).strip().lower()

    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)

if __name__ == '__main__':
    main()
