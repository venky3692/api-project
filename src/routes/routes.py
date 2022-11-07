from flask import *
from filehandler import app
from src.db import db
from src.models.models import file_db
from src.utils.util import convert_to_pdf


@app.route("/")
def welcome_page():
    return "Welcome to the file handler!"

@app.route("/file", methods = ["GET", "POST"])
def get_file_details():
        if request.method == "POST":
            get_file = request.files.getlist('file[ ]')
            for files in get_file:
                get_file_name  = files.filename
                convert_to_pdf(get_file_name)
                # # pdf = FPDF()
                # # pdf.add_page() 
                # # pdf.set_font("Arial", size = 15) 
                # f = open(os.path.expanduser('~')  +'/Downloads/' + get_file_name , "r")
                db_source_file_name = file_db(source_file_name= get_file_name)
                db.session.add(db_source_file_name)
                db.session.commit()
                # for x in f: 
                    # pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
                # pdf.output(os.path.expanduser('~') + '/' +get_file_name + '_converted.pdf')
                conv_file_name = get_file_name + '_converted.pdf'
                db_converted_file_name = file_db(converted_file_name = conv_file_name)
                db.session.add(db_converted_file_name)
                db.session.commit() 
            return make_response("file/ files successfully converted", get_file_name)