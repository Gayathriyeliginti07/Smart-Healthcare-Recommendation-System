import pickle

# Open the file in binary read mode
with open("svc.pkl", "rb") as file:
    try:
        data = pickle.load(file)
        print("File Loaded Successfully ✅")
        print("Type of Data Inside:", type(data))
        print("\nFile Contents:\n", data)
    except Exception as e:
        print("Error:", e)
