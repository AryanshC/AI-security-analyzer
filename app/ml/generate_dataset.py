import pandas as pd
import random

normal = [
    "User logged in successfully",
    "Database backup completed",
    "File uploaded successfully",
    "Password changed successfully",
    "API request completed",
    "Dashboard viewed",
    "Email sent successfully",
    "System health check passed",
    "Configuration updated",
    "Report generated successfully"
]

bruteforce = [
    "Multiple failed SSH login attempts",
    "Repeated password failures",
    "Too many login attempts detected",
    "Admin login failed 15 times",
    "Failed login from unknown IP",
    "Rapid authentication failures",
    "SSH brute force detected",
    "Account locked after login failures"
]

sql = [
    "UNION SELECT detected",
    "SQL injection attempt",
    "Database query contains OR 1=1",
    "Suspicious SQL statement",
    "DROP TABLE command detected",
    "SELECT * FROM users WHERE",
    "Database injection blocked"
]

xss = [
    "<script>alert('xss')</script>",
    "Javascript injected into input",
    "Cross-site scripting detected",
    "Malicious HTML submitted",
    "XSS payload blocked"
]

malware = [
    "PowerShell downloading payload",
    "Executable launched from temp folder",
    "Suspicious process spawned",
    "Encoded PowerShell command executed",
    "Unknown binary executed",
    "Malware signature detected"
]

rows = []

for _ in range(250):
    rows.append([random.choice(normal), "Normal"])

for _ in range(250):
    rows.append([random.choice(bruteforce), "BruteForce"])

for _ in range(250):
    rows.append([random.choice(sql), "SQLInjection"])

for _ in range(250):
    rows.append([random.choice(xss), "XSS"])

for _ in range(250):
    rows.append([random.choice(malware), "Malware"])

random.shuffle(rows)

df = pd.DataFrame(rows, columns=["text", "label"])

df.to_csv("app/ml/data/cyber_logs.csv", index=False)

print(f"Created dataset with {len(df)} samples!")