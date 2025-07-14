def copy_image(source_path,destination_path):
    try:
        with open(source_path,"rb") as source_file,open(destination_path,"wb") as dest_file:
            while True:
                chunk = source_file.read(1024)
                if not chunk:
                    break
                dest_file.write(chunk)
        print(f"{source_path} copied successfully to {destination_path}")
    except FileNotFoundError:
        print(f"{source_path} not found")
    except Exception as e:
        print(f"Found some error: {e}")
copy_image("py1.PNG","new.PNG")
        