import subprocess

proc = subprocess.Popen(
    'git log --name-only --pretty=format: | sort | uniq -c | sort -nr',
    stdout = subprocess.PIPE,
    shell=True
)

out, err = proc.communicate()
print(out)
