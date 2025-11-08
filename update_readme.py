import os
import re

SOLUTIONS_FOLDER = "solutions"

BADGE_STYLE = "flat-square"
LOGO_COLOR = {
    "hackerrank": "2EC866",
    "Python": "3776AB",
    "Java": "007396",
    "JavaScript": "F7DF1E",
    "TypeScript": "3178C6",
    "C": "555555",
    "C++": "00599C",
    "C#": "9B4F96",
}

LANGUAGE_EXTENSIONS = {
    "Python": [".py"],
    "Java": [".java"],
    "JavaScript": [".js"],
    "TypeScript": [".ts"],
    "C": [".c"],
    "C++": [".cpp", ".cc", ".cxx"],
    "C#": [".cs"]
}

def count_solutions_by_language():
    counts = {lang: 0 for lang in LANGUAGE_EXTENSIONS}
    
    for root, _, files in os.walk(SOLUTIONS_FOLDER):
        for file in files:
            for lang, exts in LANGUAGE_EXTENSIONS.items():
                if any(file.endswith(ext) for ext in exts):
                    counts[lang] += 1
                    break
    return counts

def count_total_solutions():
    total = 0
    for root, _, files in os.walk(SOLUTIONS_FOLDER):
        for file in files:
            if any(file.endswith(ext) for exts in LANGUAGE_EXTENSIONS.values() for ext in exts):
                total += 1
    return total

def generate_badges(counts, total):
    return {
        "progress": f"https://img.shields.io/badge/HackerRank%20Solutions-{total}-{LOGO_COLOR['hackerrank']}?style={BADGE_STYLE}&logo=hackerrank",
        "Python": f"https://img.shields.io/badge/Python-{counts['Python']}%20solutions-{LOGO_COLOR['Python']}?style={BADGE_STYLE}&logo=python",
        "Java": f"https://img.shields.io/badge/Java-{counts['Java']}%20solutions-{LOGO_COLOR['Java']}?style={BADGE_STYLE}&logo=java",
        "JavaScript": f"https://img.shields.io/badge/JavaScript-{counts['JavaScript']}%20solutions-{LOGO_COLOR['JavaScript']}?style={BADGE_STYLE}&logo=javascript",
        "TypeScript": f"https://img.shields.io/badge/TypeScript-{counts['TypeScript']}%20solutions-{LOGO_COLOR['TypeScript']}?style={BADGE_STYLE}&logo=typescript",
        "C": f"https://img.shields.io/badge/C-{counts['C']}%20solutions-{LOGO_COLOR['C']}?style={BADGE_STYLE}&logo=c",
        "C++": f"https://img.shields.io/badge/C%2B%2B-{counts['C++']}%20solutions-{LOGO_COLOR['C++']}?style={BADGE_STYLE}&logo=cplusplus",
        "C#": f"https://img.shields.io/badge/C%23-{counts['C#']}%20solutions-{LOGO_COLOR['C#']}?style={BADGE_STYLE}&logo=csharp",
    }

def update_readme(badges):
    readme_template = '''<div align="center">
  <h1>👨‍💻 HackerRank Solutions</h1>
  
  Solutions to [HackerRank](https://www.hackerrank.com/domains/algorithms) problems
  
  ---
  
  ![HackerRank Progress]({progress})
  <br/>
  ![Python]({Python})
  ![Java]({Java})
  ![JavaScript]({JavaScript})
  ![TypeScript]({TypeScript})
  <br/>
  ![C]({C})
  ![C++]({C++})
  ![C#]({C#})
  
  ---
</div>

## ✨ Features
- ✅ Clean & optimized solutions
- ✅ Multiple programming language solutions
- ✅ Well-documented code
- ✅ Perfect for interview preparation

## 🗂️ Solution Categories
- **Contest Solutions**: Competition and contest solutions
- **Python Solutions**: Python language specific problems
- **Java Solutions**: Java language specific problems

## 👨‍💻 Author
**Tamim Ahasan Rijon**  
📧 [tamimahasan.ar@gmail.com](mailto:tamimahasan.ar@gmail.com)  
🌐 [Portfolio](https://tamim-ar.netlify.app/)  
🔗 [LinkedIn](https://www.linkedin.com/in/tamim-ar/) • [GitHub](https://github.com/tamim-ar) • [X/Twitter](https://x.com/tamim__ahasan)  
📷 [Instagram](https://www.instagram.com/tamim__ahasan/) • [Facebook](https://www.facebook.com/hellotamim/)

## 🤝 Contributing
Contributions are welcome! 🚀  
To add or improve solutions:
1. **Fork** this repository  
2. Create a feature branch → `git checkout -b feature/your-feature`  
3. Commit changes → `git commit -m 'Add feature'`  
4. Push to your branch → `git push origin feature/your-feature`  
5. Open a **Pull Request** 🎯

## 📜 License
Licensed under the [MIT License](./LICENSE).
'''
    content = readme_template.format(**badges)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    counts = count_solutions_by_language()
    total = count_total_solutions()
    badges = generate_badges(counts, total)
    update_readme(badges)

    print("\n🚀 README Badges Updated Successfully!\n")
    print(f"📊 Total Solutions: {total}\n")
    print("📌 Solutions by Language:")
    for lang, count in counts.items():
        if count > 0:
            print(f"   • {lang:<10}: {count} solutions")
    print("\n✅ Done!\n")