from database import db

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    student_roll_number = db.Column(db.String, unique=True, nullable=False)
    student_name = db.Column(db.String, nullable=False)
    student_batch_id = db.Column(db.Integer)
    student_fees = db.Column(db.String)

class Attendance(db.Model):
    attendance_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"))
    status = db.Column(db.String)
    date = db.Column(db.Date)

class Homework(db.Model):
    homework_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"))
    status = db.Column(db.String)
    date = db.Column(db.Date)

class Exam(db.Model):
    exam_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"))
    exam_topic = db.Column(db.String)
    exam_marks = db.Column(db.String)

class Fees(db.Model):
    fees_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"))
    amount = db.Column(db.String)
    payment_mode = db.Column(db.String)