
---

# **WebChecker**  

## **Project Setup**  

This project uses a **virtual environment** to manage dependencies. The setup process included:  

1. **Creating a virtual environment**:  
   ```sh
   python3 -m venv .venv
   ```  
2. **Activating the virtual environment**:  
   - On macOS/Linux:  
     ```sh
     source .venv/bin/activate
     ```  
   - On Windows:  
     ```sh
     .venv\Scripts\activate
     ```  

3. **Installing required dependencies**:  
   ```sh
   pip install -r requirements.txt
   ```  

## **Challenges Faced**  

1. **Missing `openpyxl` module**  
   - Error:  
     ```sh
     ModuleNotFoundError: No module named 'openpyxl'
     ```  
   - Solution: Installed `openpyxl` using:  
     ```sh
     pip install openpyxl
     ```  

2. **Git push rejected due to remote updates**  
   - Error:  
     ```sh
     ! [rejected] main -> main (fetch first)
     error: failed to push some refs
     ```  
   - Solution: Pulled the latest changes first:  
     ```sh
     git pull --rebase origin main
     ```  
   - Then successfully pushed the code:  
     ```sh
     git push origin main
     ```  

## **How to Run the Script**  
Ensure the virtual environment is activated, then run:  
```sh
python script.py
```  

---

### **Created with ❤️ by Redvey**  

---

