from flask import Flask ,render_template,request,url_for
#from werkzeug import secure_filename
#from utils import Videos
import json
import os
from make_tensors import Return_Tensor
from keras.models import load_model
import pandas as pd


# using the config.json for predefined paths
#with open('config.json','r') as c :
#	params = json.load(c)['params']


#initialising the app
app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = params['upload_location']



@app.route('/', methods=['GET','POST'])
def index():

	activity=''

	if request.method == 'POST' :

		# Taking the link of the video from the form
		link = request.form['link']
		print('The link is : ',link) # Checking
		print('link type is :',type(link))   # Checking type

		# taking tensors 
		rt = Return_Tensor()
		activity = rt.give_me_tensor(link)

		# loading model
		#model = load_model('final_model.h5')

		# Making predictions
		#pred = model.predict_classes(tensors)

		#loadinng our target dataset
		#df = pd.read_csv('dataframe.csv')

		# Checking relative activity name to the array
		#activity_name = df[df['label_nums']==pred[0]]
		#activity= activity_name.labels.unique()[0]



		# Taking the video as Input 
		#a = request.files['video']

		# Initializing the class from the utils.py
		#video = Videos()

		# Taking out frames from video
		#frames = video._process_video(os.path.join(app.config['UPLOAD_FOLDER'],a.filename))
		#frames = video._process_video(a)

		# Taking out tensor from video
		#tensor = video.read_video(os.path.join(app.config['UPLOAD_FOLDER'],a.filename))
		#tensor = video.read_video(a)


		# Saving video to upload folder
		#a.save(os.path.join(app.config['UPLOAD_FOLDER'],a.filename))

	return render_template('index.html',answer=activity)

if __name__=='__main__':
	app.run(debug=True)