#TODO: error if survey file is invalid
def parse_survey(survey_name):
    survey_file = open("/etc/sws/surveys/%s" % survey_name)

    survey = []
    current_item = []
    
    for line in survey_file:
        line = line.replace("\n","")

        if line.find("\t") == -1:
            if current_item != []:
                survey += [current_item]
                current_item = []

            sep1 = line.find(":")
            sep2 = line.find(":", sep1 + 1)

            item_name = line[:sep1]
            item_type = line[sep1+1:sep2]
            item_text = line[sep2+1:]

            current_item += [item_name, item_type, item_text]
        elif line.find("\t") == 0:
            sep = line.find(":")

            choice_name = line[1:sep]
            choice_text = line[sep+1:]

            current_item += [[choice_name, choice_text]]

    if current_item != []:
        survey += [current_item]

    return survey
