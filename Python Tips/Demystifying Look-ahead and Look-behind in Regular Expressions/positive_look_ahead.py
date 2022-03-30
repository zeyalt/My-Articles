import re

text = "With great power comes great responsibility."
pattern = r'\b\w+\b(?= great)'
matches = re.finditer(pattern, text)
for match in matches:
    print(f'Match: "{match.group()}" => Span: {match.span()}')