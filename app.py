from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Replace these placeholders with your actual data
    data = {
        'name': "Punit",
        'profession': "Software Engineer",
        'experience': "5+ years of experience in Python, Django, Flask, FastAPI, Docker. Worked in startups, big MNCs like Walmart, and companies like Mirafra. Experience in building APIs, scalable applications, and working on MySQL, NoSQL databases.",
        'education': "Master of Computer Applications (MCA) with a CGPA of 6.8",
        'achievements': ["Achievement 1", "Achievement 2", "Achievement 3"]
    }
    return render_template('index.html', **data)

@app.route('/api/experience')
def experience_api():
    # Replace these placeholders with your actual data
    experience_data = [
        {
            'position': 'Senior Software Engineer',
            'company': 'Mirafra Technologies',
            'duration': 'Aug 2021 - Present',
            'responsibilities': [
                'Successfully developed projects such as TCRB, AARI, and Curesoftware, all of which have been instrumental in creating high-quality applications',
                'Successfully built a scalable and reliable system with Python that can handle 2K requests per second',
                'Build migration suite of tools with End-to-End Implementation of project CISCO client with Python',
                'Developed a dashboard for monitoring purposes using Python (Django, Postgres, RabbitMQ, Redis)',
                'Transformed a customer-specific tool to Generic, Multiple customers can get their estimations',
                'Analyzed customer needs and created a comprehensive design for new RESTful services and APIs using Flask',
                'Implemented common APIs based on architecture guidelines and frameworks such as Flask, Django, Express'
            ]
        },
        {
            'position': 'Software Engineer',
            'company': 'Walmart Labs',
            'duration': 'June 2019 - July 2020',
            'responsibilities': [
                'Developed a Flask-based microservice that integrated an existing React frontend, increasing efficiency by 25%',
                'Complete owner of the project, Backend, Frontend, and DevOps using Flask, React, and Jenkins',
                'Designed a system for stakeholders resulted in tagging a huge number of data sets using Flask as the Backend engine',
                'Successfully built a scalable and reliable backend service handling 20K requests per minute with 99.99% uptime',
                'Designed APIs which were further consumed by the stakeholders, resulting in a decrease of development time',
                'Involved in developing CI / CD pipeline for tools using Jenkins',
                'Led a design called Fuery Tagging that resulted in giving data scientists the correct search query',
                'Involved in designing of tables with MySQL, Docker'
            ]
        },
        {
            'position': 'Software Engineer',
            'company': 'Previous Company',
            'duration': 'June 2017 - June 2019',
            'responsibilities': [
                'Responsible for end-to-end designs for sending automated mail (SMTP)',
                'Worked on Python on Independent Scripts Designed a reporting System using worked independently on the Custom reports'
            ]
        }
        # Add more experiences as needed
    ]

    return jsonify(experience_data)


if __name__ == '__main__':
    app.run(debug=True)








