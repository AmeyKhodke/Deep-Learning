import os
import subprocess
from datetime import datetime, timedelta
import random

# --- Configuration ---
START_DATE = datetime(2025, 10, 20) 
END_DATE = datetime.now()            
MIN_COMMITS = 3              
MAX_COMMITS = 8             
FILE_NAME = ".work_log"  # Hidden file so it doesn't clutter your repo

# --- YOUR REAL DIRECTORIES ---
# The script will use these to generate realistic commit messages
TOPICS = [
    "Perceptron",
    "Backpropagation Algorithm",
    "Improving Neural Network",
    "Vanishing Gradient Problem"
]

ACTIONS = [
    "Implement initial logic for",
    "Refactor code in",
    "Optimize gradients in",
    "Fix convergence issue in",
    "Update documentation for",
    "Add unit tests for",
    "Clean up variables in"
]

# --- YOUR IDENTITY ---
CORRECT_NAME = "AmeyKhodke"
CORRECT_EMAIL = "ameykhodke430@gmail.com"

def run(cmd, env):
    subprocess.run(cmd, shell=True, env=env, stdout=subprocess.DEVNULL)

def main():
    print(f"--- Generating Realistic History for {CORRECT_NAME} ---")
    
    if not os.path.exists(".git"):
        print("Initializing new git repository...")
        subprocess.run("git init", shell=True, stdout=subprocess.DEVNULL)

    current_date = START_DATE
    total = 0

    while current_date <= END_DATE:
        daily_count = random.randint(MIN_COMMITS, MAX_COMMITS)
        
        # Pick a "Focus Topic" for the day to make it look realistic
        # (e.g., You probably spent the whole day working on just Backprop)
        daily_topic = random.choice(TOPICS)
        
        print(f"Processing {current_date.strftime('%Y-%m-%d')}: Working on {daily_topic}...")
        
        for _ in range(daily_count):
            h, m, s = random.randint(9, 23), random.randint(0, 59), random.randint(0, 59)
            date_str = current_date.replace(hour=h, minute=m, second=s).strftime('%Y-%m-%d %H:%M:%S')

            # 1. Update hidden log
            with open(FILE_NAME, "a") as f: 
                f.write(f"[{date_str}] Modified {daily_topic}\n")
            
            # 2. Generate Real Message
            action = random.choice(ACTIONS)
            message = f"{action} {daily_topic}"

            # 3. Set Identity & Date
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            env["GIT_AUTHOR_NAME"] = CORRECT_NAME
            env["GIT_AUTHOR_EMAIL"] = CORRECT_EMAIL
            env["GIT_COMMITTER_NAME"] = CORRECT_NAME
            env["GIT_COMMITTER_EMAIL"] = CORRECT_EMAIL

            # 4. Commit
            run(f"git add {FILE_NAME}", env)
            run(f'git commit -m "{message}"', env)
            total += 1
        
        current_date += timedelta(days=1)

    # Clean up the temp file
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        run(f"git add {FILE_NAME}", env)
        run('git commit -m "Final cleanup of logs"', env)

    print("-" * 50)
    print(f"Success! Generated {total} realistic commits.")
    print("Run: git remote add origin ... -> git branch -M main -> git push -u origin main")

if __name__ == "__main__":
    main()