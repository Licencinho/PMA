from flask import *
from flask_ngrok import run_with_ngrok
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import *
from wtforms import validators
from wtforms.validators import *
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-impossible-impopossible' # this should go in a .env file

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

app_data = {
    "name":         "Plannerd",
    "description":  "A basic Flask app for students to plan their dissertations",
    "author":       "Alonso Olate, adaptation from Peter Simeth's flask template",
    "html_title":   "Plannerd",
    "project_name": "Plannerd",
    "keywords":     "flask, webapp, dissertation, planning, python, plannerd"
}

#Class for the form used in the login
class LoginForm(FlaskForm):
	email = EmailField('Email:', validators=[DataRequired()])
	password = PasswordField('Password:', validators =[DataRequired()])

#Class for the form for creating new modules
class ModuleForm(FlaskForm):
	module = StringField('Module Name:', validators=[DataRequired()])

#Class for the form that calculates the workload of the student. The biggest form can hold up to 20 modules.
class WorkloadForm(FlaskForm):
	hours_in_dissertation = IntegerField('How many hours have you worked in your dissertation so far?', validators=[NumberRange(min=0, max=900, message='Please put a number between 0 and 900')], default=0)
	module_1_boolean = BooleanField('Module 1')
	module_2_boolean = BooleanField('Module 2')
	module_3_boolean = BooleanField('Module 3')
	module_4_boolean = BooleanField('Module 4')
	module_5_boolean = BooleanField('Module 5')
	module_6_boolean = BooleanField('Module 6')
	module_7_boolean = BooleanField('Module 7')
	module_8_boolean = BooleanField('Module 8')
	module_9_boolean = BooleanField('Module 9')
	module_10_boolean = BooleanField('Module 10')
	module_11_boolean = BooleanField('Module 11')
	module_12_boolean = BooleanField('Module 12')
	module_13_boolean = BooleanField('Module 13')
	module_14_boolean = BooleanField('Module 14')
	module_15_boolean = BooleanField('Module 15')
	module_16_boolean = BooleanField('Module 16')
	module_17_boolean = BooleanField('Module 17')
	module_18_boolean = BooleanField('Module 18')
	module_19_boolean = BooleanField('Module 19')
	module_20_boolean = BooleanField('Module 20')
	module_1_PMA_percentage = IntegerField('Module 1', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_2_PMA_percentage = IntegerField('Module 2', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_3_PMA_percentage = IntegerField('Module 3', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_4_PMA_percentage = IntegerField('Module 4', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_5_PMA_percentage = IntegerField('Module 5', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_6_PMA_percentage = IntegerField('Module 6', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_7_PMA_percentage = IntegerField('Module 7', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_8_PMA_percentage = IntegerField('Module 8', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_9_PMA_percentage = IntegerField('Module 9', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_10_PMA_percentage = IntegerField('Module 10', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_11_PMA_percentage = IntegerField('Module 11', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_12_PMA_percentage = IntegerField('Module 12', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_13_PMA_percentage = IntegerField('Module 13', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_14_PMA_percentage = IntegerField('Module 14', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_15_PMA_percentage = IntegerField('Module 15', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_16_PMA_percentage = IntegerField('Module 16', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_17_PMA_percentage = IntegerField('Module 17', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_18_PMA_percentage = IntegerField('Module 18', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_19_PMA_percentage = IntegerField('Module 19', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)
	module_20_PMA_percentage = IntegerField('Module 20', validators=[NumberRange(min=0, max=100, message='Please put a number between 0 and 100')], default=0)

#Definition for the first page. It's a login page.
@app.route('/')
def index():
	login_message = ""
	form = LoginForm()
	df = pd.read_csv("users.csv")
	return render_template('login.html', df=df, form = form, login_message = login_message, app_data=app_data)

#Definition of the home after login
@app.route('/home')
def home():
	return render_template('index.html', app_data=app_data)

#Definition for what happens when a user inputs an email and a password in the login page.
@app.route('/login', methods=('GET', 'POST'))
def login():
	login_message = ""
	form = LoginForm()
	df = pd.read_csv("users.csv")
	if request.method == "POST":
		if form.validate_on_submit():

			# Search in Pandas adapted from https://www.interviewqs.com/ddi-code-snippets/rows-cols-python.
			
			dfFound = df.loc[(df['email'] == request.form.get("email")) & (df['password'] == request.form.get("password"))]
			
			#If dfFound has one row or more, it means we found a user with matching email and password
			count_row = dfFound.shape[0]
			if count_row > 0:
				return render_template('index.html', app_data=app_data)

	login_message = "Your credentials are not correct. Please try again"
	return render_template('login.html', df=df, form=form, login_message = login_message, app_data=app_data)

#Definition of the modules page, where users can see their current modules and create new ones.
@app.route('/modules')
def modules():
	df = pd.read_csv("modules.csv")
	form = ModuleForm()
	return render_template('modules.html', df=df, form = form, app_data=app_data)

#Definition of what happens when a user creates a new module
@app.route('/create', methods=('GET', 'POST'))
def create():
	form = ModuleForm()
	df = pd.read_csv("modules.csv")
	module_limit_message = ""
	if request.method == "POST":
		if form.validate_on_submit():
			if df.shape[0] < 20:
				max_id = df['ID'].max()
				new_id = max_id + 1
				new_df = pd.DataFrame({'ID':[new_id], 
					'module':[request.form.get("module")]
				})
				df = pd.concat([df, new_df], ignore_index=True)
				df.to_csv("modules.csv", index=False)
			
				return render_template('modules.html', df=df, form = form, module_limit_message = module_limit_message, app_data=app_data)
			else:
				module_limit_message = "We are sorry. You can only have a maximum of 20 modules. Please contact support"

	return render_template('modules.html', df=df, form=form, module_limit_message = module_limit_message, app_data=app_data)

#Definition of the calendar page, where users can create and see their calendar with work distribution for the semester/year
@app.route('/calendar')
def calendar():
    return render_template('calendar.html', app_data=app_data)

#Definition of the workload page, where users can input how much time have they spend in modules and dissertation
@app.route('/workload')
def workload():
	df = pd.read_csv("modules.csv")
	form = WorkloadForm()
	return render_template('workload.html', form = form, df=df, app_data=app_data)

#Definition of the results page that shows how much time should the student work per day and per week to finish his/her dissertation
@app.route('/results')
def results():
    formResults = {}
    return render_template('results.html', formResults = formResults, app_data=app_data)

#Definition of what happens when the user fills the form in the Workload page and how the time allocation per day and week is calculated
@app.route('/submit', methods=('GET', 'POST'))
def submit():
	df = pd.read_csv("modules.csv")
	form = WorkloadForm()
	formResults = {}
	if request.method == "POST":
		if form.validate_on_submit():
			formResults['hours_in_dissertation'] = float(request.form.get("hours_in_dissertation"))

			# Calculate how many hours spent in class in modules. There has to be a more intelligent way to do this :S
			formResults['hours_in_modules'] = 0
			if(request.form.get("module_1_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_2_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_3_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40	
			if(request.form.get("module_4_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_5_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_6_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_7_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_8_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_9_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_10_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_11_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_12_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_13_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40	
			if(request.form.get("module_14_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_15_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_16_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_17_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_18_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_19_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			if(request.form.get("module_20_boolean")):
				formResults['hours_in_modules'] = float(formResults['hours_in_modules']) + 40
			
			# Calculate how many hours spent in PMA work. Just like the section before, there has to be a smarter way to do it

			# transform PMA percentages in floats
			try:
				PMA_1_percentage = float(request.form.get("module_1_PMA_percentage"))
			except:
				PMA_1_percentage = 0

			try:
				PMA_2_percentage = float(request.form.get("module_2_PMA_percentage"))
			except:
				PMA_2_percentage = 0

			try:
				PMA_3_percentage = float(request.form.get("module_3_PMA_percentage"))
			except:
				PMA_3_percentage = 0

			try:
				PMA_4_percentage = float(request.form.get("module_4_PMA_percentage"))
			except:
				PMA_4_percentage = 0

			try:
				PMA_5_percentage = float(request.form.get("module_5_PMA_percentage"))
			except:
				PMA_5_percentage = 0

			try:
				PMA_6_percentage = float(request.form.get("module_6_PMA_percentage"))
			except:
				PMA_6_percentage = 0

			try:
				PMA_7_percentage = float(request.form.get("module_7_PMA_percentage"))
			except:
				PMA_7_percentage = 0

			try:
				PMA_8_percentage = float(request.form.get("module_8_PMA_percentage"))
			except:
				PMA_8_percentage = 0

			try:
				PMA_9_percentage = float(request.form.get("module_9_PMA_percentage"))
			except:
				PMA_9_percentage = 0

			try:
				PMA_10_percentage = float(request.form.get("module_10_PMA_percentage"))
			except:
				PMA_10_percentage = 0

			try:
				PMA_11_percentage = float(request.form.get("module_11_PMA_percentage"))
			except:
				PMA_11_percentage = 0

			try:
				PMA_12_percentage = float(request.form.get("module_12_PMA_percentage"))
			except:
				PMA_12_percentage = 0

			try:
				PMA_13_percentage = float(request.form.get("module_13_PMA_percentage"))
			except:
				PMA_13_percentage = 0

			try:
				PMA_14_percentage = float(request.form.get("module_14_PMA_percentage"))
			except:
				PMA_14_percentage = 0

			try:
				PMA_15_percentage = float(request.form.get("module_15_PMA_percentage"))
			except:
				PMA_15_percentage = 0

			try:
				PMA_16_percentage = float(request.form.get("module_16_PMA_percentage"))
			except:
				PMA_16_percentage = 0

			try:
				PMA_17_percentage = float(request.form.get("module_17_PMA_percentage"))
			except:
				PMA_17_percentage = 0

			try:
				PMA_18_percentage = float(request.form.get("module_18_PMA_percentage"))
			except:
				PMA_18_percentage = 0

			try:
				PMA_19_percentage = float(request.form.get("module_19_PMA_percentage"))
			except:
				PMA_19_percentage = 0

			try:
				PMA_20_percentage = float(request.form.get("module_20_PMA_percentage"))
			except:
				PMA_20_percentage = 0

			formResults['hours_in_PMAs'] = round(PMA_1_percentage
				+ PMA_2_percentage
				+ PMA_3_percentage
				+ PMA_4_percentage
				+ PMA_5_percentage
				+ PMA_6_percentage
				+ PMA_7_percentage
				+ PMA_8_percentage
				+ PMA_9_percentage
				+ PMA_10_percentage
				+ PMA_11_percentage
				+ PMA_12_percentage
				+ PMA_13_percentage
				+ PMA_14_percentage
				+ PMA_15_percentage
				+ PMA_16_percentage
				+ PMA_17_percentage
				+ PMA_18_percentage
				+ PMA_19_percentage
				+ PMA_20_percentage * 0.6, 0)

			# Number of modules
			formResults['number_of_modules'] = float(df.shape[0])

			# Calculate how many hours spent in modules and PMA work
			formResults['hours_in_modules_and_PMAs'] = round(float(formResults['hours_in_modules']) + float(formResults['hours_in_PMAs']), 0)

			# Calculate how many hours to do in modules
			formResults['module_hours_to_do'] = round(float(df.shape[0])*100 - float(formResults ['hours_in_modules_and_PMAs']), 0)

			# Calculate how many hours to do in dissertation
			formResults['dissertation_hours_to_do'] =  round(900 - float(request.form.get("hours_in_dissertation")), 0)

			# Calculate total work hours to do
			formResults['total_hours_to_do'] =  round(float(formResults['module_hours_to_do']) + float(formResults['dissertation_hours_to_do']), 0)

			# Calculate weeks remaining to submission
			submissionDate = datetime.datetime(2022,9,6)
			today = datetime.datetime.now()
			difference = submissionDate - today
			formResults['weeks_to_submission'] = round(difference.days/7, 1)

			# Calculate hours per week to work from now
			formResults['hours_per_week'] = round(float(formResults['total_hours_to_do'])/float(formResults['weeks_to_submission']), 1)

			# Calculate hours per day in a 7 day week
			formResults['hours_per_day_in_7_day_week'] = round(float(formResults['hours_per_week'])/7, 1)
			# Calculate hours per day in a 6 day week
			formResults['hours_per_day_in_6_day_week'] = round(float(formResults['hours_per_week'])/6, 1)
			# Calculate hours per day in a 5 day week
			formResults['hours_per_day_in_5_day_week'] = round(float(formResults['hours_per_week'])/5, 1)

			return render_template('results.html', formResults=formResults, app_data=app_data)

	return render_template('workload.html', form=form, df = df, app_data=app_data)
	
#Run the page
run_with_ngrok(app)
app.run()