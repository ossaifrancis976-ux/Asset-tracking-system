assets = []

def add_asset():
    asset_name = input("Enter asset name: ")
    asset_id = input("Enter asset ID: ")
    location = input("Enter asset location: ")
    assets.append({
        "asset_name": asset_name,
        "asset_id": asset_id,
        "location": location
    })
    print("Asset added successfully")

def view_assets():
    if not assets:
        print("No assets recorded")
    else:
        for a in assets:
            print("Asset:", a["asset_name"])
            print("Asset ID:", a["asset_id"])
            print("Location:", a["location"])
            print("------------------")

def main():
    while True:
        print("1. Add Asset")
        print("2. View Assets")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_asset()
        elif choice == "2":
            view_assets()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
