from huggingface_hub import HfApi

api = HfApi()
repo_files = api.list_repo_files("paraphrase-multilingual-MiniLM-L12-v2", repo_type="model")
print("Model files:")
for file in repo_files:
    print(file)