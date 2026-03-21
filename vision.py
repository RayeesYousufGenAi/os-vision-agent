import os
import base64
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def capture_screen(filename="screenshot.png", max_size=(1024, 1024)):
    """Captures the screen and resizes it for the Vision LLM."""
    import pyautogui
    screenshot = pyautogui.screenshot()
    
    # Save original size for scaling back coordinates later
    orig_w, orig_h = screenshot.size
    
    # Resize to stay within LLM token limits and improve speed
    screenshot.thumbnail(max_size, Image.Resampling.LANCZOS)
    screenshot.save(filename)
    
    return filename, orig_w, orig_h

def encode_image(image_path):
    """Encodes an image to base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_action_from_vision(image_path, goal):
    """Sends the screen capture to GPT-4o-Vision to determine the next action."""
    base64_image = encode_image(image_path)
    
    prompt = f"""
    You are an autonomous OS operator. Your goal is: {goal}
    Analyze the attached screenshot of the user's desktop.
    Identify the next logical step to achieve the goal.
    
    Respond STRICTLY in JSON format with the following structure:
    {{
        "reasoning": "Brief explanation of what you see and why this action is next",
        "action": "click" | "double_click" | "type" | "press" | "wait",
        "params": {{
            "x": 0, (normalized 0-1000 for width)
            "y": 0, (normalized 0-1000 for height)
            "text": "string if typing",
            "key": "string if pressing key"
        }},
        "status": "in_progress" | "completed"
    }}
    
    Note: Use a coordinate system from 0 to 1000 for both X and Y.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {{
                "role": "user",
                "content": [
                    {{"type": "text", "text": prompt}},
                    {{
                        "type": "image_url",
                        "image_url": {{"url": f"data:image/png;base64,{{base64_image}}"}}
                    }}
                ]
            }}
        ],
        response_format={{ "type": "json_object" }}
    )
    
    import json
    return json.loads(response.choices[0].message.content)
