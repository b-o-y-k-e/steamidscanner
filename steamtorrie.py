from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import random
import string


CHARACTERS = string.ascii_lowercase + string.digits + "-_"


def random_id():
	return "".join(random.choice(CHARACTERS) for _ in range(3))


def main():
	try:
		while True:
			user_input = random_id()
			url = f"https://steamcommunity.com/id/{user_input}/ajaxaliases"
			request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

			try:
				with urlopen(request, timeout=15) as response:
					page = response.read().decode("utf-8", errors="replace")
			except (HTTPError, URLError, TimeoutError) as error:
				print(f"{user_input}: request failed: {error}")
				continue

			if "<title>Steam Community :: Error</title>" in page:
				print(f"{user_input}: error page")
				with open("id.txt", "a", encoding="utf-8") as id_file:
					id_file.write(f"{user_input}\n")
			else:
				print(f"{user_input}: no error page")
	except KeyboardInterrupt:
		print("\nStopped.")


if __name__ == "__main__":
	main()
