import logging
import csv
import requests


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s:%(lineno)s %(message)s",
)


CSV_HEADERS: str = ["First Name", "Last Name", "Email"]
WEBEX_BASE_URL: str = "https://webexapis.com/v1/meetings?from=2024-09-12T00%3A00%3A00Z&to=2024-10-28T00%3A00%3A00Z&hostEmail=selbyt2%40nychhc.org"
WEBEX_API_HEADERS = {"Authorization":"Bearer ZTdlM2U1MjEtOWJjYi00NWY2LWExMjctNDZlNGM2MmE3YmExOWU4MWY4N2QtMzhj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"}


def main() -> None:

    with open(OUTPUT_FILE, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(CSV_HEADERS)

        with open(INPUT_FILE) as f:
            for line in f:
                print(line)
                url: str = WEBEX_BASE_URL
                print (url)
                response = requests.get(url, headers=WEBEX_API_HEADERS, timeout=5).json()
                print(response)             




if __name__ == "__main__":