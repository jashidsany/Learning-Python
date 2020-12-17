"""
The admissions office at Calvin Coolidge’s Cool College has heard about your programming prowess and wants to get a piece of it for themselves.
They’ve been inundated with applications and need a way to automate the filtering process.
They collect three pieces of information for each applicant:
Their high school GPA, on a 0.0 - 4.0 scale.
Their personal statement, which is given a score on a 1 - 100 scale.
The number of extracurricular activities they participate in.
The admissions office has a cutoff point for each category.
They want students that have a GPA of 3.0 or higher, a personal statement with a score of 90 or higher, and who participated in 3 or more extracurricular activities.
Write a function called applicant_selector which takes three inputs, gpa, ps_score, and ec_count.
If the applicant meets the cutoff point for all three categories, have the function return the string:
"""

def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count <= 2):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
