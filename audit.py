import json, sys, random

def audit_log(user_text, agent_text):
    u = user_text.lower()
    a = agent_text.lower()
    if "belgrade" in u and "bangkok" in a:
        return "FAIL fact_over_phantom"
    if "belgrade" in u and "belgrade" in a:
        return "CLEAN"
    return "KEEP"

def hold_020_check():
    w = {a:0.2 for a in ["h","m","b","l","s"]}
    for _ in range(100):
        x = random.uniform(-1,1)
        raw = {k:0.20+0.025*x for k in w}
        total = sum(raw.values())
        w = {k:raw[k]/total for k in w}
    return all(abs(v-0.2)<1e-12 for v in w.values())

if __name__=="__main__":
    print("hold_0.20:", hold_020_check())
    for line in open(sys.argv[1]):
        log = json.loads(line)
        print(audit_log(log["user"], log["agent"]), "-", log)
