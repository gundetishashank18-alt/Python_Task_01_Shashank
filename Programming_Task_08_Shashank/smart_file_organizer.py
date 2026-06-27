import os
import shutil
from collections import Counter
from datetime import datetime

class SmartFileOrganizer:

    def __init__(self):
        self.file_types = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
            "Audio": [".mp3", ".wav", ".aac", ".flac"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Programs": [".exe", ".msi", ".py", ".java", ".c", ".cpp", ".html", ".css", ".js"]
        }

        self.stats = Counter()
        self.duplicates = []

    def get_category(self, extension):
        extension = extension.lower()
        for category, extensions in self.file_types.items():
            if extension in extensions:
                return category
        return "Others"

    def scan_files(self, folder):
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

        print("\nTotal Files:", len(files))
        print("-" * 40)

        for file in files:
            print(file)

        return files

    def organize_files(self, folder, files):
        for file in files:
            source = os.path.join(folder, file)
            ext = os.path.splitext(file)[1]
            category = self.get_category(ext)

            destination_folder = os.path.join(folder, category)
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(destination_folder, file)

            try:
                shutil.move(source, destination)
                self.stats[category] += 1
            except shutil.Error:
                print(f"File already exists: {file}")
            except Exception as e:
                print(e)

    def search(self, folder):
        print("\nSearch Options")
        print("1. File Name")
        print("2. Extension")

        choice = input("Enter choice: ")

        if choice == "1":
            keyword = input("Enter file name: ").lower()

            for root, dirs, files in os.walk(folder):
                for file in files:
                    if keyword in file.lower():
                        print(os.path.join(root, file))

        elif choice == "2":
            ext = input("Enter extension (example .pdf): ").lower()

            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(ext):
                        print(os.path.join(root, file))

    def find_duplicates(self, folder):
        names = []

        for root, dirs, files in os.walk(folder):
            for file in files:
                names.append(file)

        count = Counter(names)

        self.duplicates = [name for name, c in count.items() if c > 1]

        if self.duplicates:
            print("\nDuplicate Files:")
            for file in self.duplicates:
                print(file)
        else:
            print("\nNo Duplicate Files Found")

    def show_statistics(self):
        print("\nFile Statistics")
        print("-" * 30)

        total = sum(self.stats.values())

        print(f"Total Files : {total}")

        for category in [
            "Images",
            "Documents",
            "Videos",
            "Audio",
            "Archives",
            "Programs",
            "Others",
        ]:
            print(f"{category:<12}: {self.stats[category]}")

    def generate_report(self, folder):
        report = os.path.join(folder, "file_report.txt")

        with open(report, "w") as f:
            f.write("SMART FILE ORGANIZER REPORT\n")
            f.write("=" * 40 + "\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Folder: {folder}\n\n")

            total = sum(self.stats.values())

            f.write(f"Total Files: {total}\n\n")

            f.write("Category Wise Count\n")
            for category in self.stats:
                f.write(f"{category}: {self.stats[category]}\n")

            f.write("\nDuplicate Files\n")

            if self.duplicates:
                for file in self.duplicates:
                    f.write(file + "\n")
            else:
                f.write("No Duplicate Files\n")

            f.write("\nFolder Structure\n")

            for root, dirs, files in os.walk(folder):
                level = root.replace(folder, "").count(os.sep)
                indent = " " * 4 * level
                f.write(f"{indent}{os.path.basename(root)}/\n")

                for file in files:
                    f.write(f"{indent}    {file}\n")

        print("\nReport Generated Successfully!")

def main():

    folder = input("Enter Folder Path: ").strip()

    if not os.path.exists(folder):
        print("Invalid Folder Path")
        return

    organizer = SmartFileOrganizer()

    files = organizer.scan_files(folder)

    organizer.find_duplicates(folder)

    organizer.organize_files(folder, files)

    organizer.show_statistics()

    organizer.search(folder)

    organizer.generate_report(folder)

if __name__ == "__main__":
    main()