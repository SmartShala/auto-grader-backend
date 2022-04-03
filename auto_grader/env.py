import json
import os


def get_credentials():
    creds = {}
    if "env" in os.environ:
        creds['debug'] = os.environ['debug']
        creds['allowed_hosts'] = os.environ['allowed_hosts']
        creds['django_secret_key'] = os.environ['django_secret_key']
        creds['db_password'] = os.environ['db_password']
        creds['db_name'] = os.environ['db_name']
        creds['db_user'] = os.environ['db_user']
        creds['db_host'] = os.environ['db_host']
        creds['cors_origin_whitelist'] = os.environ['cors_origin_whitelist']
    else:
        env_file_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(env_file_dir, '.env.json'), 'r') as f:
            creds = json.loads(f.read())
    return creds


credentials = get_credentials()
