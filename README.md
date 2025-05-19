# A Text-Based Game with Python

### **Day 1: The Infinite Chatbot**  
**Goal:** Create a loop that reacts to user input until they say "quit".  
**Instructions:**  
1. Use a `while True` loop.  
2. Ask the user for input.  
3. If they type "quit", exit the loop.  
4. For any other input, echo it back (e.g., "You said: [input]").  
**Stretch Goal:** Add 3 custom responses (e.g., "hello" → "Hi!").  
**Debug Challenge:** What happens if the user types "QUIT" instead of "quit"?  

---

### **Day 2: The Hungry Pet Simulator**  
**Goal:** Add a *hunger system* to the chatbot.  
**Instructions:**  
1. Track a `hunger` variable starting at 0.  
2. Every loop iteration, increase hunger by 1.  
3. If the user types "feed", decrease hunger by 2.  
4. Print hunger status each turn (e.g., "Hunger: 5/10").  
5. If hunger reaches 10, end the game with "Your pet ran away!"  
**Stretch Goal:** Prevent hunger from going below 0.  
**Worksheet Q:** Why does `hunger` need `max(0, hunger)` after feeding?  

---

### **Day 3: The Locked Door Puzzle**  
**Goal:** Add an *inventory system* and conditional progression.  
**Instructions:**  
1. Add a `has_key = False` variable.  
2. If the user types "look", set `has_key = True`.  
3. If they type "use key" and `has_key` is True:  
   - Print "You unlocked the door!"  
   - End the loop.  
4. If they type "use key" without the key:  
   - Print "You don’t have a key!"  
**Stretch Goal:** Add a "check inventory" command.  
**Debug Challenge:** Why doesn’t "Use Key" (uppercase) work?  

---

### **Day 4: The Time Bomb**  
**Goal:** Add a *real-time countdown* using `time.time()`.  
**Instructions:**  
1. Import the `time` module.  
2. Set a 10-second timer with `start_time = time.time()`.  
3. Every loop iteration, calculate elapsed time.  
4. If time runs out: print "💥 BOOM!" and end the game.  
5. Let the user "cut red" or "cut blue" wire to defuse the bomb.  
   - Red wire: Only works in the first 5 seconds.  
   - Blue wire: Only works after 5 seconds.  
**Worksheet Q:** Why use `time.time()` instead of counting loop iterations?  

---

### **Day 5: The Dungeon Crawler**  
**Goal:** Combine all systems into one game.  
**Instructions:**  
1. **Rooms:** Create 3 rooms (start, treasure, monster).  
2. **Health:** Start with 10 HP. Monsters reduce health.  
3. **Inventory:** Collect a sword to fight monsters.  
4. **Time Pressure:** A ghost slowly approaches (hunger-style timer).  
5. **Win Condition:** Find treasure before time/health runs out.  
**Stretch Goals:**  
- Add a "map" command showing visited rooms.  
- Let the user name their character.  
**Final Challenge:** Merge code from Days 1-4 into this project.  

--- 

### **Rules for All Days:**  
1. **No Copy-Pasting Code:** Type everything from scratch.  
2. **Test Small:** After each feature, run the code to see if it breaks.  
3. **Debugging Mantra:**  
   - What did I expect to happen?  
   - What actually happened?  
   - What’s the smallest change that fixes it?  

### **Final Deliverable (Day 5):**  
A single Python file with:  
- An event loop handling:  
  - User commands  
  - Game state (health, inventory, time)  
  - Conditional progression (rooms, win/lose)  
- At least 3 stretch goals implemented.  
