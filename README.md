Jenkins Pipeline Cloner
Effortlessly duplicate your Jenkins multi-branch pipeline jobs while seamlessly transitioning to new GitHub repositories.

Overview
This Python-powered utility streamlines the process of replicating your Jenkins multi-branch pipelines, empowering you to:

Clone with Confidence: Replicate your existing pipeline job configurations, ensuring consistency across your Jenkins projects.
Seamless Repository Switching: Effortlessly update the GitHub repository associated with the new pipeline, facilitating project migrations or branch-specific workflows.
Automation at Your Fingertips: Eliminate manual configuration steps, saving time and reducing the risk of human error.
API-Driven Efficiency: Leverage the Jenkins REST API for direct interaction with your Jenkins server, ensuring robust and reliable operation.
Features
Intuitive Command-Line Interface: Simple prompts guide you through the cloning process, making it accessible to users of all skill levels.
GitHub Repository Flexibility: Specify any valid GitHub repository URL, granting you complete control over your project's source code integration.
Customization Potential: Modify the Python script to accommodate unique job configuration requirements or extend its functionality.
Clear Output: Receive informative messages during the cloning process, keeping you informed of progress and any potential issues.
Prerequisites
Jenkins Server: A running Jenkins instance with the necessary API access enabled.
Python 3: Ensure Python 3 is installed on your system.
requests Library: Install the requests library using pip install requests.
Jenkins Credentials: Have your Jenkins username and password readily available.
Installation
Clone the Repository:  Clone this GitHub repository to your local machine.

Bash
git clone https://github.com/your-username/jenkins-pipeline-cloner.git   

Use code with caution.

Navigate to the Project Directory:

Bash
cd jenkins-pipeline-cloner
Use code with caution.

Usage
Open the Script:  Open the clone_jenkins_pipeline.py file in your preferred text editor or IDE.

Configure Jenkins Details:

Replace the placeholders in the script with your actual Jenkins server URL, username, and password:

Python
jenkins_url = 'http://your-jenkins-server:8080'
username = 'your-jenkins-username'
password = 'your-jenkins-password'
Use code with caution.

Run the Script:  Execute the script from your terminal:

Bash
python clone_jenkins_pipeline.py
Use code with caution.

Follow the Prompts:  The script will guide you through the cloning process, asking for:

The name of the existing Jenkins job you want to clone
The desired name for the new Jenkins job
The URL of the new GitHub repository you want to associate with the new pipeline
Success Message:  Upon successful cloning, you'll receive a confirmation message.

Contributing
Contributions are welcome! Feel free to submit pull requests or open issues to report bugs or suggest enhancements.

License
This project is licensed under the MIT License.

