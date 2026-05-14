import os

def generate_project_tree(startpath):
    print(f"Project Structure for: {os.path.abspath(startpath)}\n")
    for root, dirs, files in os.walk(startpath):
        # Ignore hidden folders like .ipynb_checkpoints, .git, or __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.startswith('.'): # Ignore hidden files
                print(f'{sub_indent}{f}')

if __name__ == "__main__":
    # Point this to your root directory
    generate_project_tree('./')