from flask import Flask, render_template, Blueprint


app = Flask(__name__)

# Your information
name = "Punit"
profession = "Software Engineer"
experience = "5+ years of experience"
education = "MCA from Bidar with a GPA of 6.8"
contact_number = "Your Contact Number"
profile_pic_url = "url_to_your_profile_pic"
resume_url = "url_to_your_resume"

@app.route('/')
def index():
    return render_template('index.html', name=name, profession=profession,
                           experience=experience, education=education,
                           contact_number=contact_number, profile_pic_url=profile_pic_url,
                           resume_url=resume_url)

@app.route('/about')
def about():
    return render_template('about.html', name=name, profession=profession)

@app.route('/experience')
def experience():
    return render_template('experience.html', experience=experience)

@app.route('/education')
def education():
    return render_template('education.html', education=education)

if __name__ == '__main__':
    app.run(debug=True)
