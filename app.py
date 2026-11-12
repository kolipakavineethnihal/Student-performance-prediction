from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

class StudentPerformanceApp:

    def __init__(self):
        self.app = Flask(__name__)

        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)

        self.app.add_url_rule(
            '/', 'home', self.home, methods=['GET']
        )

        self.app.add_url_rule(
            '/predict', 'predict', self.predict, methods=['POST']
        )

    def home(self):
        return render_template(
            'index.html',
            prediction=None,
            error=None
        )

    def predict(self):
        try:
            hours = float(request.form['hours_studied'])
            scores = float(request.form['previous_scores'])
            extracurricular = int(request.form['extracurricular'])
            sleep = float(request.form['sleep_hours'])
            papers = int(request.form['sample_papers'])

            data = pd.DataFrame([[
                hours, scores, extracurricular, sleep, papers
            ]], columns=[
                'Hours Studied',
                'Previous Scores',
                'Extracurricular Activities',
                'Sleep Hours',
                'Sample Question Papers Practiced'
            ])

            result = self.model.predict(data)[0]
            prediction = round(float(np.clip(result, 0, 100)), 2)

            return render_template(
                'index.html',
                prediction=prediction,
                error=None
            )

        except ValueError as e:
            return render_template(
                'index.html',
                prediction=None,
                error=str(e)
            )

        except Exception:
            return render_template(
                'index.html',
                prediction=None,
                error="Unable to generate prediction."
            )


student_app = StudentPerformanceApp()
app = student_app.app

if __name__ == '__main__':
    app.run(debug=True)