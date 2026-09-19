url = input("Enter URL: ")

if "@" in url:
    print("Warning: Suspicious URL")
elif len(url) > 75:
    print("Warning: URL is too long")
else:
    print("URL looks normal")
