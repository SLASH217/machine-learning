import pickle

# 1. The data we want to save (a standard Python dictionary)
user_profile = {"username": "admin", "access_level": 5, "active": True}

# 2. Saving (Serialization)
# 'wb' stands for Write Binary
with open("profile.pkl", "wb") as file:
    pickle.dump(user_profile, file)
print("Pickle: Saved successfully!")

# 3. Loading (Deserialization)
# 'rb' stands for Read Binary
with open("profile.pkl", "rb") as file:
    loaded_profile = pickle.load(file)

print(f"Pickle: Loaded profile for {loaded_profile['username']}")
