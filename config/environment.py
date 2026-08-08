import os

from dotenv import load_dotenv


load_dotenv(
    override=True
)


def get_base_url():

    return os.getenv(
        "BASE_URL"
    )


def get_username():

    return os.getenv(
        "USERNAME"
    )


def get_password():

    return os.getenv(
        "PASSWORD"
    )