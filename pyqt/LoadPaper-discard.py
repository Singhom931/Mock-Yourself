def process_mock_test_content(content):
    lines = content.split('\n')
    processed_data = []
    current_section = None
    current_question = None
    question_number = None
    capturing_options = False

    for line in lines:
        line = line.strip()
        if line.startswith("Section"):
            current_section = {"section": line, "questions": []}
            processed_data.append(current_section)
        elif line.startswith("Question"):
            question_number = int(line.split(" ")[1][:-1])
            current_question = {
                "number": question_number,
                "text": "",
                "options": [],
                "correct_answer": ""
            }
            capturing_options = False
        elif line.startswith(("a)", "b)", "c)", "d)")):
            capturing_options = True
            current_question["options"].append(line)
        elif line.startswith("Correct Answer:"):
            current_question["correct_answer"] = line[len("Correct Answer:"):].strip()
            current_section["questions"].append(current_question)
            current_question = None
            capturing_options = False
        elif capturing_options:
            current_question["options"].append(line)

    return processed_data

with open("paper/test1.txt", "r") as file:
    content = file.read()

processed_data = process_mock_test_content(content)
print(processed_data)
