import requests
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

html_content = f"""
<html>
<head><title>{data['title']}</title></head>
<body>
    <h1>{data['title']}</h1>
    <p>{data['body']}</p>
</body>
</html>
"""

with open(output_dir / "index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
