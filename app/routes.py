from flask import Blueprint, request, jsonify
from app import app, db
from app.models import Story, Choice
from app.utils import random, generate_next_part, validate_story_data, format_response


story_blueprint = Blueprint('story', __name__)

@story_blueprint.route('/create', methods=['POST'])
def create_story():
    data = request.form
    if not validate_story_data(data):
        return jsonify(format_response('Invalid story data', data)), 400
    # Create a new story
    title = request.form['title']
    genre = request.form['genre']
    narrative = request.form['narrative']
    story = Story(title=title, genre=genre, narrative=narrative)
    db.session.add(story)
    db.session.commit()
    return jsonify({'message': 'Story created successfully'})

@story_blueprint.route('/add_choice', methods=['POST'])
def add_choice():
    # Add a new choice to a story
    story_id = request.form['story_id']
    text = request.form['text']
    choice = Choice(story_id=story_id, text=text)
    db.session.add(choice)
    db.session.commit()
    return jsonify({'message': 'Choice added successfully'})

@story_blueprint.route('/generate', methods=['POST'])
def generate_story():
    # Generate the next part of the story
    story_id = request.form['story_id']
    story = Story.query.get(story_id)
    # Use the Markov chain algorithm to generate the next part of the story
    next_part = generate_next_part(story.narrative)
    return jsonify({'next_part': next_part})

def generate_next_part(narrative):
    # Implement the Markov chain algorithm here
    # For simplicity, we'll just return a random sentence
    sentences = narrative.split('.')
    next_sentence = random.choice(sentences)
    return next_sentence