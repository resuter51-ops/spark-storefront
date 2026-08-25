from pathlib import Path

# One-time restoration of the published Bob's Thoughts list on the overlay.
path = Path("index-original.html")
text = path.read_text(encoding="utf-8")
start_marker = "        <!-- Blog post card -->"
end_marker = "        <div class=\"section-nav\">"

if start_marker not in text:
    raise SystemExit("Could not find the existing Bob's Thoughts card marker")
start = text.index(start_marker)
if end_marker not in text[start:]:
    raise SystemExit("Could not find the Bob's Thoughts section navigation marker")
end = text.index(end_marker, start)

cards = """        <!-- Bob's Thoughts: all currently published public posts, newest first -->
        <a href="https://wordsandwheels.net/blog/bob-s-thoughts/our-lives-are-like-books" target="_blank" rel="noopener" style="display:block;text-decoration:none;color:inherit;margin-bottom:24px;border:1px solid #e0ddd5;border-radius:14px;overflow:hidden;transition:box-shadow 0.3s,transform 0.2s;" onmouseover="this.style.boxShadow='0 6px 20px rgba(0,0,0,0.08)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
            <div style="display:flex;flex-direction:column;">
                <div style="height:180px;background:linear-gradient(135deg,#1a2a4a,#d4a849);display:flex;align-items:center;justify-content:center;padding:20px;text-align:center;">
                    <div style="font-family:Georgia,serif;color:white;font-size:28px;line-height:1.25;">Our Lives Are Like Books</div>
                </div>
                <div style="padding:24px;">
                    <div style="font-size:13px;color:#999;font-family:Arial,sans-serif;margin-bottom:8px;">Bob's Thoughts</div>
                    <h2 style="font-size:22px;font-family:Georgia,serif;color:var(--dark);margin-bottom:10px;line-height:1.3;">Our Lives Are Like Books</h2>
                    <p style="font-size:15px;color:var(--light-text);font-family:Arial,sans-serif;line-height:1.7;">Read the complete post on Words &amp; Wheels.</p>
                    <div style="margin-top:14px;color:var(--gold);font-size:14px;font-family:Arial,sans-serif;font-weight:bold;">Read More &rarr;</div>
                </div>
            </div>
        </a>

        <a href="https://wordsandwheels.net/blog/bob-s-thoughts/the-great-breakfast-negotiations" target="_blank" rel="noopener" style="display:block;text-decoration:none;color:inherit;margin-bottom:24px;border:1px solid #e0ddd5;border-radius:14px;overflow:hidden;transition:box-shadow 0.3s,transform 0.2s;" onmouseover="this.style.boxShadow='0 6px 20px rgba(0,0,0,0.08)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
            <div style="display:flex;flex-direction:column;">
                <img src="https://payhip.com/cdn-cgi/image/format=auto,width=1500/https://pe56d.s3.amazonaws.com/o_1jv4mmmfnkmf1ntjbglj151jmsc.png" alt="The Great Breakfast Negotiations" style="width:100%;height:220px;object-fit:cover;background:var(--cream);" onerror="this.style.display='none'">
                <div style="padding:24px;">
                    <div style="font-size:13px;color:#999;font-family:Arial,sans-serif;margin-bottom:8px;">August 03, 2026</div>
                    <h2 style="font-size:22px;font-family:Georgia,serif;color:var(--dark);margin-bottom:10px;line-height:1.3;">The Great Breakfast Negotiations</h2>
                    <p style="font-size:15px;color:var(--light-text);font-family:Arial,sans-serif;line-height:1.7;">Living in a nursing home teaches you many things. It teaches patience. It teaches flexibility. It teaches gratitude. It also teaches that ordering breakfast can become more complicated than negotiating an international peace treaty.</p>
                    <div style="margin-top:14px;color:var(--gold);font-size:14px;font-family:Arial,sans-serif;font-weight:bold;">Read More &rarr;</div>
                </div>
            </div>
        </a>

        <a href="https://wordsandwheels.net/blog/bob-s-thoughts/welcome-to-wheels-and-words-life-looks-different-from-where-i-sit" target="_blank" rel="noopener" style="display:block;text-decoration:none;color:inherit;margin-bottom:24px;border:1px solid #e0ddd5;border-radius:14px;overflow:hidden;transition:box-shadow 0.3s,transform 0.2s;" onmouseover="this.style.boxShadow='0 6px 20px rgba(0,0,0,0.08)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
            <div style="display:flex;flex-direction:column;">
                <img src="https://payhip.com/cdn-cgi/image/format=auto,width=1500/https://pe56d.s3.amazonaws.com/o_1jugdmlo6t8op5r1fn3ks51fd4c.png" alt="Welcome to Wheels and Words" style="width:100%;height:220px;object-fit:cover;background:var(--cream);" onerror="this.style.display='none'">
                <div style="padding:24px;">
                    <div style="font-size:13px;color:#999;font-family:Arial,sans-serif;margin-bottom:8px;">July 26, 2026</div>
                    <h2 style="font-size:22px;font-family:Georgia,serif;color:var(--dark);margin-bottom:10px;line-height:1.3;">Welcome to Wheels and Words: Life Looks Different From Where I Sit</h2>
                    <p style="font-size:15px;color:var(--light-text);font-family:Arial,sans-serif;line-height:1.7;">Welcome to Wheels and Words, a place for stories, faith, humor, encouragement, and an honest look at life from a wheelchair. The road may not be the one I planned, but it's the one I'm on &mdash; and there's plenty to share along the way.</p>
                    <div style="margin-top:14px;color:var(--gold);font-size:14px;font-family:Arial,sans-serif;font-weight:bold;">Read More &rarr;</div>
                </div>
            </div>
        </a>

        <div style="text-align:center;padding:18px 0 28px;">
            <a href="https://wordsandwheels.net/blog/bob-s-thoughts" target="_blank" rel="noopener" class="hero-btn" style="font-size:14px;padding:10px 24px;">View All Bob's Thoughts</a>
        </div>

"""

path.write_text(text[:start] + cards + text[end:], encoding="utf-8")
print("Restored all currently published Bob's Thoughts cards")
