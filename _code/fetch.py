import requests
import base64
import json

import config
import ndio.remote.OCP as OCP
oo = OCP()

# Before running this, populate `config.py` with your own values.

protocol = "https"
base_url = "api.github.com"
repo_name = "openconnectome/ndprojects"
ref = "master"
contents_path = "repos/{}/contents".format(repo_name)

tokens = oo.get_public_tokens()


def get_json(path):
    """
    Return JSON for a path in the ndprojects repo.

    Arguments:
        path (str): The path (no leading slash) to inspect

    Returns:
        JSON
    """

    url = "{}://{}/{}/{}/?ref={}".format(
        protocol,
        base_url,
        contents_path,
        path,
        ref
    )

    r = requests.get(url, auth=(config.USERNAME, config.AUTH))
    if r.status_code >= 400:
        raise ValueError('{}: No data found at {}'.format(r.status_code, url))
    else:
        return r.json()


def get_file_contents(path):
    """
    Gets the contents of a file specified by 'path'.

    Arguments:
        path (str): The path (no leading /) to the file

    Returns:
        str: The contents of the file.
    """
    return base64.b64decode(get_json(path)['content'])


def get_claims_for_token(token):
    """
    Gets an array of ipy notebooks, each with their own claim, that live inside
    the directory named after their project's token.

    Arguments:
        token (str): The token to inspect

    Returns:
        str[]: A list of filenames, each representing a claim
    """
    return [i['name'] for i in get_json(token)
            if i['name'] not in config.IGNORE_FILES]


def get_claim_and_result_tuple(token, claimfile):
    """
    Gets the claim and the result of the notebook (the last text-line).

    Arguments:
        token (str): The token to inspect
        claimfile (str): The name of the file (including ext) to read

    Returns:
        (str, str): The claim and its result, in string form.
    """
    cells = json.loads(get_file_contents(token + "/" + claimfile))['cells']

    return (
        cells[0]['source'][0],
        cells[-1]['outputs'][0]['text'][0]
    )
