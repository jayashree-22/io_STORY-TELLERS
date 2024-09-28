function generateStory() {
    var storyId = document.querySelector('input[name="story_id"]').value;
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ story_id: storyId })
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector('#next-part').innerHTML = data.next_part;
    });
}