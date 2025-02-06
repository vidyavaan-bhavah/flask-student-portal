from flask import Flask, render_template, request
from config import Config
from database import db
from models import Student, Attendance, Homework, Exam, Fees

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        roll_number = request.form["roll_number"]
        student = Student.query.filter_by(student_roll_number=roll_number).first()
        if student:
            return render_template("dashboard.html", student=student)
        return "Student not found", 404
    return render_template("index.html")

@app.route("/dashboard/<int:student_id>")
def dashboard(student_id):
    student = Student.query.get(student_id)
    if not student:
        return "Student not found", 404
    attendance = Attendance.query.filter_by(student_id=student_id).all()
    homework = Homework.query.filter_by(student_id=student_id).all()
    exams = Exam.query.filter_by(student_id=student_id).all()
    fees = Fees.query.filter_by(student_id=student_id).all()
    return render_template("dashboard.html", student=student, attendance=attendance, homework=homework, exams=exams, fees=fees)

if __name__ == "__main__":
    app.run(debug=True)