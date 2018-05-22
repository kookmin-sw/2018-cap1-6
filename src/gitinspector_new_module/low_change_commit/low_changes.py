import subprocess

class LowChanges(object):
    link = "https://github.com/kookmin-sw/"
    commit_list = {}

    def __init__(self, repos):
        proc = subprocess.Popen(filter(None, ["git", "rev-list", "--date-order", "--no-merges", "HEAD", "--abbrev-commit"]) , bufsize=1, stdout = subprocess.PIPE).stdout
        out = proc.readlines()
        repos_string = ", ".join([repo.name for repo in repos])
        repos_string = repos_string.split("_")
        repos_string = repos_string[1]
        self.link += repos_string + "/commit/"

        for i in range(len(out)-1):
            j = out[i].strip().decode("unicode_escape","ignore")
            j = j.encode("latin-1", "replace")
            j = j.decode("utf-8", "replace")

            tmp = j+"^"
            proc2 = subprocess.Popen(filter(None, ["git", "diff", "--stat", tmp, j]), bufsize=1, stdout = subprocess.PIPE).stdout
            out2 = proc2.readlines()
            plus = -1
            minus = -1

            proc3 = subprocess.Popen(filter(None, ["git", "log", "--oneline", "-1", j]), bufsize=1, stdout = subprocess.PIPE).stdout
            out3 = proc3.readlines()

            for k in out2:
                q = k.strip().decode("unicode_escape","ignore")
                q = q.encode("latin-1","replace")
                q = q.decode("utf-8", "replace")
                for e in range(len(q)):
                    if q[e] == '+':
                        plus += 1
                    if q[e] == '-':
                        minus += 1

            for k in out3:
                q = k.strip().decode("unicode_escape","ignore")
                q = q.encode("latin-1","replace")
                q = q.decode("utf-8","replace")
                j = q

            if plus == -1:
                plus = 0

            if minus == -1:
                minus = 0

            tmp = plus + minus
            if tmp <=5:
                self.commit_list[j] = tmp
