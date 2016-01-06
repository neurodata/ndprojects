import requests
import base64

import config
import ndio.remote.OCP as OCP
oo = OCP()

tokens = oo.get_public_tokens()

protocol = "https"
base_url = "api.github.com"
repo_name = "openconnectome/ndprojects"
ref = "master"
contents_path = "repos/{}/contents".format(repo_name)

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
    return base64.b64decode(get_json(path)['content'])


def get_claims_for_token(token):
    return [i['name'] for i in get_json(token)
            if i['name'] not in config.IGNORE_FILES]