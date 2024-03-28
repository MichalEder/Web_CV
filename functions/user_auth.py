import yaml
import streamlit as st
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader


def load_config():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    return config

def get_authenticator(config):
    return stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )