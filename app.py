from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os
import datetime

app = Flask(__name__)

# --------------------------
# QR Code Generation Section
# --------------------------
qr_code_link = "http://127.0.0.1:5000/register"  # Change if deployed online
qr = qrcode.make(qr_code_link)
if not os.path.exists("static"):
    os.makedirs("static")
qr.save("static/qrcode.png")

# --------------------------
# Student Data and Fee Details
# --------------------------
# All register numbers are stored as strings.
students = {
      "922122104001": {
        "name": "Abichellam S",
        "register_number": "922122104001",
        "password": "922122104001",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 19500,
        "Tuition Fee": 39000,
        "University Fee": 21000,
        "photo": "Abichellam.png"
    },
    "922122104002": {
        "name": "Abinayasri N",
        "register_number": "922122104002",
        "password": "922122104002",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 17500,
        "Tuition Fee": 28000,
        "University Fee": 24000,
        "photo": "Abinayasri.png"
    },
    "922122104003": {
        "name": "Abirami K",
        "register_number": "922122104003",
        "password": "922122104003",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 13000,
        "Tuition Fee": 33000,
        "University Fee": 18000,
        "photo": "Abirami.png"
    },
    "922122104004": {
        "name": "Atchayadharshan J",
        "register_number": "922122104004",
        "password": "922122104004",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9100,
        "Tuition Fee": 38000,
        "University Fee": 23000,
        "photo": "Atchayadharshan.png"
    },
    "922122104005": {
        "name": "Balavishnu J",
        "register_number": "922122104005",
        "password": "922122104005",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 17000,
        "Tuition Fee": 35000,
        "University Fee": 21000,
        "photo": "Balavishnu.png"
    },
    "922122104006": {
        "name": "Bhuvaneswari M",
        "register_number": "922122104006",
        "password": "922122104006",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 1400,
        "Tuition Fee": 27000,
        "University Fee": 20000,
        "photo": "Bhuvaneswari.png"
    },
    "922122104007": {
        "name": "Dhanalakshmi D",
        "register_number": "922122104007",
        "password": "922122104007",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 17500,
        "Tuition Fee": 52000,
        "University Fee": 16000,
        "photo": "Dhanalakshmi.png"
    },
    "922122104008": {
        "name": "Dhivyashree M",
        "register_number": "922122104008",
        "password": "922122104008",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 14500,
        "Tuition Fee": 30000,
        "University Fee": 13500,
        "photo": "Dhivyashree.png"
    },
    "922122104009": {
        "name": "Divya Dharshini J",
        "register_number": "922122104009",
        "password": "922122104009",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 8000,
        "Tuition Fee": 23500,
        "University Fee": 15000,
        "photo": "Divya Dharshini.png"
    },
    "922122104010": {
        "name": "Gokul Pandi P",
        "register_number": "922122104010",
        "password": "922122104010",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 18000,
        "Tuition Fee": 40000,
        "University Fee": 11000,
        "photo": "Gokul Pandi.png"
    },
    "922122104011": {
        "name": "Gurumoorthi P",
        "register_number": "922122104011",
        "password": "922122104011",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 35000,
        "University Fee": 17500,
        "photo": "Gurumoorthi.png"
    },
        "922122104012": {
        "name": "Haarson T",
        "register_number": "922122104012",
        "password": "922122104012",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 16500,
        "Tuition Fee": 21000,
        "University Fee": 15500,
        "photo": "Haarson.png"
    },
    "922122104013": {
        "name": "Hariesh Kumaran B",
        "register_number": "922122104013",
        "password": "922122104013",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 35000,
        "University Fee": 15000,
        "photo": "Hariesh Kumaran.png"
    },
    "922122104014": {
        "name": "Harrishraj A J",
        "register_number": "922122104014",
        "password": "922122104014",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 16500,
        "Tuition Fee": 23500,
        "University Fee": 11000,
        "photo": "Harrishraj.png"
    },
    "922122104015": {
        "name": "Hirthick Kanna M",
        "register_number": "922122104015",
        "password": "922122104015",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 15000,
        "University Fee": 25000,
        "photo": "Hirthick Kanna.png"
    },
    "922122104016": {
        "name": "Hirthiha V",
        "register_number": "922122104016",
        "password": "922122104016",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 17000,
        "University Fee": 27000,
        "photo": "Hirthiha.png"
    },
    "922122104018": {
        "name": "Jeeva A",
        "register_number": "922122104018",
        "password": "922122104018",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 15000,
        "University Fee": 25000,
        "photo": "Jeeva.png"
    },
    "922122104019": {
        "name": "Jeevitha J",
        "register_number": "922122104019",
        "password": "922122104019",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 8500,
        "Tuition Fee": 32000,
        "University Fee": 12000,
        "photo": "Jeevitha.png"
    },
    "922122104020": {
        "name": "Jenat Caroline M",
        "register_number": "922122104020",
        "password": "922122104020",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9200,
        "Tuition Fee": 18000,
        "University Fee": 11000,
        "photo": "Jenat Caroline.png"
    },
    "922122104021": {
        "name": "Jeya Shri P",
        "register_number": "922122104021",
        "password": "922122104021",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 17000,
        "Tuition Fee": 42000,
        "University Fee": 27000,
        "photo": "Jeya Shri.png"
    },
    "922122104022": {
        "name": "Jeya Sree C",
        "register_number": "922122104022",
        "password": "922122104022",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 11000,
        "Tuition Fee": 35000,
        "University Fee": 15000,
        "photo": "Jeya Sree C.png"
    },
    "922122104023": {
        "name": "Jinu Mistika R",
        "register_number": "922122104023",
        "password": "922122104023",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 15000,
        "Tuition Fee": 29500,
        "University Fee": 14500,
        "photo": "Jinu Mistika.png"
    },
    "922122104024": {
        "name": "Kaleel Ahamed J",
        "register_number": "922122104024",
        "password": "922122104024",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 35000,
        "University Fee": 15000,
        "photo": "Kaleel Ahamed.png"
    },
    "922122104025": {
        "name": "Kanisha G",
        "register_number": "922122104025",
        "password": "922122104025",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 15000,
        "Tuition Fee": 29500,
        "University Fee": 14500,
        "photo": "Kanisha.png"
    },
    "922122104026": {
        "name": "Kiruba M",
        "register_number": "922122104026",
        "password": "922122104026",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 11500,
        "Tuition Fee": 22500,
        "University Fee": 18000,
        "photo": "Kiruba.png"
    },
    "922122104027": {
        "name": "Kowsika S",
        "register_number": "922122104027",
        "password": "922122104027",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 12500,
        "Tuition Fee": 19500,
        "University Fee": 29500,
        "photo": "Kowsika.png"
    },
    "922122104028": {
        "name": "Lakshana K",
        "register_number": "922122104028",
        "password": "922122104028",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 45500,
        "University Fee": 19800,
        "photo": "Lakshana.png"
    },
    "922122104029": {
        "name": "Mohamed Ismael J",
        "register_number": "922122104029",
        "password": "922122104029",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10500,
        "Tuition Fee": 45000,
        "University Fee": 20000,
        "photo": "Mohamed Ismael.png"
    },
    "922122104030": {
        "name": "Pavithra B",
        "register_number": "922122104030",
        "password": "922122104030",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 7500,
        "Tuition Fee": 21500,
        "University Fee": 18500,
        "photo": "Pavithra.png"
    },
    "922122104031": {
        "name": "Praveena B",
        "register_number": "922122104031",
        "password": "922122104031",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9000,
        "Tuition Fee": 41500,
        "University Fee": 14500,
        "photo": "Praveena.png"
    },
    "922122104032": {
        "name": "Pravin M",
        "register_number": "922122104032",
        "password": "922122104032",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 14500,
        "Tuition Fee": 31500,
        "University Fee": 22500,
        "photo": "Pravin.png"
    },
    "922122104033": {
        "name": "Pricilla Ruby S",
        "register_number": "922122104033",
        "password": "922122104033",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 16500,
        "Tuition Fee": 29500,
        "University Fee": 19500,
        "photo": "Pricilla Ruby.png"
    },
    "922122104034": {
        "name": "Priyanga Saleth Mary S",
        "register_number": "922122104034",
        "password": "922122104034",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 35000,
        "University Fee": 15000,
        "photo": "Priyanga Saleth Mary.png"
    },
    "922122104035": {
        "name": "Raja Pandi K",
        "register_number": "922122104035",
        "password": "922122104035",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 12500,
        "Tuition Fee": 27500,
        "University Fee": 12000,
        "photo": "Raja Pandi.png"
    },
    "922122104036": {
        "name": "Rakhzanaa R",
        "register_number": "922122104036",
        "password": "922122104036",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 8000,
        "Tuition Fee": 31500,
        "University Fee": 12000,
        "photo": ""
    },
    "922122104037": {
        "name": "Reshma S",
        "register_number": "922122104037",
        "password": "922122104037",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 20000,
        "University Fee": 10000,
        "photo": "Reshma.png"
    },
    "922122104038": {
        "name": "Rithikaa B",
        "register_number": "922122104038",
        "password": "922122104038",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 27000,
        "University Fee": 9000,
        "photo": "Rithikaa.png"
    },
    "922122104039": {
        "name": "Rohini M",
        "register_number": "922122104039",
        "password": "922122104039",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9000,
        "Tuition Fee": 31000,
        "University Fee": 12000,
        "photo": "Rohini.png"
    },
    "922122104040": {
        "name": "Sahithya Dharani J",
        "register_number": "922122104040",
        "password": "922122104040",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9000,
        "Tuition Fee": 22000,
        "University Fee": 17000,
        "photo": "Sahithya Dharani.png"
    },

    "922122104041": {
        "name": "Sai B",
        "register_number": "922122104041",
        "password": "922122104041",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9000,
        "Tuition Fee": 30000,
        "University Fee": 15000,
        "photo": "Sai.png"
    },
    "922122104042": {
        "name": "Saimica Infant X",
        "register_number": "922122104042",
        "password": "922122104042",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 25000,
        "University Fee": 12000,
        "photo": "Saimica Infant.png"
    },
    "922122104043": {
        "name": "Sakthi Hariharan V",
        "register_number": "922122104043",
        "password": "922122104043",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 70000,
        "University Fee": 25000,
        "photo": "Rohinif.png"
    },
    "922122104044": {
        "name": "Sakthi Varshini V",
        "register_number": "922122104044",
        "password": "922122104044",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 35000,
        "University Fee": 25000,
        "photo": "Sakthi Varshini.png"
    },
    "922122104045": {
        "name": "Sangeeth N",
        "register_number": "922122104045",
        "password": "922122104045",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 50000,
        "University Fee": 15000,
        "photo": "Sangeeth.png"
    },
    "922122104046": {
        "name": "Santhiya Priya M",
        "register_number": "922122104046",
        "password": "922122104046",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 35000,
        "University Fee": 16000,
        "photo": "Santhiya Priya.png"
    },
    "922122104047": {
        "name": "Sarathy V",
        "register_number": "922122104047",
        "password": "922122104047",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 22000,
        "University Fee": 11000,
        "photo": "Sarathy.png"
    },
    "922122104048": {
        "name": "Sarvatha R",
        "register_number": "922122104048",
        "password": "922122104048",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9000,
        "Tuition Fee": 19000,
        "University Fee": 15000,
        "photo": "Sarvatha.png"
    },
    "922122104049": {
        "name": "Sathish Karthick G",
        "register_number": "922122104049",
        "password": "922122104049",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 35000,
        "University Fee": 15000,
        "photo": "Sathish Karthick.png"
    },
    "922122104050": {
        "name": "Siva Bharathi M",
        "register_number": "922122104050",
        "password": "922122104050",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10500,
        "Tuition Fee": 22000,
        "University Fee": 15000,
        "photo": "Siva Bharathi.png"
    },
    "922122104051": {
        "name": "Siva Sibi S",
        "register_number": "922122104051",
        "password": "922122104051",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 25000,
        "University Fee": 10000,
        "photo": "Siva Sibi.png"
    },
    "922122104052": {
        "name": "Sri Swetha Y",
        "register_number": "922122104052",
        "password": "922122104052",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 35000,
        "University Fee": 15000,
        "photo": "Sri Swetha.png"
    },
    "922122104053": {
        "name": "Subbulakshmi S G",
        "register_number": "922122104053",
        "password": "922122104053",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 21500,
        "University Fee": 11000,
        "photo": "Subbulakshmi.png"
    },
    "922122104054": {
        "name": "Sujith Kumaar K S",
        "register_number": "922122104054",
        "password": "922122104054",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 9500,
        "Tuition Fee": 32500,
        "University Fee": 14500,
        "photo": "sujith.jpg" 
    },
    "922122104055": {
        "name": "Sumuthuradevi N",
        "register_number": "922122104055",
        "password": "922122104055",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 14500,
        "Tuition Fee": 22000,
        "University Fee": 9000,
        "photo": "Sumuthuradevi.png"
    },
    "922122104056": {
        "name": "Sundhareshwaran R",
        "register_number": "922122104056",
        "password": "922122104056",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10500,
        "Tuition Fee": 23000,
        "University Fee": 11000,
        "photo": "Sundhareshwaran.png"
        
    },
    "922122104057": {
        "name": "Susmitha G",
        "register_number": "922122104057",
        "password": "922122104057",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10500,
        "Tuition Fee": 22000,
        "University Fee": 15000,
        "photo": "Susmitha.png"
    },
    "922122104058": {
        "name": "Tamil Selvan R",
        "register_number": "922122104058",
        "password": "922122104058",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 16500,
        "Tuition Fee": 25000,
        "University Fee": 15000,
        "photo": "Tamil Selvan.png"
    },
    "922122104059": {
        "name": "Vijaya Raghavi J K",
        "register_number": "922122104059",
        "password": "922122104059",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10500,
        "Tuition Fee": 19000,
        "University Fee": 14000,
        "photo": "Vijaya Raghavi.png"
    },
    "922122104060": {
        "name": "Vinith S",
        "register_number": "922122104060",
        "password": "922122104060",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 16500,
        "Tuition Fee": 29500,
        "University Fee": 13000,
        "photo": "Vinith.png"
    },
    "922122104061": {
        "name": "Winfred Reji D R",
        "register_number": "922122104061",
        "password": "922122104061",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 22500,
        "University Fee": 15000,
        "photo": "infred Reji.png"
    },
    "922122104301": {
        "name": "Akash K",
        "register_number": "922122104301",
        "password": "922122104301",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 25000,
        "University Fee": 12000,
        "photo": "Akash.png"
    },
    "922122104302": {
        "name": "Edwin Kishore A",
        "register_number": "922122104302",
        "password": "922122104302",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 16000,
        "Tuition Fee": 19500,
        "University Fee": 18000,
        "photo": "Edwin Kishore.png"
    },
    "922122104303": {
        "name": "Gokul S",
        "register_number": "922122104303",
        "password": "922122104303",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 18000,
        "Tuition Fee": 28000,
        "University Fee": 16000,
        "photo": "Gokul.png"
    },
    "922122104304": {
        "name": "Jeyaseelan S",
        "register_number": "922122104304",
        "password": "922122104304",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 10000,
        "Tuition Fee": 31500,
        "University Fee": 15000,
        "photo": "Jeyaseelan.png"
    },
    "922122104305": {
        "name": "Ragul Pranav A",
        "register_number": "922122104305",
        "password": "922122104305",
        "department": "CSE",
        "year_sem": "III/6th",
        "bus_fee": 19500,
        "Tuition Fee": 28000,
        "University Fee": 7000,
        "photo": "Ragul Pranav.png"
    }

    
    
    
}

receipt_count = 1  
payment_log = []  # Each entry: {register_number, fee_type, amount, date}

# --------------------------
# Routes for Registration & Payment Flows
# --------------------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        reg = request.form.get('register_number')
        if reg in students:
            return render_template("studentsdetails.html",
                                   student_data=students[reg],
                                   register_number=reg)
        else:
            return "<h2 style='color:red;text-align:center;'>Invalid Register Number</h2>"
    return render_template("register.html")

@app.route('/fee/<register_number>')
def fee(register_number):
    if register_number in students:
        return render_template("fee.html",
                               student_data=students[register_number],
                               register_number=register_number)
    else:
        return "<h2 style='color:red;text-align:center;'>Invalid Register Number</h2>"

@app.route('/payment/<register_number>/<fee_type>')
def payment(register_number, fee_type):
    if register_number in students:
        student = students[register_number]
        if fee_type == "total_fee":
            fee_amount = student.get("bus_fee", 0) + student.get("Tuition Fee", 0) + student.get("University Fee", 0)
        else:
            fee_amount = student.get(fee_type, 0)
        return render_template("payment.html",
                               fee_type=fee_type,
                               amount=fee_amount,
                               register_number=register_number)
    else:
        return "<h2 style='color:red;text-align:center;'>Invalid Register Number</h2>"

# --- UPI Payment Flow Route ---
@app.route('/upi_payment/<register_number>/<upitype>', methods=['GET','POST'])
def upi_payment(register_number, upitype):
    if register_number not in students:
        return "<h2 style='color:red;text-align:center;'>Invalid Register Number</h2>"
    fee_type = request.args.get('fee_type')
    if not fee_type:
        return "<h2 style='color:red;text-align:center;'>Fee type not specified</h2>"
    student = students[register_number]
    if fee_type == "total_fee":
        fee_amount = student.get("bus_fee", 0) + student.get("Tuition Fee", 0) + student.get("University Fee", 0)
    else:
        fee_amount = student.get(fee_type, 0)
    if request.method == 'POST':
        upi_password = request.form.get('upi_password')
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        if upi_password == "1234":
            payment_log.append({
                "register_number": register_number,
                "fee_type": fee_type,
                "amount": fee_amount,
                "date": current_date
            })
            return render_template("payment_result.html", 
                                   success=True, 
                                   method=upitype, 
                                   fee_amount=fee_amount, 
                                   register_number=register_number, 
                                   fee_type=fee_type,
                                   student_data=student,
                                   current_date=current_date)
        else:
            return render_template("payment_result.html", 
                                   success=False, 
                                   method=upitype, 
                                   fee_amount=fee_amount, 
                                   register_number=register_number, 
                                   fee_type=fee_type,
                                   student_data=student,
                                   current_date=current_date)
    return render_template("upi_payment.html", register_number=register_number, upitype=upitype, fee_amount=fee_amount, fee_type=fee_type)

# --- NetBanking Payment Flow Route ---
@app.route('/netbanking_payment/<register_number>', methods=['GET','POST'])
def netbanking_payment(register_number):
    if register_number not in students:
        return "<h2 style='color:red;text-align:center;'>Invalid Register Number</h2>"
    fee_type = request.args.get('fee_type')
    if not fee_type:
        return "<h2 style='color:red;text-align:center;'>Fee type not specified</h2>"
    student = students[register_number]
    if fee_type == "total_fee":
        fee_amount = student.get("bus_fee", 0) + student.get("Tuition Fee", 0) + student.get("University Fee", 0)
    else:
        fee_amount = student.get(fee_type, 0)
    if request.method == 'POST':
        userid = request.form.get('netbanking_userid')
        password = request.form.get('netbanking_password')
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        if userid == "user" and password == "pass":
            payment_log.append({
                "register_number": register_number,
                "fee_type": fee_type,
                "amount": fee_amount,
                "date": current_date
            })
            return render_template("payment_result.html", 
                                   success=True, 
                                   method="Net Banking", 
                                   fee_amount=fee_amount, 
                                   register_number=register_number, 
                                   fee_type=fee_type,
                                   student_data=student,
                                   current_date=current_date)
        else:
            return render_template("payment_result.html", 
                                   success=False, 
                                   method="Net Banking", 
                                   fee_amount=fee_amount, 
                                   register_number=register_number, 
                                   fee_type=fee_type,
                                   student_data=student,
                                   current_date=current_date)
    return render_template("netbanking_payment.html", register_number=register_number, fee_amount=fee_amount, fee_type=fee_type)

# --- Receipt Generation ---
@app.route('/generate_receipt', methods=['POST'])
def generate_receipt():
    global receipt_count
    name = request.form.get('name')
    degree = request.form.get('degree')
    year = request.form.get('year')
    fee_type = request.form.get('fee_type')
    amount = request.form.get('amount')
    date = request.form.get('date')
    receipt_no = f"{receipt_count:04d}"
    receipt_count += 1
    return render_template('receipt.html', receipt_no=receipt_no, name=name, degree=degree, 
                           year=year, fee_type=fee_type, amount=amount, date=date)

@app.route('/receipt')
def receipt():
    return "<h2 style='text-align:center;'>This is your receipt. (Placeholder)</h2>"

@app.route('/payment-success')
def payment_success():
    return "<h2 style='text-align:center;'>Payment Successful! Thank you for your payment.</h2>"

# --------------------------
# Admin Login & Report Routes
# --------------------------
@app.route('/admin', methods=['GET','POST'])
def admin():
    error_message = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == "ssmiet9221":
            return redirect(url_for('admin_report'))
        else:
            error_message = "Incorrect Admin Password"
    return render_template("admin.html", error_message=error_message)

@app.route('/admin_report')
def admin_report():
    # Aggregate payments from payment_log.
    # For payments with fee_type "total_fee", distribute them proportionally.
    department_totals = {}
    year_totals = {}
    date_totals = {}
    for payment in payment_log:
        reg = payment["register_number"]
        ftype = payment["fee_type"]
        amt = payment["amount"]
        date_val = payment["date"]
        student = students.get(reg, {})
        dept = student.get("department", "Unknown")
        year = student.get("year_sem", "Unknown")
        if ftype == "total_fee":
            bus_due = student.get("bus_fee", 0)
            tuition_due = student.get("Tuition Fee", 0)
            univ_due = student.get("University Fee", 0)
            total_due = bus_due + tuition_due + univ_due
            if total_due > 0:
                bus_alloc = amt * (bus_due / total_due)
                tuition_alloc = amt * (tuition_due / total_due)
                univ_alloc = amt * (univ_due / total_due)
                for key, alloc in [((dept, "bus_fee"), bus_alloc),
                                   ((dept, "Tuition Fee"), tuition_alloc),
                                   ((dept, "University Fee"), univ_alloc)]:
                    department_totals[key] = department_totals.get(key, 0) + alloc
                for key, alloc in [((year, "bus_fee"), bus_alloc),
                                   ((year, "Tuition Fee"), tuition_alloc),
                                   ((year, "University Fee"), univ_alloc)]:
                    year_totals[key] = year_totals.get(key, 0) + alloc
                for key, alloc in [((date_val, "bus_fee"), bus_alloc),
                                   ((date_val, "Tuition Fee"), tuition_alloc),
                                   ((date_val, "University Fee"), univ_alloc)]:
                    date_totals[key] = date_totals.get(key, 0) + alloc
        else:
            dept_key = (dept, ftype)
            department_totals[dept_key] = department_totals.get(dept_key, 0) + amt
            year_key = (year, ftype)
            year_totals[year_key] = year_totals.get(year_key, 0) + amt
            date_key = (date_val, ftype)
            date_totals[date_key] = date_totals.get(date_key, 0) + amt

    return render_template('admin_report.html',
                           department_totals=department_totals,
                           year_totals=year_totals,
                           date_totals=date_totals,
                           fee_type="Paid")  # label for display

@app.route('/reset_payments', methods=['POST'])
def reset_payments():
    global payment_log
    payment_log.clear()
    return redirect(url_for('admin_report'))

# --- Individual Report ---
@app.route('/individual_report')
def individual_report():
    search_reg = request.args.get("search_reg", "").strip()
    student_data = None
    fee_details = None
    if search_reg:
        student = students.get(search_reg)
        if student:
            bus_due = student.get("bus_fee", 0)
            tuition_due = student.get("Tuition Fee", 0)
            univ_due = student.get("University Fee", 0)
            total_due = bus_due + tuition_due + univ_due

            bus_paid = sum(p["amount"] for p in payment_log if p["register_number"] == search_reg and p["fee_type"] == "bus_fee")
            tuition_paid = sum(p["amount"] for p in payment_log if p["register_number"] == search_reg and p["fee_type"] == "Tuition Fee")
            univ_paid = sum(p["amount"] for p in payment_log if p["register_number"] == search_reg and p["fee_type"] == "University Fee")
            total_fee_paid = sum(p["amount"] for p in payment_log if p["register_number"] == search_reg and p["fee_type"] == "total_fee")

            if total_due > 0:
                bus_alloc = total_fee_paid * (bus_due / total_due)
                tuition_alloc = total_fee_paid * (tuition_due / total_due)
                univ_alloc = total_fee_paid * (univ_due / total_due)
            else:
                bus_alloc = tuition_alloc = univ_alloc = 0

            effective_bus_paid = bus_paid + bus_alloc
            effective_tuition_paid = tuition_paid + tuition_alloc
            effective_univ_paid = univ_paid + univ_alloc

            bus_balance = bus_due - effective_bus_paid
            tuition_balance = tuition_due - effective_tuition_paid
            univ_balance = univ_due - effective_univ_paid

            fee_details = [
                {"fee_type": "Bus Fee", "due": bus_due, "paid": round(effective_bus_paid,2), "balance": round(bus_balance,2)},
                {"fee_type": "Tuition Fee", "due": tuition_due, "paid": round(effective_tuition_paid,2), "balance": round(tuition_balance,2)},
                {"fee_type": "University Fee", "due": univ_due, "paid": round(effective_univ_paid,2), "balance": round(univ_balance,2)}
            ]
            total_paid = effective_bus_paid + effective_tuition_paid + effective_univ_paid
            fee_details.append({"fee_type": "Total", "due": total_due, "paid": round(total_paid,2), "balance": round(total_due - total_paid,2)})
            student_data = {
                "register_number": search_reg,
                "name": student.get("name"),
                "department": student.get("department"),
                "year_sem": student.get("year_sem")
            }
        else:
            student_data = {"error": "Student not found"}
    return render_template("individual.html",
                           search_reg=search_reg,
                           student_data=student_data,
                           fee_details=fee_details)

# --- Payment Details Route ---
@app.route('/payment_details')
def payment_details():
    filter_type = request.args.get('filter_type')  # "department", "year", "date"
    filter_value = request.args.get('filter_value')
    fee_type = request.args.get('fee_type')
    filtered_payments = []
    for payment in payment_log:
        # If the requested fee type is not "total_fee", then include payments that are either exactly that fee type or are "total_fee" (to show distribution)
        if fee_type != "total_fee":
            if payment["fee_type"] not in [fee_type, "total_fee"]:
                continue
        else:
            if payment["fee_type"] != "total_fee":
                continue
        if filter_type == "department":
            student = students.get(payment["register_number"])
            if student and student.get("department") == filter_value:
                filtered_payments.append(payment)
        elif filter_type == "year":
            student = students.get(payment["register_number"])
            if student and student.get("year_sem") == filter_value:
                filtered_payments.append(payment)
        elif filter_type == "date":
            if payment["date"] == filter_value:
                filtered_payments.append(payment)
        else:
            filtered_payments.append(payment)
    return render_template("payment_details.html", 
                           payments=filtered_payments,
                           filter_type=filter_type,
                           filter_value=filter_value,
                           fee_type=fee_type,
                           students=students)

if __name__ == '__main__':
    app.run(debug=True)
