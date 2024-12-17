import xml.etree.ElementTree as ET


def list_e_projects(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    e_projects = {}

    for employee in root.findall('employee'):
        name = employee.find('name').text
        projects = [project.text for project in employee.find('projects').findall('project')]
        e_projects[name] = projects

    return e_projects


# call
file_path = 'mitarbeiter.xml'
projects = list_e_projects(file_path)

print(projects)
