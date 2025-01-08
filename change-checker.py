import os
import git

repo = git.Repo('.')
changed = False

# Get the diff between two commits/tags
# Replace 'old_commit' and 'new_commit' with your commit hashes or tag names
diff = repo.git.diff('old_commit', 'new_commit', '--', 'entri/ui/static_design_revamp/north_south/sass/')

if diff:
    # Changes exist in the directory
    print("There are changes in the sass directory between commits:")
    
    # Parse diff output to show specific changes
    for line in diff.split('\n'):
        if line.startswith('diff --git'):
            file_path = line.split(' b/')[1]
            print(f"Changed: {file_path}")
            changed = True

if not changed:
    print("No changes detected in the sass directory between commits")
