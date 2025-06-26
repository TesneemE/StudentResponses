import pandas

questions = pandas.read_csv("Student Questions - Sheet1.csv")
question_list = []
for index, row in questions.iterrows():
    question_list += (row.Question.split(';'))

print(question_list)

# data = pandas.read_csv("Prep for Prep - IFE Summer 2024-submissions (updated 2024-08-01 174018 UTC).csv")
# print(data.loc[data["Prompt"] == "6 Your Why"])
