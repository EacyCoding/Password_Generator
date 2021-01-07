# Install passgen module
import subprocess
import sys

def install(package):
    subprocess.call([
        sys.executable,
        '-m',
        'pip',
        '--disable-pip-version-check',
        '-q',
        'install',
        package
    ])
install('passgen')

# Actual code golf password gen:
import passgen as p
print(p.passgen(length=15,punctuation=True))
