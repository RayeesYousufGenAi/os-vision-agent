import time
import os
import sys
from dotenv import load_dotenv
from vision import capture_screen, get_action_from_vision
from actions import click_at, type_string, press_key, get_screen_size

load_dotenv()

def run_agent(goal, max_steps=10):
    print(f"🚀 Starting OS-Vision-Agent with goal: {goal}")
    print("--------------------------------------------------")
    
    screen_w, screen_h = get_screen_size()
    print(f"🖥️ Detected Screen Resolution: {screen_w}x{screen_h}")

    for step in range(1, max_steps + 1):
        print(f"\n[Step {step}/{max_steps}] Thinking...")
        
        # 1. Capture and analyze the screen
        screenshot_path, _, _ = capture_screen()
        try:
            result = get_action_from_vision(screenshot_path, goal)
        except Exception as e:
            print(f"❌ Error during vision processing: {e}")
            break

        reasoning = result.get("reasoning", "No reasoning provided.")
        action = result.get("action", "wait")
        params = result.get("params", {})
        status = result.get("status", "in_progress")

        print(f"🧠 Reasoning: {reasoning}")
        print(f"🎬 Action: {action.upper()} | Params: {params}")

        # 2. Execute the action
        if action == "click" or action == "double_click":
            # Map 0-1000 normalized coordinates to actual screen pixels
            target_x = int((params.get("x", 0) / 1000) * screen_w)
            target_y = int((params.get("y", 0) / 1000) * screen_h)
            click_at(target_x, target_y, double=(action == "double_click"))
        
        elif action == "type":
            type_string(params.get("text", ""))
        
        elif action == "press":
            press_key(params.get("key", "enter"))
        
        elif action == "wait":
            print("⏳ Waiting for 2 seconds...")
            time.sleep(2)

        # 3. Check if completed
        if status == "completed":
            print("\n✅ Goal achieved! Terminating session.")
            break
        
        time.sleep(1) # Small delay between actions

    print("\n--------------------------------------------------")
    print("🏁 Agent Finished.")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in .env file.")
        sys.exit(1)

    user_goal = input("Enter your goal for the OS-Vision-Agent: ")
    if user_goal:
        run_agent(user_goal)
    else:
        print("No goal provided. Exiting.")
