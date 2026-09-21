url = input("Enter URL: ")

if "@" in url:
    print("Warning: Suspicious URL")
elif not url.startswith("https://"):
    print("Warning: URL is not secure")
elif "login" in url or "verify" in url or "account" in url:
    print("Warning: Suspicious words found in URL")
elif len(url) > 75:
    print("Warning: URL is too long")
elif url.count(".") > 3:
    print("Warning: Too many dots in URL")
else:
    print("URL looks normal")
