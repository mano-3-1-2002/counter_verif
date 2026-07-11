#!/usr/bin/env python3

import os
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)

CONFIG_FILE = os.path.join(PROJECT_DIR, "config", "test_config.yaml")

# Read YAML configuration
with open(CONFIG_FILE, "r") as file:
    config = yaml.safe_load(file)

tests = config["tests"]

print("=" * 50)
print("Running Regression")
print("=" * 50)

for test in tests:
    testname = test["name"]
    seed = test["seed"]

    print(f"\nRunning {testname} (Seed={seed})")

    cmd = f"make -C sim regress_sim TESTNAME={testname} SEED={seed}"
    status = os.system(cmd)

    if status == 0:
        print(f"{testname} completed successfully.")
    else:
        print(f"{testname} failed with exit code {status}")

print("\nRegression Complete.")
