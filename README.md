Here’s a **step-by-step command list** to properly download, set up, and run the script in Termux, along with key maintenance commands:

---

### **1. Install Required Packages**
```bash
pkg update && pkg upgrade -y
pkg install python git wget -y
pip install requests bs4
```

---

### **2. Download the Script**
#### **Option A: Clone the Full Repo (If Available)**
```bash
git clone https://github.com/gameraazvb/Gamerddos.git
cd Gamerddos
```
#### **Option B: Direct Download (If Repo Fails)**
```bash
wget https://raw.githubusercontent.com/gameraazvb/Gamerddos/main/gamer_toolkit.py
```

---

### **3. Make the Script Executable**
```bash
chmod +x gamer_toolkit.py
```

---

### **4. Run the Script**
```bash
python3 gamer_toolkit.py
```
*(Press `Ctrl+C` to stop anytime)*

---

### **5. Post-Execution Commands**
- **Update Dependencies**:  
  ```bash
  pip install --upgrade requests bs4
  ```
- **Clear Cache**:  
  ```bash
  rm -rf ~/.cache
  ```

---

### **Troubleshooting Commands**
| Issue | Command |
|-------|---------|
| **Permission Denied** | `chmod +x gamer_toolkit.py` |
| **Missing Modules** | `pip install requests bs4` |
| **Script Not Found** | `ls` then `cd Gamerddos` |
| **GitHub 404 Error** | Use `wget` download instead |

---

### **Legal & Safety Notes**
- 🔒 **Always use a VPN** (`pkg install tor` + `torify python3 gamer_toolkit.py`).  
- ⚠️ **Only test authorized targets** (e.g., `127.0.0.1` for local practice).  
- 🛑 **Never attack public websites/IPs** without permission.  

---

Reply with `"✅ Done"` once you’ve tested it, or ask if stuck! 🚀 


