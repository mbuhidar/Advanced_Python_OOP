from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from roommates_bill import house

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        form_amount = float(billform.amount.data)
        form_period = billform.period.data
        form_name1 = billform.name1.data
        form_days_in_house1 = float(billform.days_in_house1.data)
        form_name2 = billform.name2.data
        form_days_in_house2 = float(billform.days_in_house2.data)

        the_bill = house.Bill(form_amount, form_period)
        roommate1 = house.Roommate(form_name1, form_days_in_house1)
        roommate2 = house.Roommate(form_name2, form_days_in_house2)

        return render_template('results.html',
                                name1=roommate1.name,
                                amount1=roommate1.pays(the_bill, roommate2),
                                name2=roommate2.name,
                                amount2=roommate2.pays(the_bill, roommate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="September 2022")

    name1 = StringField("Name: ", default="Pam")
    days_in_house1 = StringField("Days in the house: ", default="10")

    name2 = StringField("Name: ", default="Mike")
    days_in_house2 = StringField("Days in the house: ", default="30")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
