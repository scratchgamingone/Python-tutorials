import os

# Your variable containing the output
password_output = "ThisIsMySecurePassword123!"

# Define the folder and file paths
folder_name = "password"
file_name = "output.txt"

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Define the full file path
file_path = os.path.join(folder_name, file_name)

# Save the output to the file
with open(file_path, "w") as file:
    file.write(password_output)

print(f"Password saved to {file_path}")
