import subprocess

def install_requirements():
    try:
        result = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
        if result.stderr:
            print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing the requirements: {e}")
        print(e.stderr.decode('utf-8'))

if __name__ == "__main__":
    install_requirements()
