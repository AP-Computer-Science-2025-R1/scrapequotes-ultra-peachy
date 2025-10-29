# --- Function for Student E ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.
def get_random_quote(quotes):
    if not quotes:
         print("No quotes available.")
        return
    random_quote = random.choice(quotes)
    print(random_quote)












# ==================================
# SECTION 3: MAIN PROGRAM
# ==================================


# Team Lead/Integrator: Write the main logic here that calls the functions.
if __name__ == "__main__":
