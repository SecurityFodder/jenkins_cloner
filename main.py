import jenkins
import lxml.etree as ET

# Jenkins server credentials and URLs
jenkins_url = 'http://your_jenkins_url'  # Replace with your Jenkins URL
username = 'your_username'               # Replace with your Jenkins username
password = 'your_password'               # Replace with your Jenkins password or API token

# Job names and new repository URL
existing_job_name = 'existing_multibranch_pipeline_job'  # Replace with the existing job name
new_job_name = 'new_multibranch_pipeline_job'            # Replace with the new job name
new_repo_url = 'https://github.com/your_new_repo.git'    # Replace with the new GitHub repository URL

# Connect to Jenkins
server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# Get the configuration XML of the existing job
config_xml = server.get_job_config(existing_job_name)

# Parse the XML configuration
root = ET.fromstring(config_xml)

# Function to strip namespaces from XML tags
def strip_namespace(element):
    for elem in element.iter():
        if elem.tag.startswith('{'):
            elem.tag = elem.tag.split('}', 1)[1]

# Strip namespaces to simplify tag searching
strip_namespace(root)

# Function to update the repository URL in the XML configuration
def update_repository_url(root_element, new_url):
    updated = False
    # Iterate through all <source> elements
    for source in root_element.findall('.//source'):
        scm_class = source.get('class')
        # Check if the source is a Git SCM source
        if scm_class == 'jenkins.plugins.git.GitSCMSource':
            remote = source.find('remote')
            if remote is not None:
                old_repo_url = remote.text
                remote.text = new_url
                updated = True
                print(f'Replaced repository URL: {old_repo_url} -> {new_url}')
    return updated

# Update the repository URL
if not update_repository_url(root, new_repo_url):
    print('Repository URL not found in the configuration.')
    exit(1)

# Convert the modified XML back to a string
modified_config_xml = ET.tostring(root, encoding='unicode')

# Check if the new job already exists
if server.job_exists(new_job_name):
    print(f'A job with the name "{new_job_name}" already exists.')
    exit(1)

# Create the new job with the modified configuration
server.create_job(new_job_name, modified_config_xml)
print(f'New job "{new_job_name}" created with repository "{new_repo_url}".')
