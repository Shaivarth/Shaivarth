from datetime import datetime
import re
import os

# Your badge URL (already set for your TryHackMe username)
badge_url_base = "https://tryhackme-badges.s3.amazonaws.com/Shaivarth.png"
readme_path = "README.md"

# Read README.md content
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Create new timestamp
timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
new_url = f"{badge_url_base}?timestamp={timestamp}"

# Replace or insert badge
if "tryhackme-badges.s3.amazonaws.com/Shaivarth.png" in content:
    # Update old timestamp if badge exists
    content = re.sub(
        r"https://tryhackme-badges\.s3\.amazonaws\.com/Shaivarth\.png(\?timestamp=\d+)?",
        new_url,
        content
    )
else:
    # Append badge if it doesn't exist
    content += f"\n\n![TryHackMe Stats]({new_url})\n"

# Save updated README.md
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f" Updated badge to: {new_url}")
