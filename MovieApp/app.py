# MoviePy App

# Imports for WebApp
from flask import *

# Imports for MoviePy
from moviepy.editor import *


app = Flask(__name__,template_folder='template',static_folder='static')


# Landing Page
@app.route('/', methods=['GET', 'POST'])
def landingpage():
    if request.method=="POST":
        
        f1 = request.files['vid1']  
        f1.save(f1.filename) 
        f2 = request.files['vid2']  
        f2.save(f2.filename) 

        vid1 = VideoFileClip(f1.filename)
        vid2 = VideoFileClip(f2.filename)

        clip=concatenate_videoclips([vid1,vid2],method='compose')
        clip.write_videofile("static/Edited.mp4")

        return render_template('index.html',name="Edited.mp4")

    return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = "xyz" 
    app.run(debug=True)
    