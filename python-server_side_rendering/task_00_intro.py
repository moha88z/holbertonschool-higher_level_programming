#!/usr/bin/python
def generate_invitations(template, attendees):
   
    if type(template) is not str:
        print("The template must be a string.")
        return
    if type(attendees) is not list or any(type(a) is not dict for a in attendees):
        print("The attendees list must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Empty template, no files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no files generated.")
        return

    fields = ['name', 'event_title', 'event_date', 'event_location']

    for i in range(len(attendees)):
        line = template
        for field in fields:
            val = attendees[i].get(field)
            if val is None or val == "":
                line = line.replace("{" + field + "}", "N/A")
            else:
                line = line.replace("{" + field + "}", str(val))
        try:
            with open("output_" + str(i+1) + ".txt", "w", encoding="utf-8") as f:
                f.write(line)
        except Exception as e:
            print("Error writing file output_" + str(i+1) + ".txt:", e)
