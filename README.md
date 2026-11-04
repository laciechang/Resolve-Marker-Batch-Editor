# Resolve-Marker-Batch-Editor

# 🔧 Installation

- Please copy *Marker_Batch_Editor_v1 ENG.py* into DaVinci Resolve’s designated scripts folder.

    Mac OS X: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts
  
    Windows: %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts
  
    Linux: /opt/resolve/Fusion/Scripts  (or /home/resolve/Fusion/Scripts/ depending on installation)
  
- Use DaVinci Resolve v17.2 or above.

- You can find it in the menu: Workspace > Scripts.

- Can only be used inside DaVinci Resolve, not as an external script.

# 🎛 Usage

- The tool provides *replacement for marker color, marker name, and marker note*, as well as *delete by marker color*.

- Usage is similar to most system “Find/Replace” functions: the left input field is “Find”, the right one is “Replace”.

- Supports regular expressions*.

- To switch to regex mode, when both left and right input fields are empty, click the Edit button on the right.

- If you drag the bottom of the window to increase its height, you will see a hidden Restore button, which can revert all mistakenly modified markers back to the state when you opened this tool.

# 🧷 Tips

To delete specific content, simply leave the right target field empty.

# ☝️ Requirements

- Python 3.6 64-bit  
- Other Python versions are not supported by DaVinci Resolve.
