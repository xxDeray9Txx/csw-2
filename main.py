from pyscript import document, display

def calc_gwa():
    try:
        # get all grades
        math = float(document.getElementById("math").value)
        sci = float(document.getElementById("sci").value)
        eng = float(document.getElementById("eng").value)
        music = float(document.getElementById("music").value)
        ict = float(document.getElementById("ict").value)

        # compute average
        gwa = (math + sci + eng + music + ict) / 5

        # remarks
        if gwa >= 90:
            remark = "Excellent"
        elif gwa >= 85:
            remark = "Very Good"
        elif gwa >= 80:
            remark = "Good"
        elif gwa >= 75:
            remark = "Passed"
        else:
            remark = "Failed"

        # show result
        display(f"GWA: {gwa:.2f} — {remark}", target="result")

    except:
        display("Enter valid numbers!", target="result")

weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
total_units = (5 * 3) + 3 + 2 + 1
gwa = weighted_sum / total_unit
display(f"GWA: {gwa:.2f}", target="result") 
display(f'Name: {first_name} {last_name}', target="student_info")
display(summary, target='summary')
display(f'Your general weighted average is {gwa:.2f}', target='output')

