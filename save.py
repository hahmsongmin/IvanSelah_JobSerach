import csv, openpyxl

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding='utf-8-sig', newline='')
    writer = csv.writer(file)
    writer.writerow(["회사", "채용", "지역", "링크"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

    # excel_file = openpyxl.load_workbook('jobs.xlsx')
    # excel_sheet = excel_file.active
    # excel_sheet.append(["회사", "채용", "지역", "링크"])
    # excel_sheet.column_dimensions['A'].width = 50
    # excel_sheet.column_dimensions['B'].width = 80
    # excel_sheet.column_dimensions['C'].width = 15
    # excel_sheet.column_dimensions['D'].width = 100
    #
    # for job in jobs:
    #     excel_sheet.append(list(job.values()))
    #     excel_sheet.cell(column=4).hyperlink =

