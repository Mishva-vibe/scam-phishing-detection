url = input("Enter URL: ")

if "@" in url:
    print("Warning: Suspicious URL")
elif len(url) > 75:
    print("Warning: URL is too long")
elif url.count(".") > 3:
    print("Warning: Too many dots in URL")
else:
    print("URL looks normal")
