import json

def load_students():
    with open("students.json", "r") as f:
        return json.load(f)

def generate_attendance(absent_rolls):
    students = load_students()
    result = []

    for s in students:
        roll = s["roll"]
        name = s["name"]
        phone = s["phone"]

        if roll in absent_rolls:
            status_ui = "✘"          # red cross
            status_csv = "A"         # CSV format
            sms = f"SMS to {phone}: {name} (Roll {roll}) is ABSENT today."
        else:
            status_ui = "✔"          # green tick
            status_csv = "P"
            sms = ""

        result.append({
            "roll": roll,
            "name": name,
            "status_ui": status_ui,
            "status_csv": status_csv,
            "sms": sms
        })

    return result
