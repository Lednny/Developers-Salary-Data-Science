import kagglehub

# Download latest version
path = kagglehub.dataset_download("emreksz/software-engineer-jobs-and-salaries-2024")

print("Path to dataset files:", path)
