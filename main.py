import json
import cric_api

def show_menu():
        print("\n=====Cricket=====")
        print("1. General news")
        print("2. Upcoming matches")
        print("0. Exit")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("\n=== Series News ===")
            news = cric_api.cricket_news()
            print(news)
        elif choice == "2":
            print("\n=== Upcoming Matches News ===")
            upc1 = cric_api.Future_match()
            print(upc1)
        elif choice == "0":
            print("... Exiting ...")
            break
        else:
            print("Invalid choice. Try again.")
#try:
#   news = cric_api.cricket_news()
#   print(json.dumps(news, indent=3))
#except Exception as e:
#   print("Failed to fetch Cricbuzz data:", e)
if __name__ == "__main__":
    #cric_api.api_info_check()
    #cric_api.Future_match()  
    main()