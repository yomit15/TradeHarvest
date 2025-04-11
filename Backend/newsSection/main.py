from flask import Flask, jsonify
from flask_cors import CORS
import feedparser
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/api/rss', methods=['GET'])
def get_news():
    # RSS feed URL
    feed_url = 'https://eng.ruralvoice.in/rss/latest-posts'
    
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)
    
    news_items = []
    
    # Loop through entries in the feed
    for entry in feed.entries:
        # Extract relevant information
        news_item = {
            'source': entry.source.title if 'source' in entry else 'Unknown',
            'title': entry.title,
            'link': entry.link,
            'published': entry.published if 'published' in entry else None,
            'image': None,  # Initialize image as None
            'description': None  # Initialize description as None
        }
        
        # Attempt to extract the image from media:content
        if 'media_content' in entry and len(entry.media_content) > 0:
            news_item['image'] = entry.media_content[0]['url']
        # Alternatively, check media:thumbnail
        elif 'media_thumbnail' in entry and len(entry.media_thumbnail) > 0:
            news_item['image'] = entry.media_thumbnail[0]['url']
        # Check if there's a description that contains an image (if applicable)
        elif 'description' in entry:
            # Use regex to extract the first <img> src if present in description
            img_search = re.search(r'<img.*?src=["\'](.*?)["\']', entry.description)
            if img_search:
                news_item['image'] = img_search.group(1)

            # Strip HTML tags from the description and limit its length
            clean_description = re.sub(r'<.*?>', '', entry.description)
            news_item['description'] = clean_description[:300] + '...'  # Shorten description to 300 chars

        news_items.append(news_item)
    
    return jsonify(news_items)

if __name__ == '__main__':
    app.run(debug=True)
