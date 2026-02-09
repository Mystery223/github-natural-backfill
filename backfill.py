
import os
import random
from datetime import datetime, timedelta

# ===== CONFIG =====
DAYS_BACK = 345          # Berapa hari ke belakang ingin diisi
MIN_COMMITS = 5         # Minimal commit per hari
MAX_COMMITS = 25         # Maksimal commit per hari
FILE_NAME = "activity_log.txt"
# ==================

def run():
    for d in range(1, DAYS_BACK + 1):
        commit_count = random.randint(MIN_COMMITS, MAX_COMMITS)

        for _ in range(commit_count):
            random_minutes = random.randint(0, 1440)
            commit_date = datetime.now() - timedelta(days=d, minutes=random_minutes)
            formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

            with open(FILE_NAME, "a") as f:
                f.write(f"Update at {formatted_date}\n")

            os.system("git add .")
            os.system(
                f'GIT_AUTHOR_DATE="{formatted_date}" '
                f'GIT_COMMITTER_DATE="{formatted_date}" '
                f'git commit -m "chore: natural update"'
            )

    print("✅ Backfill selesai. Jangan lupa git push!")

if __name__ == "__main__":
    run()
