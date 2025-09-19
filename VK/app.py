from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def student_form():
    if request.method == "POST":
        name = request.form["name"]
        roll_number = request.form["roll_number"]
        department = request.form["department"]
        email = request.form["email"]
        phone = request.form["phone"]

        # For now, just show the submitted data
        return f"""
        <h2>Student Details Submitted Successfully!</h2>
        <p><b>Name:</b> {name}</p>
        <p><b>Roll Number:</b> {roll_number}</p>
        <p><b>Department:</b> {department}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Phone:</b> {phone}</p>
        <a href="/">Go Back</a>
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
