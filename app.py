import os
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
app.config.from_object('settings.Config')
pages = FlatPages(app)
assets = Environment(app)

post_content = Bundle(
    'jquery.js',
    'bootstrap/js/bootstrap-affix.js',
    'custom.js',
    filters='jsmin',
    output='packed/post_content.js')

assets.register('post_content_js', post_content)

@app.route('/')
def index():
    return render_template('index.html', pages=pages._pages)

## MAIN ##
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)