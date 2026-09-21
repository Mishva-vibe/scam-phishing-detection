url = input("Enter URL: ")

score = 0

if "@" in url:
    score += 1

if not url.startswith("https://"):
    score += 1

if any(word in url.lower() for word in ["login", "verify", "account", "bank", "password"]):
    score += 1

if len(url) > 75:
    score += 1

if url.count(".") > 3:
    score += 1

percentage = (score / 5) * 100

print("Phishing Risk:", percentage, "%")

if percentage >= 60:
    print("Warning: URL may be suspicious")
else:
    print("URL looks normal")
