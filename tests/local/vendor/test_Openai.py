# poetry run pytest tests/local/vendor/test_Openai.py

from jipso.vendor.Openai import *
from jipso.Client import ClientOpenai

def test_compute_forward():
  compute_forward(client=ClientOpenai(), model='gpt-4o', messages=[{'role': 'user', 'content': 'Hello ChatGPT!'}])

# def test_handle_response(): pass
