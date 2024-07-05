file_name = input("File name: ").strip().lower()
if '.' in file_name:
    if file_name.count(".") == 1:
        fname, fext = file_name.split('.')
    else:
        fname, fext = [file_name.split('.')[i] for i in (0, -1)]

    match fext:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "gif":
            print("image/gif")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

else:
    print("application/octet-stream")
