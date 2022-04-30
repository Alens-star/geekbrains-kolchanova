def user(name = "", surn = "",
         year = "", city = "",
         email = "", tel = ""):
    user_result = f"{name} {surn} {year} {city} {email} {tel}"
    return user_result
print(user(name="Света", tel="890765432"))
