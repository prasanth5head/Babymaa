from pathlib import Path

root = Path(__file__).resolve().parent.parent
app = root / 'src' / 'App.jsx'
html = root / 'index.html'
text = app.read_text(encoding='utf-8')
repls = [
    ('Kuttymaa', 'Babymaa'),
    ('kuttymaa', 'babymaa'),
    ('story: "Happy Birthday, my love. Every memory leads right back to you.",', 'story: "My love. Every memory leads right back to you.",'),
    ("Click on any star in Kuttymaa's night sky to reveal a secret thought...", "Click on any star in Babymaa's night sky to reveal a secret thought..."),
    ('"Happy Birthday, Kuttymaa. 🎂",', '"For Babymaa, with all my love. 💖",'),
    ('Happy Birthday, Kuttymaa! ❤️', 'Forever yours, Babymaa! ❤️'),
    ('if (pw === "kuttymaa" || pw === "jessy" || pw === "kutty" || pw === "k" || pw === "j") {', 'if (pw === "babymaa" || pw === "jessy" || pw === "baby" || pw === "b" || pw === "j") {'),
    ('localStorage.setItem("kuttymaa_capsule", capsuleMessage);', 'localStorage.setItem("babymaa_capsule", capsuleMessage);'),
    ('const saved = localStorage.getItem("kuttymaa_capsule");', 'const saved = localStorage.getItem("babymaa_capsule");'),
    ('title: "Happy Birthday, Babymaa! 🎉",', 'title: "For Babymaa, my love! 🎉",'),
    ('title: "Today & Forever 🎂✨",', 'title: "Today & Forever ✨",'),
    ('On your birthday, I just want you to know how grateful I am for every moment, every memory, every challenge we\'ve overcome, and every smile we\'ve shared. Thank you for trusting me, for staying by my side, and for being the beautiful person you are.', 'On this special day, I just want you to know how grateful I am for every moment, every memory, every challenge we\'ve overcome, and every smile we\'ve shared. Thank you for trusting me, for staying by my side, and for being the beautiful person you are.'),
    ('title: "Happy Birthday, My Love. ❤️🎂✨",', 'title: "Forever Yours, My Love. ❤️✨",'),
    ('On your birthday, I want to promise you that no matter what storms come, I am holding your hand.', 'I want to promise you that no matter what storms come, I am holding your hand.'),
    ('Thank you for choosing me every single day. Happy Birthday, my love. ❤️', 'Thank you for choosing me every single day. Always yours, my love. ❤️'),
    ('{/* Final Chapter - Birthday */}', '{/* Final Chapter - Love */}'),
    ('Birthday Time Capsule', 'Love Time Capsule'),
    ('Write a message to your future self. I\'ll keep it locked away safely until your next birthday.', 'Write a message to your future self. I\'ll keep it locked away safely until our next surprise moment.'),
    ("Kuttymaa's Birthday Project", "Babymaa's Surprise Project"),
    ('Kuttymaa ❤️', 'Babymaa ❤️'),
]
for old, new in repls:
    text = text.replace(old, new)
app.write_text(text, encoding='utf-8')
html_text = html.read_text(encoding='utf-8')
html_text = html_text.replace('title>Happy Birthday My Love ❤️</title>', 'title>For My Lovely Girlfriend ❤️</title>')
html.write_text(html_text, encoding='utf-8')
print('Updated surprise text and title.')
