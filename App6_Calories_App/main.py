from calorie import Calorie
from flask import Flask, render_template, request
from flask.views import MethodView
from temperature import Temperature
from wtforms import Form, StringField, SubmitField

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template(
            "calories_form_page.html", caloriesform=calories_form
        )


class ResultsPage(MethodView):
    def post(self):
        caloriesform = CaloriesForm(request.form)

        form_weight = float(caloriesform.weight.data)
        form_height = float(caloriesform.height.data)
        form_age = int(caloriesform.age.data)

        form_city = caloriesform.city.data
        form_country = caloriesform.country.data

        temperature = Temperature(form_country, form_city).get()
        calories = Calorie(
            form_weight, form_height, form_age, temperature=temperature
        )

        return render_template(
            "results.html", calories=int(calories.calculate())
        )


class CaloriesForm(Form):
    weight = StringField("Weight: ", default="70")
    height = StringField("Height: ", default="175")
    age = StringField("Age: ", default="32")

    city = StringField("City: ", default="Rome")
    country = StringField("Country: ", default="Italy")

    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule(
    "/calories_form", view_func=CaloriesFormPage.as_view("calories_form_page")
)
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))

app.run(debug=True)
