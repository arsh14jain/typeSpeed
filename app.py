from flask import Flask,render_template,request
import random

app = Flask(__name__)

List = ["Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO or FILO. There are many real-life examples of a stack. Consider an example of plates stacked over one another in the canteen.", "In computer science, a queue is a collection of entities that are maintained in a sequence and can be modified by the addition of entities at one end of the sequence and the removal of entities from the other end of the sequence.", "A linked list is a linear collection of data elements, whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence"]

@app.route('/check',methods=['POST'])
def calculate():
	written_text = request.form["txt-box"]
	time1=request.form['sw-t']
	expected_text = request.form['sw-t1']
	# print(written_text)
	# print("Time is")
	# print(time1)
	# # print(type(time1))
	time1=float(time1)
	time1=time1/60
	# print(type(time1))
	num_chars=len(written_text)
	net_word=num_chars/5
	speed=net_word/time1
	# print(num_chars)
	# print(net_word)
	# print(speed)
	sp = speed
	speed = str(speed)
	expected_res = expected_text.split()
	written_res = written_text.split()
	numExp = len(expected_res)
	numWri = len(written_res)
	d_expected = dict()
	d_written = dict()
	for word in expected_res:
		word=word.strip()
		# word=word.translate(word.maketrans("", "", string.punctuation)) 
		if word in d_expected:
			d_expected[word]=d_expected[word]+1
		else:
			d_expected[word]=1
	for word in written_res:
		word=word.strip()
		# word=word.translate(line.maketrans("", "", string.punctuation)) 
		if word in d_written:
			d_written[word]=d_written[word]+1
		else:
			d_written[word]=1
	errors=0
	e=0
	for key in list(d_expected.keys()):
		if key in d_written:
			e = abs(d_expected[key] - d_written[key])
			errors = errors + e
		else:
			e = d_expected[key]
			errors = errors + e
	
	print(errors)
	# print(expected_res)
	# print(errors)
	net_words = numExp - errors
	net_speed = net_words/time1
	accuracy = (net_words/net_word) * 100
	sp=float("{:.2f}".format(sp))
	net_speed=float("{:.2f}".format(net_speed))
	accuracy = float("{:.2f}".format(accuracy))
	# print(net_speed)
	speednet = [net_speed,errors,sp,accuracy]
	return render_template('result.html',speednet=speednet)

@app.route('/',methods=['POST','GET'])
def index():
	n=random.choice([0,1,2])
	sample_text=List[n]
	return render_template('ind.html',sample_text=sample_text)

@app.route('/about')
def aboutPage():
	return render_template('aboutUs.html')

@app.route('/developers')
def developersPage():
	return render_template('developers.html')	

if __name__ == "__main__":
	app.run(debug=True)