import subprocess

def runAnsiblePlaybook(playbookPath, inventoryPath):
    try:
        # Run the Ansible playbook using the 'ansible-playbook' command
        result = subprocess.run(['ansible-playbook', '--ask-become-pass', '-i', inventoryPath, playbookPath], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
    # print error if the process failed
        return e.stderr

#the python file resides in the same directory as the playbook and inventory files
playbookPath = 'playbook.yml' 
inventoryPath = 'hosts'

print('Running Ansible playbook...')
#call on the defined function and input the variables
playbookOutput = runAnsiblePlaybook(playbookPath, inventoryPath)

print('Ansible playbook output:')
#print the output after the process is completed
print(playbookOutput)