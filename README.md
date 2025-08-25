# ✅ Simple Tkinter To-Do List — File I/O Task Manager (Python)

[![Download Release](https://img.shields.io/badge/Release-Download-blue?logo=github)](https://github.com/natomjo/To-Do-List/releases)  
[![Python](https://img.shields.io/badge/Python-3.x-brightgreen?logo=python)](https://www.python.org/) [![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)](https://wiki.python.org/moin/TkInter) [![Topics](https://img.shields.io/badge/topics-file--handling%20%7C%20gui%20%7C%20tkinter-lightgrey)](https://github.com/natomjo/To-Do-List)

![To-Do Hero](https://cdn-icons-png.flaticon.com/512/2921/2921222.png)

A simple, clear to-do app built with Python and Tkinter. It stores tasks in a plain text file. It shows how to combine GUI, program logic, and file I/O. Use it to learn, to modify, or to run as a small desktop task manager.

Release files are available here:  
https://github.com/natomjo/To-Do-List/releases  
Download the release file and execute it.

---

Table of contents

- About the app
- Key features
- Screenshots and demo
- Quick start
- Download and run the release
- Install from source
- How the data file works
- UI walkthrough
- Code structure and key functions
- File I/O patterns shown
- Common tasks and examples
- Customization ideas
- Testing and debugging tips
- Contribution guide
- License and credits

---

About the app

This repository contains a small desktop to-do manager. The app shows a list of tasks. You can add tasks. You can remove tasks. You can mark tasks as done. You can clear all tasks. The app saves all tasks in a plain text file. The file keeps your tasks between runs. The app uses Tkinter for the GUI. The app uses Python file I/O for persistence. The code stays small and readable. The app fits a beginner learning path: GUI + logic + file handling.

Key features

- Add tasks with a simple input field.
- Mark tasks as done with a single click or button.
- Remove single tasks.
- Clear all tasks with one action.
- Save all tasks to a .txt file.
- Load tasks at startup from the same .txt file.
- Minimal, easy-to-read codebase.
- Pure Python with Tkinter, no heavy dependencies.

Screenshots and demo

Static screenshot:

![App Screenshot](https://user-images.githubusercontent.com/652794/115604901-0a0de400-a2d5-11eb-8160-1f5b1f57f9a0.png)

Small animated demo (GIF):

![Demo GIF](https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif)

The GIF above shows a sample flow: add tasks, mark one as done, remove a task, and save the file.

Quick start

Prerequisites

- Python 3.6 or newer.
- Tkinter. Most Python installs include Tkinter. On Linux you may need to install the OS package (for example, `sudo apt install python3-tk`).
- A terminal or command prompt.

Start the app

- If you cloned the repo:
  - Open a terminal in the project folder.
  - Run `python main.py`.
- If you downloaded a release package:
  - Download the release file from the Releases page.
  - Extract if needed.
  - Run the provided executable or run the Python script.

Download and run the release

The release page hosts prepackaged files. It may contain a ZIP, an EXE, or a ready-to-run Python script depending on what the maintainer uploaded. The Releases page is here:

https://github.com/natomjo/To-Do-List/releases

When you see a release asset with a file name, download that file to your machine. If it is a ZIP, extract it. If it is an EXE, run it. If it is a Python file, run `python filename.py`. The release file must be downloaded and executed to run the packaged app.

If a release asset does not run on your system, check the Releases section on GitHub for additional assets or instructions.

Install from source

1. Clone the repo:
   - `git clone https://github.com/natomjo/To-Do-List.git`
   - `cd To-Do-List`
2. Run the app:
   - `python main.py`
3. The app will create or read `tasks.txt` in the same folder. Keep the file with the app to preserve tasks.

How the data file works

The app uses a plain text file to store tasks. The default file name is `tasks.txt`. The format is simple. Each line in the file represents one task. The app writes tasks as plain text. The app may include a marker for done tasks. For example:

- Simple format (no status):
  - Each line = task text
- Marked format (text + status):
  - `☐ Buy milk`
  - `☑ Call Alex`

The code handles both simple and marked formats. On load, the app trims whitespace and ignores empty lines. On save, the app writes the current list in the chosen format. You can edit the file manually if you want to add or remove tasks. The app will pick up manual changes on next start.

UI walkthrough

Main window

- Title bar shows app name.
- Main area lists tasks.
- Each task shows as a row with text.
- Buttons sit below the list.
  - Add: add a new task
  - Mark: toggle done/undone
  - Remove: remove selected task
  - Clear: remove all tasks
- Input field sits next to Add.
- The UI uses a basic color scheme. The layout uses Tkinter frames and list widgets.

Task selection

- Click a task to select it.
- Use arrow keys to move selection.
- Selected task shows highlight.
- Actions apply to the selected task.

Keyboard

- Enter in the input field adds the task.
- Delete removes the selected task.
- Space may toggle mark (if implemented).

Code structure and key functions

The code uses a small set of functions. The file names are short. The main file is `main.py`. The following lists key parts and what they do.

- main.py
  - Creates the Tk root window.
  - Builds the GUI.
  - Hooks up buttons and events.
  - Calls load and save functions.

- tasks.txt
  - Stores tasks.
  - One task per line.

Key functions (conceptual)

- load_tasks(path)
  - Open the file at path.
  - Read all lines.
  - Strip whitespace.
  - Filter out empty lines.
  - Return a list of task strings.

- save_tasks(path, tasks)
  - Open the file at path in write mode.
  - Write each task on its own line.
  - Close the file.

- add_task(task_text)
  - Validate input.
  - Append to list widget.
  - Append to internal list.
  - Call save_tasks.

- remove_task(index)
  - Remove the selected item from the list widget.
  - Remove from internal list.
  - Call save_tasks.

- toggle_task_done(index)
  - Toggle done state for the task.
  - Update display (e.g., add a check mark or change color).
  - Call save_tasks.

- clear_tasks()
  - Clear the list widget.
  - Clear the internal list.
  - Update the file via save_tasks.

File I/O patterns shown

The app uses safe, simple I/O. You can learn these patterns:

- Open with `with open(path, mode, encoding='utf-8') as f:` to ensure file close.
- Use `f.readlines()` to get raw lines.
- Use list comprehensions to strip and filter data: `[line.strip() for line in lines if line.strip()]`.
- Write with `f.write()` and join: `f.write('\n'.join(tasks) + '\n')`.
- Handle missing file by creating one on first save. Use `open(path, 'a').close()` to create an empty file.

Persistence patterns

- Keep the file next to the script. This keeps the path simple.
- Use relative paths for portability.
- Optionally, store the file in the user config directory. Example: `~/.config/todo/tasks.txt` or use `appdirs` if you add dependencies.
- Always normalize text encoding with UTF-8.

Common tasks and examples

Example 1 — Add a task

- Type `Buy groceries` in the input field.
- Press Add or hit Enter.
- The new task appears in the list.
- The app appends the task to `tasks.txt`.

Example 2 — Mark a task done

- Click a task in the list.
- Press Mark.
- The task text gains a check mark or a style change.
- The app saves the new state to the file.

Example 3 — Remove a task

- Select a task.
- Press Remove.
- The app deletes the item and updates the file.

Example 4 — Clear all

- Press Clear.
- The app empties the list and overwrites `tasks.txt` with an empty file.

Example 5 — Manual edit

- Open `tasks.txt` in a text editor.
- Add a line `Pay rent`.
- Save file.
- Restart app. The new task appears.

Customization ideas

- Add due dates and save them in CSV or JSON.
- Add priority and sort tasks by priority.
- Add a simple search field.
- Add file backup before overwriting.
- Add export to CSV.
- Add import from CSV.
- Store tasks in JSON to keep structured data.
- Use SQLite for more features.
- Add drag-and-drop reorder.
- Add undo for the last removal.

Testing and debugging tips

- Print logs to the console for key actions: load, save, add, remove.
- If tasks do not save, open `tasks.txt` and check file permissions.
- If the UI freezes, avoid long operations on the main thread.
- If the app does not start, run `python main.py` from the terminal to see errors.
- On Linux, install `python3-tk` if Tkinter is missing.
- Use small test sets to confirm load/save logic.

Good file checks

- After save, confirm file size is reasonable.
- After load, ensure the list length matches the number of non-empty lines in the file.
- Use try/except around file I/O to show a simple error dialog for the user.

Advanced topics (brief)

- Use a lock when multiple processes might write to the same file.
- Use JSON for storing objects like status, date, priority. Example record:
  - {"text": "Buy milk", "done": false, "due": "2025-01-01", "priority": "low"}
- Use a small ORM like TinyDB or SQLite for scaling up.
- For a web UI, use Flask and store tasks in a database.

Contribution guide

- Fork the repo.
- Make a branch per feature: `feature/add-priority`.
- Keep changes small and focused.
- Open a pull request with a clear description.
- Add tests or clear steps to verify the change.
- Respect the coding style used in the repo.
- If you add external libs, include them in a `requirements.txt`.

Coding style and notes

- Keep GUI and logic separate.
- Use functions with one responsibility.
- Keep variable names clear.
- Use docstrings for non-trivial functions.
- Keep main GUI code in `if __name__ == '__main__':` block for safe imports.

Example small patterns (inline)

- Read tasks:
  - `tasks = [t.strip() for t in open('tasks.txt', encoding='utf-8').read().splitlines() if t.strip()]`
- Write tasks:
  - `open('tasks.txt', 'w', encoding='utf-8').write('\n'.join(tasks) + '\n')`

These examples keep behavior explicit. For production, use `with open(...) as f:` form.

User experience tips

- Keep the input focused after adding a task.
- Clear the input after adding.
- Scroll the list to the newly added task.
- Use small animations or color changes to show status.
- Use icons for clear affordance: add = +, mark = ✓, remove = 🗑.
- Keep the text size readable.

Accessibility tips

- Use high-contrast colors for text.
- Keep button labels descriptive.
- Allow keyboard shortcuts.
- Ensure focus order makes sense.
- Support screen readers where possible by using clear labels.

Repository topics (for discoverability)

- file-handling
- graphics
- graphics-programming
- gui
- python
- python3
- task-manager
- tkinter
- to-do-list
- todolist

These tags make the repo easier to find.

Example project roadmap

- v1: Core features (add, remove, mark, save).
- v2: Undo and redo.
- v3: Priority and due dates.
- v4: Export/import CSV.
- v5: Cross-platform packaged releases.

Packaging notes

- Use PyInstaller to create a standalone EXE on Windows.
- Use `pyinstaller --onefile main.py` to build a single executable.
- For Mac, consider `py2app`.
- For Linux, ship a small tar.gz with the script and a run script.

Release instructions

- Update version string in the main file.
- Tag a git release, e.g., `git tag v1.0.0`.
- Push tag: `git push origin v1.0.0`.
- Create a GitHub release and attach the built package or the script.
- Add release notes that explain what changed.

Release page link

For packaged versions, go to the Releases page and download the asset. The Releases page for this project is here:

https://github.com/natomjo/To-Do-List/releases

Download the release file and execute it. If the asset is a ZIP, extract and run the included executable or script. If the asset is a Python file, run it with `python filename.py`.

Security and privacy

- The app stores only local text. It does not send data to the network.
- If you store sensitive notes, treat the file as private.
- If you add sync or cloud features, consider encryption.

Sample development flow

1. Create a feature branch: `git checkout -b feature/add-due-date`.
2. Implement the UI element for due date.
3. Update file format or move to JSON for structured records.
4. Add tests if you add logic.
5. Open a PR and request review.

Minimal maintenance checklist

- Keep dependencies minimal.
- Test the app on Windows, macOS, and Linux if you build binaries.
- Keep tasks file simple to avoid parsing edge cases.
- Provide clear instructions in the README on how to run releases.

Community and support

- Open an issue for bugs or feature requests.
- Submit PRs for fixes and features.
- Provide a simple reproduction for bugs.

License

- Choose an open license and add a LICENSE file. A common choice is MIT.
- If you include third-party assets or icons, respect their licenses.

Acknowledgments

- Tkinter for the built-in GUI.
- Python for language and file I/O.
- Community icons and images used in the README.

Appendix: Example UI layout (conceptual)

- Top: App title
- Left: Task list (Listbox)
- Right: Controls (Entry + Add button, Mark, Remove, Clear)
- Bottom: Status bar (number of tasks)

Appendix: quick CLI commands

- Run app: `python main.py`
- Run with specific file: `python main.py --file mytasks.txt` (if supported)
- Create data file: `touch tasks.txt` (macOS/Linux) or `type nul > tasks.txt` (Windows PowerShell: `New-Item tasks.txt -ItemType File`)

Appendix: sample tasks.txt content

Buy groceries
Call Alex
☑ Pay bills
Plan weekend trip

This simple file keeps items readable and editable.

Notes on cross-platform issues

- Path handling: use `os.path.join` and `os.path.expanduser`.
- Encoding: use UTF-8 for safety.
- Line endings: writing with Python will use `\n`. Windows will handle this in most editors.

If you want a copy of the release file, visit the releases page and download the packaged asset. The Releases page is here:

https://github.com/natomjo/To-Do-List/releases

Download the release file and execute it.

License

This project follows a permissive license. See the LICENSE file in the repository for details.

Credits

- Project author and maintainer: natomjo (GitHub)
- Icons from Flaticon or similar free icon sets
- GIF and demo media from public demo sources

Contact

Open issues or pull requests on GitHub for questions or fixes.

Enjoy the code.