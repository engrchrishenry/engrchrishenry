from scholarly import scholarly
import svgwrite

# Your Google Scholar user ID
USER_ID = "VOm093YAAAAJ"

# Output SVG file
OUTPUT_FILE = "citations.svg"

# Fetch citation data
author = scholarly.search_author_id(USER_ID)
author = scholarly.fill(author)
citations_count = author['citedby']

# Create badge
dwg = svgwrite.Drawing(OUTPUT_FILE, profile='tiny', size=('150px','20px'))
dwg.add(dwg.rect(insert=(0,0), size=('150px','20px'), rx=3, ry=3, fill='#4c1'))
dwg.add(dwg.text(f'Citations: {citations_count}', insert=(75,14),
                 text_anchor="middle", fill='white', font_size="12px", font_family="Verdana"))
dwg.save()
print(f"Generated badge with {citations_count} citations.")