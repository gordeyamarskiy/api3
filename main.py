from dotenv import load_dotenv
import requests
import os
from urllib.parse import urlparse
import argparse

def shorten_link(token, long_link):    

    url = os.environ["URL"]

    headers = {"Authorization": f"Bearer {token}"}
    params = {"v": 5.199, "url": long_link}
    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    return response.json()["response"]["short_url"]


def count_clics(token, short_link):
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    params = {
        "v": 5.199,
        "interval": "forever",
        "key": short_link,
        "extended": 0
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    statistic = response.json()["response"]["stats"]
    if statistic:
        count = response.json()["response"]["stats"][0]["views"] or 0
    return count


def main():
    load_dotenv()
    vk_token = os.environ["VK_TOKEN"]
    parser = argparse.ArgumentParser(description='Эта программа позволяет сокращать ссылки, либо, если ссылка уже сокращена, то выводит количесто кликов по ней.')
    parser.add_argument('--url', type=str, help='Введите ссылку')
    args = parser.parse_args()
    try:
        parsed_url = urlparse(args.url)
        if parsed_url.netloc == "vk.cc":
            print(count_clics(vk_token, parsed_url.path[1:]))
        else:
            short_link = shorten_link(vk_token, args.url)
            print(short_link)

    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")

if __name__ == "__main__":
    main()
