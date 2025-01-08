import os
import git

repo = git.Repo('.')
changed = False

# Get the diff between HEAD and specified commit/tag
diff = repo.git.diff('HEAD', 'ef27661bc4c4f03ca9a95d55091ed28df705eba4', '--', 'entri/ui/static_design_revamp/north_south/sass/')

if diff:
    # Changes exist in the directory
    print("There are changes in the sass directory between HEAD and specified commit:")
    
    # Parse diff output to show specific changes
    for line in diff.split('\n'):
        if line.startswith('diff --git'):
            file_path = line.split(' b/')[1]
            print(f"Changed: {file_path}")
            changed = True

if not changed:
    print("No changes detected in the sass directory between HEAD and specified commit")
