import os
import yaml
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)


CONFIG_FILE = os.path.join(PROJECT_DIR, "config", "test_config.yaml")
LOG_DIR = os.path.join(PROJECT_DIR, "logs")
REPORT_DIR = os.path.join(PROJECT_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

with open(CONFIG_FILE, "r") as file:
    config = yaml.safe_load(file)

summary = []

pass_count = 0
fail_count = 0

for test in config["tests"]:

    test_name = test["name"]

    logfile = os.path.join(LOG_DIR, f"{test_name}.log")

    errors = 0
    warnings = 0
    fatals = 0
    result = "NOT_RUN"

    if os.path.exists(logfile):

        with open(logfile, "r") as f:
            data = f.read()

        errors = data.count("UVM_ERROR")
        warnings = data.count("UVM_WARNING")
        fatals = data.count("UVM_FATAL")

        if "RESULT : PASSED" in data:
            result = "PASSED"
            pass_count += 1

        elif "RESULT : FAILED" in data:
            result = "FAILED"
            fail_count += 1

    summary.append({
        "test": test_name,
        "errors": errors,
        "warnings": warnings,
        "fatals": fatals,
        "result": result
    })

df = pd.DataFrame(summary)

df.to_csv(
    os.path.join(REPORT_DIR, "summary.csv"),
    index=False
)

df.to_excel(
    os.path.join(REPORT_DIR, "summary.xlsx"),
    index=False
)

with open(os.path.join(REPORT_DIR, "summary.yaml"), "w") as f:
    yaml.dump(
        summary,
        f,
        default_flow_style=False,
        sort_keys=False
    )

print("\n==============================")
print(f"PASS : {pass_count}")
print(f"FAIL : {fail_count}")
print("==============================")
