# app/utils.py

import random

def split_narrative(narrative):
    """
    Splits the narrative into sentences for processing.
    Args:
        narrative (str): The complete narrative text.
    Returns:
        list: A list of sentences.
    """
    return [sentence.strip() for sentence in narrative.split('.') if sentence]

def get_random_sentence(sentences):
    """
    Returns a random sentence from a list of sentences.
    Args:
        sentences (list): List of sentences.
    Returns:
        str: A randomly selected sentence.
    """
    return random.choice(sentences) if sentences else ''

def generate_next_part(narrative):
    """
    Generates the next part of the story based on the existing narrative.
    Args:
        narrative (str): The existing narrative text.
    Returns:
        str: The next part of the story.
    """
    sentences = split_narrative(narrative)
    return get_random_sentence(sentences)

def validate_story_data(data):
    """
    Validates the data for creating a new story.
    Args:
        data (dict): A dictionary containing story data.
    Returns:
        bool: True if data is valid, False otherwise.
    """
    required_fields = ['title', 'genre', 'narrative']
    return all(field in data and data[field] for field in required_fields)

def format_response(message, data=None):
    """
    Formats a response for API calls.
    Args:
        message (str): The message to include in the response.
        data (dict, optional): Additional data to include in the response.
    Returns:
        dict: A formatted response dictionary.
    """
    response = {'message': message}
    if data:
        response['data'] = data
    return response
